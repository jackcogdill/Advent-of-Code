from enum import IntEnum
import os

# Util
# ----
class Opcodes(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    QUIT = 99

class Modes(IntEnum):
    POSITION = 0
    IMMEDIATE = 1

def err(s):
    print(s)
    exit(1)

# Intcode computer
# ----------------
def parse_instruction(ins):
    # Any missing modes are 0
    modes = [0] * 3
    j = 0
    op = ins % 100
    ins //= 100
    while ins > 0:
        modes[j] = ins % 10
        j += 1
        ins //= 10
    return op, modes

def get_param(mem, addr, mode):
    v = mem[addr]
    if mode == Modes.POSITION:
        return mem[v]
    elif mode == Modes.IMMEDIATE:
        return v
    else:
        err(f'Error: unrecognized mode {mode}')

def parse_program(orig_mem):
    mem = orig_mem.copy()

    # Notes:
    # Parameters that an instruction writes to will never be in immediate mode

    i = 0
    while i < len(mem):
        op, modes = parse_instruction(mem[i])
        if op == Opcodes.ADD:
            p1 = get_param(mem, i + 1, modes[0])
            p2 = get_param(mem, i + 2, modes[1])
            store = mem[i + 3]
            mem[store] = p1 + p2
            i += 4
        elif op == Opcodes.MULTIPLY:
            p1 = get_param(mem, i + 1, modes[0])
            p2 = get_param(mem, i + 2, modes[1])
            store = mem[i + 3]
            mem[store] = p1 * p2
            i += 4
        elif op == Opcodes.INPUT:
            store = mem[i + 1]
            mem[store] = int(input())
            i += 2
        elif op == Opcodes.OUTPUT:
            p = get_param(mem, i + 1, modes[0])
            print(p)
            i += 2
        elif op == Opcodes.JUMP_IF_TRUE:
            p1 = get_param(mem, i + 1, modes[0])
            if p1 != 0:
                p2 = get_param(mem, i + 2, modes[1])
                i = p2
            else:
                i += 3
        elif op == Opcodes.JUMP_IF_FALSE:
            p1 = get_param(mem, i + 1, modes[0])
            if p1 == 0:
                p2 = get_param(mem, i + 2, modes[1])
                i = p2
            else:
                i += 3
        elif op == Opcodes.LESS_THAN:
            p1 = get_param(mem, i + 1, modes[0])
            p2 = get_param(mem, i + 2, modes[1])
            store = mem[i + 3]
            mem[store] = int(p1 < p2)
            i += 4
        elif op == Opcodes.EQUALS:
            p1 = get_param(mem, i + 1, modes[0])
            p2 = get_param(mem, i + 2, modes[1])
            store = mem[i + 3]
            mem[store] = int(p1 == p2)
            i += 4
        elif op == Opcodes.QUIT:
            i += 1
            break
        else:
            err(f'Error: unrecognized opcode {op}')

# Read program
# ------------
with open('input') as f:
    mem = list(
        map(int,
            f.read().split(',')))

# Part one
print('Enter system ID (1 for AC unit):')
parse_program(mem)

# Part one
print('Enter system ID (5 for thermal radiator):')
parse_program(mem)
