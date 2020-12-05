def get_seat(p):
    lo = 0
    hi = 128
    for i in range(7):
        mid = (lo + hi) // 2
        if p[i] == 'F': hi = mid
        if p[i] == 'B': lo = mid
    row = lo

    lo = 0
    hi = 8
    for i in range(7, 10):
        mid = (lo + hi) // 2
        if p[i] == 'L': hi = mid
        if p[i] == 'R': lo = mid
    col = lo

    return row * 8 + col

# Part 1
with open('input') as f:
    print(max(get_seat(line) for line in f))

# Part 2
with open('input') as f:
    ids = [get_seat(line) for line in f]
    ids.sort()
    for i in range(1, len(ids) - 1):
        if ids[i + 1] == ids[i] + 2:
            print(ids[i] + 1)
