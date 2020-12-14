from file_reader import get_file_entries
import re
from collections import defaultdict

mem = re.compile(r'mem\[(\d*)\] = (\d*)')
mask = re.compile(r'mask = ([01X]*)')

def set_bit(value, bit):
    return value | (1 << bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def new_mask(mask):
    replacements = {}
    for index, value in enumerate(mask[::-1]):
        if value != 'X':
            replacements[index] = int(value)
    return replacements

def sub1():
    lines = get_file_entries('day14/input.txt')
    replacements = {}
    memory = defaultdict(int)
    for command in lines:
        if (match := mask.match(command)) is not None:
            replacements = new_mask(match.group(1))
        elif (match := mem.match(command)) is not None:
            location = int(match.group(1))
            value = int(match.group(2))
            for rkey, rvalue in replacements.items():
                if rvalue == 0:
                    value = clear_bit(value, rkey)
                elif rvalue == 1:
                    value = set_bit(value, rkey)
            memory[location] = value
        else:
            print(f'Could not parse {command}')
    print(sum(memory.values()))

def modify_location(location, mask):
    locations = [location]
    for index, bit in enumerate(mask[::-1]):
        if bit == '0':
            continue
        elif bit == '1':
            for location_index in range(len(locations)):
                locations[location_index] = set_bit(locations[location_index], index)
        elif bit == 'X':
            new_locations = []
            for location_index in range(len(locations)):
                first = set_bit(locations[location_index], index)
                second = clear_bit(locations[location_index], index)
                new_locations.append(first)
                new_locations.append(second)
            locations = new_locations
    return locations

def sub2():
    lines = get_file_entries('day14/input.txt')
    current_mask = None
    memory = defaultdict(int)
    for command in lines:
        if (match := mask.match(command)) is not None:
            current_mask = match.group(1)
        elif (match := mem.match(command)) is not None:
            location = int(match.group(1))
            value = int(match.group(2))
            locations = modify_location(location, current_mask)
            for location in locations:
                memory[location] = value
        else:
            print(f'Could not parse {command}')
    print(sum(memory.values()))