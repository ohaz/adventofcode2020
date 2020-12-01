from file_reader import get_file_entries_numbers
from itertools import combinations
import math

def calculator(combination_size, filename='day1/input.txt'):
    numbers = get_file_entries_numbers(filename)
    for element in combinations(numbers, combination_size):
        if sum(element) == 2020:
            print(math.prod(element))

def sub1():
    calculator(2)

def sub2():
    calculator(3)