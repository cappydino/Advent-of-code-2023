with open("./day_3/input.txt", "r") as file:
    schematic = file.readlines()

symbols = ["*", "+", "&", "/", "#", "%", "@", "=", "-", "$"]


def charIsSymbol(char):
    for symbol in symbols:
        if char == symbol:
            return True
    return False


def symbolInString(str):
    for char in str:
        if charIsSymbol(char):
            return True
    return False


def findNumbers(line):
    numbers = []
    onNum = False
    startIndex = 0

    for i, char in enumerate(line):
        try:
            int(char)
        except ValueError:
            if onNum:
                numbers.append([startIndex, i - 1])
                onNum = False
        else:
            if onNum:
                continue
            startIndex = i
            onNum = True

    if onNum:
        numbers.append([startIndex, len(line) - 1])

    return numbers


schematicSum = 0


# part one
for i, line in enumerate(schematic):
    numbers = findNumbers(line)
    for number in numbers:
        startIndex = number[0]
        endIndex = number[1]

        num = line[startIndex:endIndex+1]

        leftIndex = max(startIndex - 1, 0)
        rightIndex = min(endIndex + 1, len(line) - 1)

        # check characters above
        if i > 0:
            lineAbove = schematic[i-1]
            charsAbove = lineAbove[leftIndex:rightIndex + 1]
            if symbolInString(charsAbove):
                schematicSum += int(line[startIndex:endIndex+1])
                continue

        # check characters to left and right
        if charIsSymbol(line[max(startIndex - 1, 0)]):
            schematicSum += int(line[startIndex:endIndex+1])
            continue

        if charIsSymbol(line[min(endIndex + 1, len(line) - 1)]):
            schematicSum += int(line[startIndex:endIndex+1])
            continue

        # check characters below
        if i < len(schematic) - 1:
            lineBelow = schematic[i+1]
            charsBelow = lineBelow[leftIndex:rightIndex + 1]
            if symbolInString(charsBelow):
                schematicSum += int(line[startIndex:endIndex+1])
                continue

print(schematicSum)


# part two
def findWholeNum(string, index):

    # forward
    i = index
    while i < len(string) - 1:
        try:
            int(string[i + 1])
            i += 1
        except ValueError:
            break
    endIndex = i

    i = index
    while i > 0:
        try:
            int(string[i - 1])
            i -= 1
        except ValueError:
            break
    startIndex = i

    return int(string[startIndex:endIndex + 1])


def charIsNum(char):
    try:
        int(char)
    except ValueError:
        return False
    return True


def findGears(string):
    indicies = []
    for i, char in enumerate(string):
        if char == '*':
            indicies.append(i)
    return indicies


gearRatioSum = 0

for i, line in enumerate(schematic):
    for gearIndex in findGears(line):
        neighbors = []
        # left and right
        if gearIndex > 0:
            if charIsNum(line[gearIndex - 1]):
                neighbors.append((-1, 0))

        if gearIndex < len(line) - 1:
            if charIsNum(line[gearIndex + 1]):
                neighbors.append((1, 0))

        # top
        if i > 0:
            thingy = [False, False, False]

            if gearIndex > 0:
                if charIsNum(schematic[i-1][gearIndex - 1]):
                    thingy[0] = True

            if charIsNum(schematic[i-1][gearIndex]):
                thingy[1] = True

            if gearIndex < len(line) - 1:
                if charIsNum(schematic[i-1][gearIndex + 1]):
                    thingy[2] = True

            if thingy[1]:
                neighbors.append((0, -1))
            else:
                if thingy[0]:
                    neighbors.append((-1, -1))
                if thingy[2]:
                    neighbors.append((1, -1))

        # bottom
        if i < len(line) - 1:
            thingy = [False, False, False]

            if gearIndex > 0:
                if charIsNum(schematic[i+1][gearIndex-1]):
                    thingy[0] = True

                if charIsNum(schematic[i+1][gearIndex]):
                    thingy[1] = True

                if gearIndex < len(line) - 1:
                    if charIsNum(schematic[i+1][gearIndex+1]):
                        thingy[2] = True

            if thingy[1]:
                neighbors.append((0, 1))
            else:
                if thingy[0]:
                    neighbors.append((-1, 1))
                if thingy[2]:
                    neighbors.append((1, 1))

        if len(neighbors) == 2:
            firstGearNum = findWholeNum(
                schematic[i + neighbors[0][1]], gearIndex + neighbors[0][0])

            secondGearNum = findWholeNum(
                schematic[i + neighbors[1][1]], gearIndex + neighbors[1][0])

            gearRatioSum += firstGearNum*secondGearNum

print(gearRatioSum)
