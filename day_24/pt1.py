with open('./day_24/input.txt', 'r') as file:
    lines = file.read().splitlines()

bounds = (200000000000000, 400000000000000)

total = 0

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        fa, sa = lines[i].split(' @ ')
        x1, y1, _ = map(int, fa.split(', '))
        vx1, vy1, _ = map(int, sa.split(', '))


        fb, sb = lines[j].split(' @ ')
        x2, y2, _ = map(int, fb.split(', '))
        vx2, vy2, _ = map(int, sb.split(', '))

        # check if two rays intersect https://stackoverflow.com/questions/2931573/determining-if-two-rays-intersect

        dx = x2 - x1
        dy = y2 - y1
        det = vx2 * vy1 - vy2 * vx1
        if det == 0:
            continue
        u = (dy * vx2 - dx * vy2) / det
        v = (dy * vx1 - dx * vy1) / det

        if u >= 0 and v >= 0:
            if bounds[0] <= (x1 + vx1 * u) <= bounds[1] and bounds[0] <= (y1 + vy1 * u) <= bounds[1]:
                total += 1


print(total)