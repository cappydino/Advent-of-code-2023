with open("/workspaces/Advent-of-code-2023/day_6/input.txt", "r") as file:
    inputs = file.readlines()

times = inputs[0].split()[1:]
records = inputs[1].split()[1:]

output = 1

for i in range(len(times)):
    time = int(times[i])
    record = int(records[i])

    minTime = time
    maxTime = 0

    for t in range(time):
        d = t * (time - t)
        if d > record:
            print(t, d)
            minTime = t
            break

    for t in range(time, 0, -1):
        d = t * (time - t)
        if d > record:
            print(t, d)
            maxTime = t
            break

    output *= maxTime - minTime + 1

print(output)
