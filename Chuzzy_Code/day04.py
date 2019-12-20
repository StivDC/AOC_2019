import itertools as it

with open("day04input.txt", "r") as f:
    def has_increasing_digits(num):
        return str(num) == "".join(sorted(str(num)))

    def has_identical_adjacent_digits(num): 
        return any([len(list(g)) >= 2 for k, g in it.groupby("".join(sorted(str(num))))])

    def has_exactly_two_identical_adjacent_digits(num):
        return any([len(list(g)) == 2 for k, g in it.groupby("".join(sorted(str(num))))])

    minimum, maximum = [int(num) for num in f.readline().split("-")]

    # Part 1
    print([has_increasing_digits(i) and has_identical_adjacent_digits(i) for i in range(minimum, maximum + 1)].count(True))

    # Part 2      
    print([has_increasing_digits(i) and has_exactly_two_identical_adjacent_digits(i) for i in range(minimum, maximum + 1)].count(True))

