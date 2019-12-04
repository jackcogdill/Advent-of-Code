def get_fuel(mass):
    return int(mass / 3) - 2

def get_fuel_including_fuel(mass):
    total = 0
    while True:
        fuel = get_fuel(mass)
        if fuel <= 0:
            break
        total += fuel
        mass = fuel
    return total

# Part one
with open('input') as f:
    print(sum(
            get_fuel(
                int(line)) # mass
            for line in f))

# Part two
with open('input') as f:
    print(sum(
        get_fuel_including_fuel(
            int(line)) # mass
        for line in f))
