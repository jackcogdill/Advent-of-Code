with open('input') as f:
    adapters = list(map(int, f.read().split()))
    adapters.sort()
    adapters.append(adapters[-1] + 3)

# counts: _,1,2,3
def find_chain(i = 0, jolts = 0, counts = [0] * 4, diffs = []):
    if i == len(adapters):
        return counts, diffs
    while i < len(adapters):
        d = adapters[i] - jolts
        if 1 <= d <= 3:
            copy = counts[:]
            copy[d] += 1
            res = find_chain(i + 1, jolts + d, copy, diffs + [d])
            if res != None:
                return res
        i += 1

counts, diffs = find_chain()

# Part 1
print(counts[1] * counts[3])

# Part 2
arr = [0] * len(diffs)
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, len(arr)):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
n = 1
succ = 1
for i in range(1, len(diffs)):
    if diffs[i] == diffs[i - 1] == 1:
        succ += 1
    elif succ > 1:
        n *= arr[succ]
        succ = 1
print(n)
