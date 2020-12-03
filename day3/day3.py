from file_reader import reader
from collections import deque
from copy import deepcopy

def read_deques(filename='./day3/input.txt'):
    data = reader(filename)
    deques = []
    for line in data.splitlines():
        new_deque = deque()
        for char in line:
            new_deque.append(char)
        deques.append(new_deque)
    return deques

def rotate_all_once(deques):
    for de in deques:
        de.rotate(-1)

def move(right, down, deques, current_line):
    for _ in range(right):
        rotate_all_once(deques)
    current_line += down
    return current_line

def traverse(deques, right, down):
    trees = 0
    current_line = 0
    while current_line < len(deques):
        if deques[current_line][0] == '#':
            trees += 1
        current_line = move(right, down, deques, current_line)
    return trees

def sub1():
    deques = read_deques()
    trees = traverse(deques, 3, 1)
    print(trees)

def sub2():
    deques = read_deques()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    mul = 1
    for slope in slopes:
        trees = traverse(deepcopy(deques), slope[0], slope[1])
        mul *= trees
    print(mul)