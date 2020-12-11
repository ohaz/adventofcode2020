from file_reader import get_file_entries
from collections import defaultdict
from pprint import pprint
from enum import Enum
from copy import deepcopy

class Seat(Enum):
    EMPTY = 'L'
    FULL = '#'
    ROW = '.'
    OUTSIDE = '*'

def count_neighbours(row_index, column_index, airplane):
    full_spots = 0
    for x in range(row_index - 1, row_index + 2):
        for y in range(column_index - 1, column_index + 2):
            if x == row_index and y == column_index:
                continue
            if airplane[x][y] == Seat.FULL:
                full_spots += 1
    return full_spots


def step(airplane, neighbour_counter, allowed_neighbours=4):
    changed_seats = 0
    new_airplane = deepcopy(airplane)
    for row_index, row in enumerate(airplane):
        for column_index, column in enumerate(row):
            if column == Seat.ROW or column == Seat.OUTSIDE:
                continue
            neighbours = neighbour_counter(row_index, column_index, airplane)
            if column == Seat.EMPTY and neighbours == 0:
                new_airplane[row_index][column_index] = Seat.FULL
                changed_seats += 1
            if column == Seat.FULL and neighbours >= allowed_neighbours:
                new_airplane[row_index][column_index] = Seat.EMPTY
                changed_seats += 1
                    
    return new_airplane, changed_seats

def count_occupied(airplane):
    count = sum([x.count(Seat.FULL) for x in airplane])
    return count

def sub1():
    airplane = []
    for line in get_file_entries('day11/input.txt'):
        airplane.append([Seat.OUTSIDE])
        for character in line:
            airplane[-1].append(Seat(character))
        airplane[-1].append(Seat.OUTSIDE)
    empty_row = [Seat.OUTSIDE for _ in range(len(airplane[0]))]
    airplane.insert(0, empty_row)
    airplane.append(empty_row)
    changed_seats = -1
    while changed_seats != 0:
        airplane, changed_seats = step(airplane, count_neighbours)
    print(count_occupied(airplane))

def go(row_index, column_index, airplane, vector):
    row_index += vector[0]
    column_index += vector[1]
    if airplane[row_index][column_index] == Seat.OUTSIDE:
        return 0
    if airplane[row_index][column_index] == Seat.FULL:
        return 1
    if airplane[row_index][column_index] == Seat.EMPTY:
        return 0
    return go(row_index, column_index, airplane, vector)

def count_neighbours_vector(row_index, column_index, airplane):
    vectors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == 0 and i == 0:
                continue
            vectors.append((i, j))
    full_seats = 0
    for vector in vectors:
        full_seats += go(row_index, column_index, airplane, vector)
    return full_seats

def sub2():
    airplane = []
    for line in get_file_entries('day11/input.txt'):
        airplane.append([Seat.OUTSIDE])
        for character in line:
            airplane[-1].append(Seat(character))
        airplane[-1].append(Seat.OUTSIDE)
    empty_row = [Seat.OUTSIDE for _ in range(len(airplane[0]))]
    airplane.insert(0, empty_row)
    airplane.append(empty_row)
    changed_seats = -1
    while changed_seats != 0:
        airplane, changed_seats = step(airplane, count_neighbours_vector, allowed_neighbours=5)
    print(count_occupied(airplane))
