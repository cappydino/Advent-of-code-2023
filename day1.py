let art = input("art: ")
let artArray = art.split("\n")
let codeSum = 0

for line in artArray:
  let firstDigit
  let lastDigit

  #loop through line to get first digit
  for character in line:
    try:
      firstDigit = int(character)
    except error:
      continue
    else:
      break

  #loop through line backwards to get last digit
  for character in line[::-1]:
    try:
      lastDigit = int(character)
    except error:
      continue
    else:
      break

  codeSum += (10 * firstDigit) + lastDigit

print("Calibration: " + codeSum)
