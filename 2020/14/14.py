import re
from itertools import product

with open('input') as f:
    lines = f.read().splitlines()

def dec2list(x, pad):
    return list(bin(x)[2:].rjust(pad, '0'))

def list2dec(L):
    return int(''.join(L), base=2)

# Part 1
mask = ''
mem = {}
for line in lines:
    m = re.fullmatch(r'mask = (.+)', line)
    if m:
        mask = m.group(1)
        continue
    m = re.fullmatch(r'mem\[(\d+)\] = (\d+)', line)
    if m:
        addr, val = map(int, m.groups())
        val = dec2list(val, len(mask))
        for i, bit in enumerate(mask):
            if bit != 'X':
                val[i] = bit
        mem[addr] = list2dec(val)
        continue
    print('error parsing')
    exit(1)
print(sum(mem.values()))

# Part 2
mask = ''
mem = {}
for line in lines:
    m = re.fullmatch(r'mask = (.+)', line)
    if m:
        mask = m.group(1)
        continue
    m = re.fullmatch(r'mem\[(\d+)\] = (\d+)', line)
    if m:
        addr, val = map(int, m.groups())
        addr = dec2list(addr, len(mask))
        for i, bit in enumerate(mask):
            if bit in '1X':
                addr[i] = bit
        for bits in product('01', repeat=addr.count('X')):
            copy = addr[:]
            i = 0
            for j, bit in enumerate(copy):
                if bit == 'X':
                    copy[j] = bits[i]
                    i += 1
            a = list2dec(copy)
            mem[a] = val
        continue
    print('error parsing')
    exit(1)
print(sum(mem.values()))
