with open('input') as f:
    grid = list(map(list, f.read().splitlines()))

w = len(grid[0])
h = len(grid)
moves = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, -1),
    (-1, 1),
    (1, 1),
    (-1, -1),
]

def adjacent(grid, x, y):
    for mx, my in moves:
        X = x + mx
        Y = y + my
        if 0 <= X < w and 0 <= Y < h:
            yield grid[Y][X]

def visible(grid, x, y):
    for mx, my in moves:
        X = x + mx
        Y = y + my
        while 0 <= X < w and 0 <= Y < h:
            pos = grid[Y][X]
            if pos != '.':
                yield pos
                break
            X += mx
            Y += my

def update(grid, occupied_threshold, neighbors_gen):
    new = [row[:] for row in grid] # deep copy
    for y in range(h):
        for x in range(w):
            N = list(neighbors_gen(grid, x, y))
            if grid[y][x] == 'L' and all(n != '#' for n in N):
                new[y][x] = '#'
            if grid[y][x] == '#' and sum(n == '#' for n in N) >= occupied_threshold:
                new[y][x] = 'L'
    return new

def life(update_func):
    pp = grid
    p = grid
    curr = update_func(grid)
    while not(curr == p and curr == pp):
        pp = p
        p = curr
        curr = update_func(curr)
    print(sum(map(lambda row: row.count('#'), curr)))

# Part 1
life(lambda g: update(g, 4, adjacent))

# Part 2
life(lambda g: update(g, 5, visible))
