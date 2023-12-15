with open('./day_15/input.txt', 'r') as file:
    steps = filter(lambda x: x != '\n', file.read().split(','))

total = 0
for step in steps:
    HASH = 0
    for char in step:
        HASH += ord(char)
        HASH *= 17
        HASH = HASH % 256
    total += HASH

print(total)