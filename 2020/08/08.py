with open('input') as f:
    instructions = []
    for line in f:
        op, arg = line.split()
        instructions.append((op, int(arg)))

# Part 1
executed = [False] * len(instructions)
accumulator = 0
i = 0
while i < len(instructions):
    if executed[i]: break
    executed[i] = True
    op, n = instructions[i]
    if op == 'acc':
        accumulator += n
        i += 1
    elif op == 'jmp':
        i += n
    elif op == 'nop':
        i += 1
    else:
        print('invalid operator')
        exit(1)
print(accumulator)

# Part 2
mod = ['jmp', 'nop']

def fix(j):
    executed = [False] * len(instructions)
    accumulator = 0
    i = 0
    while i < len(instructions):
        if executed[i]:
            return False
        executed[i] = True
        op, n = instructions[i]
        if i == j:
            op = mod[mod.index(op) ^ 1] # Swap
        if op == 'acc':
            accumulator += n
            i += 1
        elif op == 'jmp':
            i += n
        elif op == 'nop':
            i += 1
        else:
            print('invalid operator')
            exit(1)
    return accumulator

for i, (op, _) in enumerate(instructions):
    if op in mod:
        res = fix(i)
        if res != False:
            print(res)
            break
