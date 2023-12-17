with open('./day_16/input.txt', 'r') as file:
    theMap = file.read().splitlines()

maxHeated = 0


for i in range(len(theMap[0])*2 + len(theMap) * 2):
    if i < len(theMap[0]):
        explorers = [[i, 0, (0,1)]]
    elif i < len(theMap[0]) * 2:
        explorers = [[i - len(theMap[0]), len(theMap)-1, (0,-1)]]
    elif i < len(theMap[0]) * 2 + len(theMap):
        explorers = [[0, i - len(theMap[0]) * 2, (1,0)]]
    else:
        explorers = [[len(theMap[0]) - 1, i - len(theMap[0]) * 2 - len(theMap), (-1, 0)]]
    explored = set()

    while explorers:
        newExplorers = []
        for dora in explorers:
            if tuple(dora) in explored:
                continue
            if dora[0] < 0 or dora[0] >= len(theMap) or dora[1] < 0 or dora[1] >= len(theMap[0]):
                continue

            explored.add(tuple(dora))
            
            char = theMap[dora[1]][dora[0]]
            split = (False, None)
            if char == '/':
                if dora[2][0] != 0:
                    dora[2] = (0, -dora[2][0])
                elif dora[2][1] != [0]:
                    dora[2] = (-dora[2][1], 0)

            elif char == '\\':
                if dora[2][0] != 0:
                    dora[2] = (0, dora[2][0])
                elif dora[2][1] != 0:
                    dora[2] = (dora[2][1], 0)

            elif char == '|' and dora[2][0] != 0:
                split = (True, [(0, 1), (0, -1)] )

            elif char == '-' and dora[2][1] != 0:
                split = (True, [(1, 0), (-1, 0)] )

            if split[0]:
                for newDir in split[1]:
                    newExplorers.append([dora[0] + newDir[0], dora[1] + newDir[1], newDir])
                continue

            dora[0] = dora[0] + dora[2][0]
            dora[1] = dora[1] + dora[2][1]
            newExplorers.append(dora)
        explorers = newExplorers
            
    uniqueExplored = set((dora[0], dora[1]) for dora in explored)
    maxHeated = max(maxHeated, len(uniqueExplored))


print(maxHeated)