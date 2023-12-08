with open("/workspaces/Advent-of-code-2023/day_7/input.txt", "r") as file:
    inputs = file.read().splitlines()

cardDict = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'T': 'd',
    '9': 'e',
    '8': 'f',
    '7': 'g',
    '6': 'h',
    '5': 'i',
    '4': 'j',
    '3': 'k',
    '2': 'l',
    'J': 'm'
}

sortedHands = []

for hand in inputs:
    metadata = ''
    c = hand.split()[0]
    typesWithJokers = []
    typesWithoutJokers = []
    jokers = sum(c[i] == 'J' for i in range(len(c)))

    for ct in ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
        if ct != 'J':
            typesWithJokers.append(
                sum([c[i] == ct for i in range(len(c))])+jokers)
        typesWithoutJokers.append(sum([c[i] == ct for i in range(len(c))]))

    maxWithJokers = max(typesWithJokers)
    maxOther = max(typesWithoutJokers)

    if maxWithJokers == 5:
        metadata += 'a'
    elif maxWithJokers == 4:
        metadata += 'b'
    elif maxWithJokers == 3:
        if sum([typesWithoutJokers[i] >= 2 for i in range(len(typesWithoutJokers))]) == 2:
            metadata += 'c'
        else:
            metadata += 'd'
    elif maxWithJokers == 2:
        if sum([typesWithoutJokers[i] == 2 for i in range(len(typesWithoutJokers))]) == 2:
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
