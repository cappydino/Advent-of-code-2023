with open('./day_14/input.txt', 'r') as file:
    inputs = file.read().splitlines()

def tilt(inputs, dir):
    key = (''.join(inputs), dir)
    
    result = inputs

    if dir in 'NS':
        if dir == 'S':
            result = result[::-1]
        for i, line in enumerate(result):
            rocks = [j for j, char in enumerate(line) if char == 'O']

            for rock in rocks:
                for j in range(i, -1, -1):
                    if j == i:
                        continue
                    if result[j][rock] in '#O':
                        result[i]   = ''.join(result[i][:rock] + '.' + result[i][rock + 1:])
                        result[j+1] = ''.join(result[j+1][:rock] + 'O' + result[j+1][rock + 1:])
                        break
                    elif j == 0:
                        result[i]   = ''.join(result[i][:rock] + '.' + result[i][rock + 1:])
                        result[0] = ''.join(result[0][:rock] + 'O' + result[0][rock + 1:])
                        break
        
        if dir == 'S':
            result = result[::-1]
        return result
    
    if dir in 'WE':
        if dir == 'E':
            result = [''.join(line[j] for j in range(len(result[0])-1, -1, -1) ) for line in result]
        for i in range(len(result[0])):
            rocks = [j for j in range(len(result)) if result[j][i] == 'O']

            for rock in rocks:
                for j in range(i, -1, -1):
                    if j == i:
                        continue
                    if result[rock][j] in '#O':
                        if j+1 == i:
                            break
                        result[rock] = result[rock][:j+1] + 'O' + result[rock][j+2:i] + '.' + result[rock][i+1:]
                        break
                    elif j == 0:
                        result[rock] = result[rock][:j] + 'O' + result[rock][j+1:i] + '.' + result[rock][i+1:]
        
        if dir == 'E':
            result = [''.join(line[j] for j in range(len(result[0])-1, -1, -1) ) for line in result]
        return result

cacheS = {}
def spin(inputs):
    if ''.join(inputs) in cacheS:
        print(2)
        return cacheS[''.join(inputs)]
    
    cacheS[''.join(inputs)] = (result := tilt(tilt(tilt(tilt(inputs, 'N'), 'W'), 'S'), 'E') )
    return result



lastRounds = []
stableLength = 0
stableStart = 0
for i in range(1000000000):
    inputs = spin(inputs)

    if '\n'.join(inputs) in lastRounds:
        stableLength = len(lastRounds[lastRounds.index('\n'.join(inputs)):])
        stableStart = i - stableLength
        break
    
    lastRounds.append('\n'.join(inputs))

print(stableStart, stableLength)
inputs = lastRounds[stableStart - 1 + (1000000000 - stableStart) % stableLength].splitlines()

load = 0
for i, line in enumerate(inputs):
    load += line.count('O') * (len(inputs) - i)

print(load)