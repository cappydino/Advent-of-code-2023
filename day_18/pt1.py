with open('./day_18/input.txt', 'r') as file:
    inputs = file.read().splitlines()

dirs = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0)
}

points = [(0, 0)]
b = 0

for line in inputs:
    _, _, x = line.split()
    x = x[2:-1]
    dr, dc = dirs[ "RDLU"[ int( x[-1] ) ] ]
    n = int(x[:-1], 16)
    b += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))
    
A = abs(sum(points[i][0] * (points[i-1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
i = A - b // 2 + 1

print(i + b)