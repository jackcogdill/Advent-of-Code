# Part 1
with open('input') as f:
    groups = f.read().split('\n\n')
    print(sum(
        len(set(
            ''.join(g.split())
        ))
        for g in groups
    ))

# Part 2
with open('input') as f:
    groups = f.read().split('\n\n')
    t = 0
    for g in groups:
        ppl = g.split()
        s = set(ppl[0])
        for i in range(1, len(ppl)):
            s &= set(ppl[i])
        t += len(s)
    print(t)
