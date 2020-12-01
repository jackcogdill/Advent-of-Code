with open('input') as f:
    orig_mem = list(
        map(int,
            f.read().split(',')))

def calc(noun, verb):
    mem = orig_mem.copy();

    mem[1] = noun
    mem[2] = verb

    i = 0
    while i < len(mem):
        op = mem[i]
        if op == 1:
            j = mem[i + 1]
            k = mem[i + 2]
            out = mem[i + 3]
            mem[out] = mem[j] + mem[k]
        elif op == 2:
            j = mem[i + 1]
            k = mem[i + 2]
            out = mem[i + 3]
            mem[out] = mem[j] * mem[k]
        else: # 99 = quit
            break
        i += 4

    return mem[0]

# Part one
print(calc(12, 2))

# Part two
for noun in range(100):
    for verb in range(100):
        if calc(noun, verb) == 19690720:
            print(100 * noun + verb)
