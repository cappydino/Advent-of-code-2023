"""pt1"""

with open("./day_9/input.txt", "r", encoding="utf-8") as file:
    inputs = file.read().splitlines()

def predictNextValue(l):
    if type(l) == int:
        return l
    if all([l[i] == l[i-1] for i in range(len(l))]):
        return l[0]
    return l[-1] + predictNextValue([l[i+1] - l[i] for i in range(len(l) - 1)])

sum = 0
for line in inputs:
    sum += predictNextValue(list(map(int, line.split())))
    
print(sum)