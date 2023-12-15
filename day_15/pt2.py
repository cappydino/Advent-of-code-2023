with open('./day_15/input.txt', 'r') as file:
    steps = filter(lambda x: x != '\n', file.read().split(','))

def hashValue(string):
    h = 0
    for char in string:
        h += ord(char)
        h *= 17
        h = h % 256
    return h

boxes = [ [] for _ in range(256)]

for step in steps:
    if '=' in step:
        lens, value = step.split('=')
        bIndex = hashValue(lens)
        if lens in (b := [boxes[bIndex][i].split(' ')[0] for i in range(len(boxes[bIndex]))]):
            boxes[bIndex][b.index(lens)] = ' '.join([lens, value])
        else:
            boxes[bIndex].append(' '.join([lens, value]))
    elif '-' in step:
        lens = step[:-1]
        bIndex = hashValue(lens)
        if lens in (b := [boxes[bIndex][i].split(' ')[0] for i in range(len(boxes[bIndex]))]):
            lIndex = b.index(lens)
            del boxes[bIndex][lIndex]



total = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        total += (i+1) * (j+1) * int(lens.split(' ')[1])

print(total)