# Courtesy of
# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
def get_segment_intersection(l1, l2):
    # Points
    p1, p2 = l1
    p3, p4 = l2
    # Coords
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denom = ((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4))
    if denom == 0:
        return None

    t = (((x1-x3)*(y3-y4)) - ((y1-y3)*(x3-x4))) / denom
    u = -(((x1-x2)*(y1-y3)) - ((y1-y2)*(x1-x3))) / denom

    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1+t*(x2-x1), y1+t*(y2-y1))
        # OR
        # return (x3+u*(x4-x3), y3+u*(y4-y3))
    else:
        return None

# Setup
# -----
with open('input') as f:
    wires = f.read().split()

port = (0, 0)
all_pairs_and_steps = []

# Store line segments
# -------------------
for wire in wires:
    pos = port
    dirs = wire.split(',')
    pairs_and_steps = []
    steps = 0

    for p in dirs:
        d = p[0]
        n = int(p[1:])
        if d == 'U':
            move = (0, 1)
        elif d == 'D':
            move = (0, -1)
        elif d == 'L':
            move = (-1, 0)
        elif d == 'R':
            move = (1, 0)

        end = (pos[0] + move[0] * n, pos[1] + move[1] * n)
        pair = (pos, end)
        steps += n

        pairs_and_steps.append((pair, steps))
        pos = end

    all_pairs_and_steps.append(pairs_and_steps)

a = all_pairs_and_steps[0]
b = all_pairs_and_steps[1]

# Find intersections
# ------------------
intersections_and_steps = []
for i in range(len(a)):
    for j in range(len(b)):
        l1, s1 = a[i]
        l2, s2 = b[j]
        intersection = get_segment_intersection(l1, l2)
        if intersection:
            x, y = intersection
            # Points
            p1, p2 = l1
            p3, p4 = l2
            # Coords
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            x4, y4 = p4
            combined_steps = (s1 - abs(x2 - x) - abs(y2 - y)) + (s2 - abs(x4 - x) - abs(y4 - y))
            intersections_and_steps.append((intersection, combined_steps))

# Part one
print(min([abs(x) + abs(y)
           for (x, y), _ in intersections_and_steps
           if (x, y) != port]))

# Part two
print(min([combined_steps
           for (x, y), combined_steps in intersections_and_steps
           if (x, y) != port]))
