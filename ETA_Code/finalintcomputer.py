class IntComputer():
    """An intcode computer.
    Todo: perhaps change the program from a full array into a defaultdict from collections."""
    def __init__(self, program, start_stack = []):
        self.program = program[:] # Questionable; always copy the input program
        self.pc = 0 # Initialise program counter
        self.rb = 0 # Initialise relative base
        self.inputstack = start_stack
        self.finished = False

    def addinput(self, value):
        self.inputstack.append(value)
    
    def iteration(self, debug):
        """Running a single opcode"""
        previouspc = self.pc
        
        op = self.program[self.pc] % 100
        modes = [self.program[self.pc] // 100 % 10, self.program[self.pc] // 1000 % 10, self.program[self.pc] // 10000 % 10]
        
        if debug: print("pc", self.pc, "\nrb", self.rb, "op", op, "\nmodes", modes, "\nprog", self.program, "\n")
        
        def set(address, value):
            """Set the value at the given address"""
            if address < len(self.program):
                self.program[address] = value
            else:
                self.program += [0] * (1 + address - len(self.program))
                self.program[address] = value
        
        def get(address):
            """Get the value at the given address"""
            if address < len(self.program):
                return self.program[address]
            else:
                return 0

        def convert(val, m):
            """Convert a parameter via the given mode"""
            if m == 0:
                return get(val)
            elif m == 1:
                return val
            elif m == 2:
                return get(self.rb + val)
        
        if op in [1, 2]:
            # Addition or multiplication
            a, b  = convert(get(self.pc+1), modes[0]), convert(get(self.pc+2), modes[1])
            
            """For posterity; this worked"""
            #if modes[2] == 0:
            #    set(get(self.pc+3), a+b if op == 1 else a*b)
            #elif modes[2] == 2:
            #    set(get(self.pc+3) + self.rb, a+b if op == 1 else a*b)
            
            set(get(self.pc+3) + (modes[2] == 2)*self.rb, a+b if op == 1 else a*b)
            
            self.pc += 4
        elif op == 3:
            # Input
            set(get(self.pc+1) + (modes[0] == 2)*self.rb, self.inputstack.pop())
            
            self.pc += 2
        elif op == 4:
            # Output
            self.inputstack.append(convert(get(self.pc+1), modes[0]))
            self.pc += 2
            
            return True
        elif op in [5, 6]:
            # Jump
            if op == 5 and convert(get(self.pc+1), modes[0]) != 0:
                # Jump if not equal
                self.pc = convert(get(self.pc+2), modes[1])
            elif op == 6 and convert(get(self.pc+1), modes[0]) == 0:
                # Jump if equal
                self.pc = convert(get(self.pc+2), modes[1])
            else:
                # No jump
                self.pc += 3
        elif op in [7, 8]:
            # Comparisons
            if op == 7:
                # Less than
                condition = convert(get(self.pc+1), modes[0]) < convert(get(self.pc+2), modes[1])
            elif op == 8:
                # Equal to
                condition = convert(get(self.pc+1), modes[0]) == convert(get(self.pc+2), modes[1])
            
            set(get(self.pc+3) + (modes[2] == 2)*self.rb, int(condition))
            
            self.pc += 4
        elif op == 9:
            # Changing relative base
            self.rb += convert(get(self.pc+1), modes[0])
            self.pc += 2
        
        # Whether the program has reached output yet
        return False

    def run(self, debug = False):
        """Run the intcode computer"""
        while not self.finished:
            self.iteration(debug)
            
            if self.program[self.pc] == 99:
                self.finished = True

    def run_until_output(self, debug = False):
        """Run until it generates some output"""
        while not self.finished:
            #outputted = self.iteration(debug)
            
            if self.iteration(debug): # Break on ouput
                #print(self.pc)
                return
            
            if self.program[self.pc] == 99:
                self.finished = True


quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
comp = IntComputer(quine)
comp.run()
assert(quine == comp.inputstack)

from math import log10
longishnum = [1102,34915192,34915192,7,4,7,99,0]
comp = IntComputer(longishnum)
comp.run()
assert(15 < log10(comp.inputstack.pop()) <= 16)

longnum = [104,1125899906842624,99]
comp = IntComputer(longnum)
comp.run()
assert(comp.inputstack.pop() == longnum[1])

BOOST = [int(x) for x in open("day9input.txt").read().split(',')]
comp = IntComputer(BOOST[:], [1])
comp.run()
assert(2518058886 == comp.inputstack.pop())

comp = IntComputer(BOOST[:], [2])
comp.run()
assert(44292 == comp.inputstack.pop())

tests = [[3,9,8,9,10,9,4,9,99,-1,8], [3,9,7,9,10,9,4,9,99,-1,8], [3,3,1108,-1,8,3,4,3,99],\
         [3,3,1107,-1,8,3,4,3,99], [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],\
        [3,3,1105,-1,9,1101,0,0,12,4,12,99,1],
        [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,\
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,\
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]]
vals = [[7, 8], [7, 8], [7, 8], [7, 8], [-4, 0], [-4, 0], [3, 10]]
results = [[0, 1], [1, 0], [0, 1], [1, 0], [1, 0], [1, 0], [999, 1001]]

for prog, val, result in zip(tests, vals, results):
    comp = IntComputer(prog[:], [val[0]])
    comp.run()
    assert(comp.inputstack[0] == result[0])
    comp = IntComputer(prog[:], [val[1]])
    comp.run()
    assert(comp.inputstack[0] == result[1])
