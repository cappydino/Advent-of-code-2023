from time import sleep

with open("/workspaces/Advent-of-code-2023/day_5/input.txt", "r") as file:
    almanac = file.read()


blocks = almanac.split("\n\n")[1:]

inputs = list(map(int, almanac.split("\n\n")[0].split(": ")[1].split()))

seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))


for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))

    seeds = new
ms = seeds[0][0]
for seed in seeds:
    ms = min(ms, seed[0])
print(seeds, ms)
