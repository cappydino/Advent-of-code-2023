import networkx as nx

g = nx.Graph()

for line in open('./day_25/input.txt'):
    left, right = line.split(':')
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)


g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))





# Good luck runnin this in a year buddy

# from collections import deque

# with open('./day_25/input.txt', 'r') as file:
#     lines = file.read().splitlines()

# wireMap = {}

# for line in lines:
#     k, second = line.split(': ')
#     vs = second.split()
#     if k in wireMap:
#         wireMap[k].update(vs)
#     else:
#         wireMap[k] = set(vs)
#     for v in vs:
#         if v in wireMap:
#             wireMap[v].add(k)
#         else:
#             wireMap[v] = {k,}

# connections = set()
# for key in wireMap.keys():
#     values = wireMap[key]
#     for v in values:
#         connections.add(frozenset([key, v]))

# print(len(connections))

# for i in range(len(connections)):
#     for j in range(i+1, len(connections)):
#         for k in range(j+1, len(connections)):
#             a, b, c = [list(connections)[q] for q in [i, j, k]]
            
#             seen = set()
#             q = deque([list(wireMap.keys())[0]])
            
#             while q:
#                 key = q.popleft()
#                 if key in seen:
#                     continue
#                 seen.add(key)
#                 for v in wireMap[key]:
#                     if key in a and v in a or key in b and v in b or key in c and v in c:
#                         continue
#                     q.append(v)
            
#             if len(seen) != len(seen):
#                 print(len(seen) * (len(wireMap)- len(seen)))
#                 exit(0)