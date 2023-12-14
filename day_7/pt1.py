with open("./day_7/input.txt", "r") as file:
    inputs = file.read().splitlines()

cardDict = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'J': 'd',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm'
}
cardTypes = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


sortedHands = []

for hand in inputs:
    metadata = ''
    c = hand.split()[0]
    types = []
    for ct in cardTypes:
        types.append(sum([c[i] == ct for i in range(len(c))]))

    if max(types) == 5:
        metadata += 'a'
    elif max(types) == 4:
        metadata += 'b'
    elif max(types) == 3 and any(types[i] == 2 for i in range(len(cardTypes))):
        metadata += 'c'
    elif max(types) == 3:
        metadata += 'd'
    elif max(types) == 2:
        types.pop(types.index(2))
        if max(types) == 2:
            metadata += 'e'
        else:
            metadata += 'f'
    else:
        metadata += 'g'

    metadata += ''.join([cardDict[c[i]] for i in range(len(c))])
    sortedHands.append([hand, metadata])

sortedHands.sort(key=lambda x: x[1])

gameValue = 0
for i, hand in enumerate(reversed(sortedHands)):
    gameValue += int(hand[0].split()[1]) * (i + 1)

print(gameValue)
