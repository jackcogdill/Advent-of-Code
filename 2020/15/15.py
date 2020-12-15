from collections import defaultdict

with open('input') as f:
    nums = list(map(int, f.read().split(',')))

def play(S):
    last = defaultdict(lambda: (0, 0))

    for turn in range(1, len(nums) + 1):
        n = nums[turn - 1]
        p = last[n] = 0, turn

    for turn in range(turn + 1, S + 1):
        n = p[1] - (p[0] or p[1])
        p = last[n] = last[n][1], turn

    return n

# Part 1
print(play(2020))

# Part 2
print(play(30000000))
