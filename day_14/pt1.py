with open('./day_14/input.txt', 'r') as file:
    inputs = file.read().splitlines()


for i, line in enumerate(inputs):
    rocks = [j for j, char in enumerate(line) if char == 'O']

    for rock in rocks:
        for j in range(i, -1, -1):
            if j == i:
                continue
            if inputs[j][rock] in '#O':
                inputs[i]   = ''.join(inputs[i][:rock] + '.' + inputs[i][rock + 1:])
                inputs[j+1] = ''.join(inputs[j+1][:rock] + 'O' + inputs[j+1][rock + 1:])
                break
            elif j == 0:
                inputs[i]   = ''.join(inputs[i][:rock] + '.' + inputs[i][rock + 1:])
                inputs[0] = ''.join(inputs[0][:rock] + 'O' + inputs[0][rock + 1:])
                break


load = 0
for i, line in enumerate(inputs):
    load += line.count('O') * (len(inputs) - i)

print(load)