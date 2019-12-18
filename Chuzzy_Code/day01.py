def fuel_needed_for_mass(mass):
    return int(mass) // 3 - 2

def fuel_needed_for_module(mass):
    fuel = fuel_needed_for_mass(mass)
    if fuel < 7:
        return fuel
    else:
        return fuel + fuel_needed_for_module(fuel) # A recursive solution because Im epic

# Part 1
with open("day01input.txt", "r") as f:
    print(sum([fuel_needed_for_mass(mass) for mass in f]))

# Part 2
with open("day01input.txt", "r") as f:
    print(sum([fuel_needed_for_module(mass) for mass in f]))
