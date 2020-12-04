import re

required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]
optional = [
    'cid',
]

# Part 1
with open('input') as f:
    valid = 0
    passports = f.read().split('\n\n')
    for pp in passports:
        fields = pp.split()
        keys = list(map(lambda s: s.split(':')[0], fields))
        for f in required:
            if f not in keys:
                break
        else:
            valid += 1
    print(valid)

# Part 2
def is_valid(f):
    k, v = f.split(':')
    if k not in required: return True
    if k == 'byr':
        if re.fullmatch('\d{4}', v) == None: return False
        if not (1920 <= int(v) <= 2002): return False
    if k == 'iyr':
        if re.fullmatch('\d{4}', v) == None: return False
        if not (2010 <= int(v) <= 2020): return False
    if k == 'eyr':
        if re.fullmatch('\d{4}', v) == None: return False
        if not (2020 <= int(v) <= 2030): return False
    if k == 'hgt':
        m = re.fullmatch('(\d+)(cm|in)', v)
        if m == None: return False
        n = int(m.group(1))
        u = m.group(2)
        if u == 'cm' and not (150 <= n <= 193): return False
        if u == 'in' and not (59 <= n <= 76): return False
    if k == 'hcl':
        if re.fullmatch('#[0-9a-f]{6}', v) == None: return False
    if k == 'ecl':
        if re.fullmatch('amb|blu|brn|gry|grn|hzl|oth', v) == None: return False
    if k == 'pid':
        if re.fullmatch('\d{9}', v) == None: return False
    return True

with open('input') as f:
    valid = 0
    passports = f.read().split('\n\n')
    for pp in passports:
        fields = pp.split()
        keys = list(map(lambda s: s.split(':')[0], fields))
        if all(f in keys for f in required) and all(is_valid(f) for f in fields):
            valid += 1
    print(valid)
