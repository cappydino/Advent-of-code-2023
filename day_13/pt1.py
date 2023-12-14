"""pt1"""

with open("./day_13/input.txt", "r", encoding="utf-8") as file:
    inputs = file.read().split('\n\n')

def reflection(block, isRotated):
    lines = block.split()

    doubles = []
    pastLine = ''
    for i, line in enumerate(lines):
        if line == pastLine:
            doubles.append(i)
        pastLine = line
    
    for i in doubles:
        isReflection = True
        for j in (a := range(min(i, len(lines) - i))):
            if (b := lines[i + j]) != (c := lines[i - 1 - j]):
                isReflection = False
                break
        if isReflection:
            return i * (100 if not isRotated else 1)
    

    rotated = '\n'.join([''.join([lines[i][j] for i in range(len(lines))]) for j in range(len(lines[0]))])
    return reflection(rotated, True)


total = 0

for block in inputs:
    
    total += reflection(block, False)

print(total)