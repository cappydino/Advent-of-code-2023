"""pt1"""

with open("./day_1/puzzle_input.txt", "r", encoding="utf-8") as file:
    inputs = file.read().splitlines()

s = 0
for line in inputs:
    nums = list(filter(lambda x: x.isdecimal(), [char for char in line]))
    s += int("".join([nums[0], nums[-1]]))

print(s)
