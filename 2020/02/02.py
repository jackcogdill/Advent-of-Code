# Part 1
with open('input') as f:
    valid = 0
    for line in f:
        policy, pw = line.split(': ')
        times, letter = policy.split()
        lo, hi = list(map(int, times.split('-')))
        if lo <= pw.count(letter) <= hi:
            valid += 1
    print(valid)

# Part 2
with open('input') as f:
    valid = 0
    for line in f:
        policy, pw = line.split(': ')
        times, letter = policy.split()
        lo, hi = list(map(int, times.split('-')))
        if [pw[lo - 1], pw[hi - 1]].count(letter) == 1:
            valid += 1
    print(valid)
