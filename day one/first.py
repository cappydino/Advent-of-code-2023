input("start")

f = open("puzzle_input.txt", "r")
print(2)
artArray = f.readlines()
print(artArray)
f.close()
codeSum = 0

for line in artArray:
  firstDigit = 0
  lastDigit = 0

  #loop through line to get first digit
  for character in line:
    try:
      firstDigit = int(character)
    except ValueError:
      continue
    else:
      break

  #loop through line backwards to get last digit
  for character in line[::-1]:
    try:
      lastDigit = int(character)
    except ValueError:
      continue
    else:
      break

  codeSum += (10 * firstDigit) + lastDigit

print("Calibration: " , codeSum)
