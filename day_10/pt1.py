"""pt1"""

with open("/workspaces/Advent-of-code-2023/day_10/input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

connections = {
    'S': "NSEW",
    '|': "NS",
    '-': "EW",
    'L': "NE",
    'J': "NW",
    '7': "SW",
    'F': "SE",
    '.': ''
}
oppositeDir = {
    'N': 'S',
    'S': 'N',
    'W': 'E',
    'E': 'W'
}
lineLength = inputs.find('\n') + 1

def ic(index):
    return (index % lineLength, index // lineLength)

def ci(coords):
    return coords[0] + coords[1] * lineLength

def addCoords(coordsA, coordsB):
    return (coordsA[0] + coordsB[0], coordsA[1] + coordsB[1])

def connects(pipeA, dir, pipeB):
    if dir == 'N':
        return 'N' in connections[pipeA] and 'S' in connections[pipeB]
    if dir == 'S':
        return 'S' in connections[pipeA] and 'N' in connections[pipeB]
    if dir == 'W':
        return 'W' in connections[pipeA] and 'E' in connections[pipeB]
    if dir == 'E':
        return 'E' in connections[pipeA] and 'W' in connections[pipeB]

def step(coords, dir):
    if dir == 'N':
        return (coords[0], coords[1] - 1)
    if dir == 'S':
        return (coords[0], coords[1] + 1)
    if dir == 'E':
        return (coords[0] + 1, coords[1])
    if dir == 'W':
        return (coords[0] - 1, coords[1])

def coordConnects(coords, dir):
    try:
        return connects(inputs[ci(coords)], dir, inputs[ci(step(coords, dir))])
    except IndexError:
        return False

def moveThroughPipe(coordDir):
    coord, dir = coordDir
    for oc in "NSEW".replace(oppositeDir[dir], ''):
        if coordConnects(coord, oc):
            return (step(coord, oc), oc)

startCoords =  ic(inputs.find("S"))
coordDirs = []

for dir in "NSWE":
    if coordConnects(startCoords, dir):
        coordDirs.append((step(startCoords, dir), dir))

lastCD = coordDirs
steps = 0
while not any([coordDirs[0][0] == lastCD[1][0], coordDirs[1][0] == lastCD[0][0], lastCD[0][0] == lastCD[1][0]]):
    lastCD = coordDirs
    coordDirs = list(map(moveThroughPipe, coordDirs))
    steps += 1

print(steps)