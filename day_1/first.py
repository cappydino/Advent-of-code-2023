
with open("/workspaces/Advent-of-code-2023/day_one/puzzle_input.txt", "r") as file:
  artArray = file.readlines()

valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def isNum(character):
  try:
    int(character)
  except ValueError:
    return False
  return True

def parseLine(line):
  firstDigit = 0
  lastDigit = 0

  forwardLoop = True
  for i, character in enumerate(line):
    if not forwardLoop:
      break

    if isNum(character):
      firstDigit = int(character)
      break

    for value, digit in enumerate(valid_digits):
      if line[i::].startswith(digit):
        firstDigit = value + 1
        forwardLoop = False
        break
  

  backwardLoop = True
  for i, character in enumerate(line[::-1]):
    if not backwardLoop:
      break

    if isNum(character):
      lastDigit = int(character)
      break
    

    for value, digit in enumerate(valid_digits):
      print(line[len(line)-1-i::-1], digit[::-1])
      if line[len(line)-1-i::-1].startswith(digit[::-1]):
        lastDigit = value + 1
        backwardLoop = False
        break


  return (firstDigit * 10) + lastDigit
  

codeSum = 0

for line in artArray:
  codeSum += parseLine(line)
  print(parseLine(line))

print("Calibration: " , codeSum)
