from time import sleep

with open("./day_4/input.txt", "r") as file:
    cards = file.readlines()


def extractNums(numbers):
    nums = []
    i = 1
    while i < len(numbers):
        nums.append(numbers[i-1:i+1])
        i += 3

    return nums


def findMatches(card):
    cardMatches = 0
    parts = card.split(" | ")
    winningNums = extractNums(parts[0].split(": ")[1])
    ownedNums = extractNums(parts[1])
    for winningNum in winningNums:
        if winningNum in ownedNums:
            cardMatches += 1

    return cardMatches


scoreSum = 0

for card in cards:
    cardScore = 0
    cardMatches = findMatches(card)
    for i in range(cardMatches):
        cardScore = max(1, cardScore * 2)
    scoreSum += cardScore


print("part 1:", scoreSum, "points")

# part 2

ownedCards = [1] * len(cards)
for cardIndex, amountOfCards in enumerate(ownedCards):

    matches = findMatches(cards[cardIndex])
    for i in range(matches):
        ownedCards[cardIndex + 1 + i] += amountOfCards

print("part 2:", sum(ownedCards), "cards")
