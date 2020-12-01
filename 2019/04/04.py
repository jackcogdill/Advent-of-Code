input_range = '402328-864247'
start, end = list(map(int, input_range.split('-')))

# Thank you https://stackoverflow.com/a/6309535/1313757
import re
repeat_matcher = re.compile(r'(\d)\1*')
get_repeats = lambda s: [
    m.group()
    for m in repeat_matcher.finditer(s)]

def no_decrease(n):
    # Going from left to right, the digits never decrease; they only ever
    # increase or stay the same (like 111123 or 135679).
    t = n
    prev = t % 10
    t //= 10
    while t > 0: # Iterate through digits backwards
        d = t % 10
        if prev < d: # Found decrease
            return False
        prev = d
        t //= 10
    return True

def has_double(n):
    # Two adjacent digits are the same (like 22 in 122345).
    return any(
        len(r) >= 2
        for r in get_repeats(str(n)))

def has_exact_double(n):
    # The two adjacent matching digits are not part of a larger group of
    # matching digits (like 112233 but not 123444).
    return any(
        len(r) == 2
        for r in get_repeats(str(n)))

# Part one
print(sum(1
          for n in range(start, end + 1)
          if no_decrease(n) and has_double(n)))

# Part two
print(sum(1
          for n in range(start, end + 1)
          if no_decrease(n) and has_exact_double(n)))
