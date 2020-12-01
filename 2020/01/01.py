with open('input') as f:
    nums = [int(line) for line in f]

# Part 1
d = {}
for n in nums:
    if n in d:
        print(n * d[n])
        break
    d[2020 - n] = n

# Part 2
nums.sort()
for i in range(len(nums)):
    t = 2020 - nums[i]
    j = i + 1
    k = len(nums) - 1
    while j < k:
        if nums[j] + nums[k] > t:
            k -= 1
        elif nums[j] + nums[k] < t:
            j += 1
        else:
            print(nums[i] * nums[j] * nums[k])
            break
