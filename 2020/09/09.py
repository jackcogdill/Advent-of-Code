L = 25

with open('input') as f:
    nums = list(map(int, f.read().split()))

# Part 1
for i in range(L, len(nums)):
    pre = nums[i - L:i]
    n = nums[i]
    d = {}
    for p in pre:
        if p in d and p != d[p]:
            break
        d[n - p] = p
    else:
        print(n)
        break

# Part 2
i = 0
j = 2
while j < len(nums):
    cont = nums[i:j]
    s = sum(cont)
    if s > n:
        i += 1
    elif s < n or j - i < 2:
        j += 1
    else:
        print(min(cont) + max(cont))
        break
