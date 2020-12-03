from math import prod

with open('input') as f:
    data = f.read().splitlines()

def find_trees(slope):
    sx, sy = slope
    trees = 0
    x = 0
    y = 0
    w = len(data[0])
    h = len(data)
    while y < h - sy:
        x = (x + sx) % w
        y += sy
        if data[y][x] == '#':
            trees += 1
    return trees

# Part 1
print(find_trees((3, 1)))

# Part 2
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
print(prod(map(find_trees, slopes)))
