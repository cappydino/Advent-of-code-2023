with open('./day_21/input.txt', 'r') as file:
    garden = file.read().splitlines()

positions = set()

for i in range(len(garden)):
    for j in range(len(garden[0])):
        if garden[i][j] == 'S':
            positions.add((i, j))

for _ in range(64):
    newPositions = set()
    for x, y in positions:
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx =(x + i) % len(garden)
            ny = (y + j) % len(garden[0])
            if garden[nx][ny] != '#':
                newPositions.add((nx, ny))
    positions = newPositions

print(len(positions))