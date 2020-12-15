from file_reader import get_file_entries
import re
from collections import defaultdict, deque

def run(amount):
    numbers = defaultdict(lambda: deque([], maxlen=2))
    starting_numbers = [int(x) for x in get_file_entries('day15/input.txt')[0].split(',')]
    for index, number in enumerate(starting_numbers):
        numbers[number].append(index)
    last_number = starting_numbers[-1]
    for turn_number in range(len(starting_numbers), amount):
        if len(numbers[last_number]) < 2:
            new_last_number = 0
        else:
            new_last_number = numbers[last_number][0] - numbers[last_number][1]
        numbers[new_last_number].appendleft(turn_number)
        last_number = new_last_number
    print(last_number)

def sub1():
    run(2020)

def sub2():
    run(30000000)