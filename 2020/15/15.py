from collections import defaultdict

with open('input') as f:
    nums = list(map(int, f.read().split(',')))

def play(S):
    last = {}

    for turn in range(1, len(nums) + 1):
        n = nums[turn - 1]
        p = last[n] = turn

    pp = 0
    for turn in range(turn + 1, S + 1):
        n = p - pp if pp else 0
        pp = last.get(n, 0)
        p = last[n] = turn

    return n

# Part 1
print(play(2020))

# Part 2
print(play(30000000))
