from file_reader import get_file_entries_numbers
from itertools import combinations

def possible_options(numbers):
    return {x: sum(x) for x in combinations(numbers, 2)}

def get_first_invalid_number(numbers, preemble_size=25):
    for index, i in enumerate(numbers[preemble_size:]):
        sums = possible_options(numbers[index:index+preemble_size])
        if not i in sums.values():
            return i

def sub1():
    numbers = get_file_entries_numbers('day9/input.txt')
    print(get_first_invalid_number(numbers))

def sub2():
    numbers = get_file_entries_numbers('day9/input.txt')
    searched_number = get_first_invalid_number(numbers)

    size = 3
    while True:
        for index, _ in enumerate(numbers[:-size]):
            if sum(numbers[index:index+size]) == searched_number:
                mi = min(numbers[index:index+size])
                ma = max(numbers[index:index+size])
                print(mi+ma)
                return
        size += 1