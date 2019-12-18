import sys

memory = [int(cell) for cell in open("day02input.txt", "r").readline().split(",")]

# Undo HCF instruction
memory[1] = 12
memory[2] = 2

def evaluate(program):
    # Make a copy so the argument doesn't get mutated in the evaluation
    program = program[:]

    for pc in range(0, len(program), 4):
        if program[pc] == 99:
            break
        elif program[pc] == 1:
            addr_in1, addr_in2, addr_out = program[pc + 1], program[pc + 2], program[pc + 3]
            program[addr_out] = program[addr_in1] + program[addr_in2]
        elif program[pc] == 2:
            addr_in1, addr_in2, addr_out = program[pc + 1], program[pc + 2], program[pc + 3]
            program[addr_out] = program[addr_in1] * program[addr_in2]

    return program

# Part 1
print(evaluate(memory))

# Part 2
target = 19690720

for noun in range(100):
    for verb in range(100):
        try:
            memory[1], memory[2] = noun, verb

            if evaluate(memory)[0] == target:
                print(f"Gottem 😎 {100 * noun + verb}")
                break

        except IndexError as ex:
            pass