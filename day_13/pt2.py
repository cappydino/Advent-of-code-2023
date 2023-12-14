"""pt1"""

with open("./day_13/input.txt", "r", encoding="utf-8") as file:
    inputs = file.read().split('\n\n')

def reflection(block):
    lines = block.split()

    for possibleReflection in range(1, len(lines)):
        reflected = True
        smudges = 0
        for i in (l := range(min(possibleReflection, len(lines) - possibleReflection))):
            top = lines[possibleReflection + i]
            bottom = lines[possibleReflection - 1 - i]
            differences = sum([top[j] != bottom[j] for j in range(len(top))])
            if differences > 1 or (differences > 0 and smudges > 0):
                reflected = False
                break
            if differences == 1:
                smudges = 1
        if reflected and smudges == 1:
            return possibleReflection * 100
    
    for possibleReflection in range(1, len(lines[0])):
        reflected = True
        smudges = 0
        for i in range(min(possibleReflection, len(lines[0]) - possibleReflection)):
            right = [lines[j][possibleReflection + i] for j in range(len(lines))]
            left = [lines[j][possibleReflection - 1 - i] for j in range(len(lines))]
            differences = sum([left[j] != right[j] for j in range(len(left))])
            if differences > 1 or (differences > 0 and smudges > 0):
                reflected = False
                break
            if differences == 1:
                smudges = 1
        if reflected and smudges == 1:
            return possibleReflection



total = 0

for block in inputs:
    
    total += reflection(block)

print (total)