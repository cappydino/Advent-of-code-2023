from math import lcm

with open("./day_8/input.txt", "r") as file:
    inputs = file.read().splitlines()

instructions = inputs[0]

mapDict = {}
for line in inputs[2:]:
    s = line.split(' = (')
    a = s[0]
    sa = s[1].split(', ')
    b = sa[0]
    c = sa[1][0:3]
    mapDict[a] = (b, c)

locs = list(filter(lambda x: x[2] == 'A', [inp[:3]
            for inp in inputs[2:]]))

# the loops will all meet up at the lcm of each loop length

loops = []

for loc in locs:
    cloc = loc
    steps = 0
    while cloc[2] != 'Z':
        cloc = mapDict[cloc][0 if instructions[steps %
                                               len(instructions)] == 'L' else 1]
        steps += 1
    loops.append(steps)


print(lcm(lcm(lcm(loops[0], loops[1]), lcm(
    loops[2], loops[3])), lcm(loops[4], loops[5])))
