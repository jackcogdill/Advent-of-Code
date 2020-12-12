from math import cos, sin, pi

with open('input') as f:
    instructions = f.read().splitlines()

def update(coord, d, s):
    x, y = coord
    dx, dy = d
    return (
        x + dx * s,
        y + dy * s
    )

def rotate(d, deg):
    rad = deg * pi / 180
    dx, dy = d
    return (
        dx * cos(rad) - dy * sin(rad),
        dx * sin(rad) + dy * cos(rad)
    )

def manhattan(pos):
    x, y = pos
    return abs(x) + abs(y)

# Part 1
pos = 0, 0
d = 1, 0
for i in instructions:
    c = i[0]
    n = int(i[1:])
    if c == 'N':
        pos = update(pos, (0, 1), n)
    elif c == 'S':
        pos = update(pos, (0, -1), n)
    elif c == 'E':
        pos = update(pos, (1, 0), n)
    elif c == 'W':
        pos = update(pos, (-1, 0), n)
    elif c == 'L':
        d = rotate(d, n)
    elif c == 'R':
        d = rotate(d, -n)
    elif c == 'F':
        pos = update(pos, d, n)
print(round(manhattan(pos)))

# Part 2
ship = 0, 0
way = 10, 1
for i in instructions:
    c = i[0]
    n = int(i[1:])
    if c == 'N':
        way = update(way, (0, 1), n)
    elif c == 'S':
        way = update(way, (0, -1), n)
    elif c == 'E':
        way = update(way, (1, 0), n)
    elif c == 'W':
        way = update(way, (-1, 0), n)
    elif c == 'L':
        way = rotate(way, n)
    elif c == 'R':
        way = rotate(way, -n)
    elif c == 'F':
        ship = update(ship, way, n)
print(round(manhattan(ship)))
