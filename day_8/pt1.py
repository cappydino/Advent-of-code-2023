with open("/workspaces/Advent-of-code-2023/day_8/input.txt", "r") as file:
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

loc = 'AAA'
steps = 0
while loc != 'ZZZ':
    loc = mapDict[loc][0 if instructions[steps %
                                         len(instructions)] == 'L' else 1]
    steps += 1

print(steps)
