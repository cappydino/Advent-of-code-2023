from collections import deque

with open('./day_23/input.txt', 'r') as file:
    grid = file.read().splitlines()

st = (0, grid[0].index('.'))
end = (len(grid) - 1, grid[-1].index('.'))

graph = {}

q = deque([(st, st, st, 1)])
seen = set()

while q:
    node1, (lr, lc), (r, c), w = q.popleft()

    nextPos = []
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or (nr, nc) == (lr, lc):
            continue

        if (nr, nc) == end:
            if node1 in graph:
                graph[node1].append((end, w))
            else:
                graph[node1] = [(end, w)]

        if grid[nr][nc] != '#':
            nextPos.append((nr, nc))
        
    if len(nextPos) == 1:
        q.append([node1, (r, c), nextPos[0], w + 1])
    elif len(nextPos) > 1:
        if node1 in graph:
            graph[node1].append(((r, c), w))
        else:
            graph[node1] = [((r, c), w)]
        for branch in nextPos:
            if ((r, c), branch) in seen:
                continue
            q.append([(r, c), (r, c), branch, 1])
            seen.add(((r, c), branch))

print('map made')

maxPath = 0
q = deque([(st, [st], 0)])

while q:
    node1, route, w = q.pop()
    paths = graph[node1]
    for pathNode1, pathW in paths:
        if pathNode1 in route:
            continue
        if pathNode1 == end:
            maxPath = max(maxPath, w + pathW)
            print(maxPath)
            continue
        if not (pathNode1, route + [pathNode1], w + pathW) in q:
            q.append((pathNode1, route + [pathNode1], w + pathW))

print(maxPath)