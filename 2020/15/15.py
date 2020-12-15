from collections import defaultdict

with open('input') as f:
    nums = list(map(int, f.read().split(',')))

def play(S):
    last = defaultdict(list)

    for turn in range(1, len(nums) + 1):
        n = nums[turn - 1]
        last[n] = last[n][-1:] + [turn]

    prev = n
    for turn in range(turn + 1, S + 1):
        if len(last[prev]) == 1:
            n = 0
        else:
            n = last[prev][1] - last[prev][0]
        last[n] = last[n][-1:] + [turn]
        prev = n

    return n

# Part 1
print(play(2020))

# Part 2
print(play(30000000))
