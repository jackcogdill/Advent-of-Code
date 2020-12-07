import re

def verify(m):
    if m == None:
        print('error parsing')
        exit(1)

with open('input') as f:
    rules = f.read().splitlines()
    mine = 'shiny gold'
    d = {}
    dead = set()
    for rule in rules:
        m = re.fullmatch(r'(.+) bags contain (.+)\.', rule)
        verify(m)
        k, v = m.groups()
        if v == 'no other bags':
            dead.add(k)
            continue
        d[k] = []
        for child in v.split(', '):
            m = re.fullmatch(r'(\d+) (.+) bags?', child)
            verify(m)
            n, color = m.groups()
            d[k].append((int(n), color))

    # Part 1
    t = 0
    for color in d:
        if color == mine: continue
        q = [color]
        while q:
            node = q.pop()
            if node in dead: continue
            if node == mine:
                t += 1
                break
            q += [child for _, child in d[node]]
    print(t)

    # Part 2
    c = {}
    def cost(k):
        if k in dead: return 1
        if k not in c:
            c[k] = 1 + sum(
                n * cost(child)
                for n, child in d[k]
            )
        return c[k]
    print(cost(mine) - 1)
