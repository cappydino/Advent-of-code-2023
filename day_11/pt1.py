"""pt1"""

with open("/workspaces/Advent-of-code-2023/day_11/input.txt", "r", encoding="utf-8") as file:
    inputs = file.read().splitlines()

doubleRows = [i for i in range(len(inputs)) if not '#' in inputs[i]]
doubleColumns = [i for i in range(len(inputs[0])) if not '#' in [line[i] for line in inputs]]
galaxies = [(x,y) for x in range(len(inputs[0])) for y in range(len(inputs)) if inputs[x][y] == '#']

distSum = 0

for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        a,b = galaxies[i], galaxies[j]
        c = abs(a[0] - b[0])
        d = abs(a[1] - b[1])
        r1 = list(range(min(a[0], b[0]), max(a[0], b[0])))
        c1 = list(range(min(a[1], b[1]), max(a[1], b[1])))
        
        e = sum([r in r1 for r in doubleRows])
        f = sum([c in c1 for c in doubleColumns])
        distSum += c + d + e + f

print(distSum)
