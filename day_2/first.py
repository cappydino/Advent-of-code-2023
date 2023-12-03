import re 

with open("/workspaces/Advent-of-code-2023/day_2/input-txt", "r") as file:
    lines = file.readlines()


lines = map(lambda x: x.strip("\n"), lines)
powerSum = sum = 0

for game in lines:
    gameNum = int(game.split(": ")[0][5::])
    
    game = game.split(": ")[1]
    draws = re.split(', |; ', game)
    gameIsValid = True
    maxRed = maxGreen = maxBlue = 0

    for draw in draws:
        draw = draw.split(' ')
        
        if draw[1] == 'red':
            maxRed = max(maxRed, int(draw[0]))
        if draw[1] == 'green':
            maxGreen = max(maxGreen, int(draw[0]))
        if draw[1] == 'blue':
            maxBlue = max(maxBlue, int(draw[0]))

        
        if int(draw[0]) > 12 and draw[1] == 'red':
            gameIsValid = False
        elif int(draw[0]) > 13 and draw[1] == 'green':
            gameIsValid = False
        elif int(draw[0]) > 14 and draw[1] == 'blue':
            gameIsValid = False

    if gameIsValid:
        sum += gameNum
    
    powerSum += maxRed * maxGreen * maxBlue


print('pt 1:', sum)
print('pt2', powerSum)