from math import floor, ceil, sqrt

with open("./day_6/input.txt", "r") as file:
    inputs = file.readlines()

time = int(''.join(inputs[0].split()[1:]))
record = int(''.join(inputs[1].split()[1:]))

# print(time, record)

# d(t) = -t^2 + t*time
# record = d(t)
# -t^2 + t*time - record = 0
# (time +/-sqrt( time^2 - 4*record ))/2
# lowt =   ceil( (time - sqrt(time*time - 4*record)) / 2)
# hight = floor( (time + sqrt(time*time - 4*record)) / 2)

lowt = ceil((time - sqrt(time*time - 4*record)) / 2)
hight = floor((time + sqrt(time*time - 4*record)) / 2)
print(hight - lowt + 1)
