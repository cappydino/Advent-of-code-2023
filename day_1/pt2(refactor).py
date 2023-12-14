"""pt2"""

with open("./day_1/puzzle_input.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

digits = ["one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine"]

s = 0

for line in lines:
    num = ''
    for i, char in enumerate(line):
        if char.isdecimal():
            num = char
            break

        if any(writtenOut := [line[i:].startswith(digit) for digit in digits]):
            num += str(writtenOut.index(True) + 1)
            break


    for i, char in enumerate(line[::-1]):
        if char.isdecimal():
            num += char
            break

        if any(writtenOut := [line[len(line)-1-i::-1].startswith(digit[::-1]) for digit in digits]):
            num += str(writtenOut.index(True) + 1)
            break

    s += int(num)


print(s)
