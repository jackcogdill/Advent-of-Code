from math import cos, sin, pi

with open('input') as f:
    instructions = f.read().splitlines()

def update(d, s, coord):
    return (coord[0] + d[0] * s, coord[1] + d[1] * s)

x, y = 0, 0
d = 1, 0

for i in instructions:
    c = i[0]
    n = int(i[1:])
    if c == 'N':
        x, y = update((0, 1), n, (x, y))
    elif c == 'S':
        x, y = update((0, -1), n, (x, y))
    elif c == 'E':
        x, y = update((1, 0), n, (x, y))
    elif c == 'W':
        x, y = update((-1, 0), n, (x, y))
    elif c == 'L':
        n *= pi / 180
        d = d[0] * cos(n) - d[1] * sin(n), d[0] * sin(n) + d[1] * cos(n)
    elif c == 'R':
        n *= pi / 180
        d = d[0] * cos(-n) - d[1] * sin(-n), d[0] * sin(-n) + d[1] * cos(-n)
    elif c == 'F':
        x, y = update(d, n, (x, y))
print(int(abs(x) + abs(y)))

# Part 2
ship = 0, 0
way = 10, 1
for i in instructions:
    c = i[0]
    n = int(i[1:])
    if c == 'N':
        way = update((0, 1), n, way)
    elif c == 'S':
        way = update((0, -1), n, way)
    elif c == 'E':
        way = update((1, 0), n, way)
    elif c == 'W':
        way = update((-1, 0), n, way)
    elif c == 'L':
        n *= pi / 180
        way = way[0] * cos(n) - way[1] * sin(n), way[0] * sin(n) + way[1] * cos(n)
    elif c == 'R':
        n *= pi / 180
        way = way[0] * cos(-n) - way[1] * sin(-n), way[0] * sin(-n) + way[1] * cos(-n)
    elif c == 'F':
        ship = ship[0] + way[0] * n, ship[1] + way[1] * n
print(round(abs(ship[0]) + abs(ship[1])))
