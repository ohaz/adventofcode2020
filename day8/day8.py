from file_reader import get_file_entries
from copy import copy

accumulator = 0

def accumulate(parameter):
    global accumulator
    accumulator += int(parameter)
    return 1

def jump(parameter):
    return int(parameter)

def noop(parameter):
    return 1

instruction_table = {
    'acc': accumulate,
    'jmp': jump,
    'nop': noop,
}

def parse_command(line):
    instruction, parameter = line.split(' ')
    return instruction, parameter

def run_program(program):
    global accumulator
    accumulator = 0
    instruction_pointer = 0
    instructions_visited = []
    while instruction_pointer not in instructions_visited and instruction_pointer < len(program):
        instructions_visited.append(instruction_pointer)
        instruction, parameter = parse_command(program[instruction_pointer])
        instruction_pointer += instruction_table[instruction](parameter)
    return instruction_pointer >= len(program)

def sub1():
    program = get_file_entries('day8/input.txt')
    run_program(program)
    print(accumulator)

def modify_and_run(program, newcommand, line, index):
    _, parameter = parse_command(line)
    program[index] = f'{newcommand} {parameter}'
    return run_program(program)

def sub2():
    program = get_file_entries('day8/input.txt')
    for index, line in enumerate(program):
        instruction, parameter = parse_command(line)
        ran_successfully = False
        if instruction == 'jmp':
            ran_successfully = modify_and_run(copy(program), 'nop', line, index)
        elif instruction == 'nop':
            ran_successfully = modify_and_run(copy(program), 'jmp', line, index)
        
        if ran_successfully:
            print(accumulator)
            break
