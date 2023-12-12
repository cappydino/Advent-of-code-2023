"""pt1"""

with open("/workspaces/Advent-of-code-2023/day_11/input.txt", "r", encoding="utf-8") as file:
    inputs = file.read().splitlines()

doubleRows = [i for i in range(len(inputs)) if not '#' in inputs[i]]
doubleColumns = [i for i in range(len(inputs[0])) if not '#' in [line[i] for line in inputs]]
galaxies = [(y,x) for x in range(len(inputs[0])) for y in range(len(inputs)) if inputs[x][y] == '#']

ageFactor = 1000000

def translatedPoint(point):
    x,y = point
    doubledColumns = len([column for column in doubleColumns if column < x])
    doubledRows = len([row for row in doubleRows if row < y])
    return((doubledColumns * (ageFactor - 1)) + x, (doubledRows * (ageFactor - 1)) + y)

distSum = 0

for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        a,b = translatedPoint(galaxies[i]), translatedPoint(galaxies[j])
        c = abs(a[0] - b[0])
        d = abs(a[1] - b[1])
        distSum += c + d

print(distSum)
