import numpy as np

with open('input') as f:
    lines = f.read().splitlines()

early = int(lines[0])
buses = [(i, int(bus))
         for i, bus in enumerate(lines[1].split(','))
         if bus != 'x']

# Part 1
def earliest():
    time = early
    while True:
        for _, bus in buses:
            if time % bus == 0:
                return (time - early) * bus
        time += 1
print(earliest())

# Part 2
t = 0
step = 1
for i, bus in buses:
    while (t + i) % bus != 0:
        t += step
    step *= bus
print(t)
