"""pt2"""

with open("./day_10/input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

connections = {
    'S': 'NSEW',
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

def coordsConnect(a, b):
    if a[0] - b[0] == 1:
        return coordConnects(a, 'N')
    if b[0] - a[0] == 1:
        return coordConnects(b, 'N')
    if a[1] - b[1] == 1:
        return coordConnects(a, 'W')
    if b[1] - a[1] == 1:
        return coordConnects(b, 'W')

def moveThroughPipe(coordDir):
    coord, dir = coordDir
    for oc in "NSEW".replace(oppositeDir[dir], ''):
        if coordConnects(coord, oc):
            return (step(coord, oc), oc)

startCoords =  ic(inputs.find("S"))
coordDirs = []

pipePoints = [startCoords]
cCoords = ()

actualSConnections = ''
for dir in "NSWE":
    if coordConnects(startCoords, dir):
        cCoords = (step(startCoords, dir), dir)
        actualSConnections += dir
connections['S'] = actualSConnections

while not cCoords[0] in pipePoints:
    pipePoints.append(cCoords[0])
    cCoords = moveThroughPipe(cCoords)


statePath = {
    'out': 'entering',
    'entering': 'in',
    'in': 'exiting',
    'exiting': 'out'
}

inShape = False

sum = 0

for y in range(len(inputs.splitlines())):
    inShape = False
    for x in range(lineLength - 1):
        if (x,y) in pipePoints:
            if "S" in connections[inputs[ci((x, y))]]:
                inShape = not inShape
        else:
            if inShape:
                sum += 1

print(sum)