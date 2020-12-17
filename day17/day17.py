from file_reader import get_file_entries
import re
from collections import defaultdict, deque

def neighbours(pos):
    _neighbours = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x==0 and y==0 and z==0:
                    continue
                _neighbours.add((pos[0] + x, pos[1] + y, pos[2] + z))
    return _neighbours

def parse_input(filename='day17/input.txt'):
    points = set()
    lines = get_file_entries(filename)
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == '#':
                points.add((x,y,0))
    return points

def existing_neighbours(possible_neighbours, points):
    return [x for x in possible_neighbours if x in points]

def sub1():
    points = parse_input()
    for _ in range(6):
        new_points = set()
        for point in points:
            n = neighbours(point)
            l = len(existing_neighbours(n, points))
            if l == 2 or l == 3:
                new_points.add(point)
            for neighbour in n:
                if len(existing_neighbours(neighbours(neighbour), points)) == 3:
                    new_points.add(neighbour)
        points = new_points
    print(len(points))

def neighbours_4d(pos):
    _neighbours = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    if x==0 and y==0 and z==0 and w==0:
                        continue
                    _neighbours.add((pos[0] + x, pos[1] + y, pos[2] + z, pos[3] + w))
    return _neighbours

def parse_input_4d(filename='day17/input.txt'):
    points = set()
    lines = get_file_entries(filename)
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == '#':
                points.add((x,y,0,0))
    return points

def sub2():
    points = parse_input_4d()
    for _ in range(6):
        new_points = set()
        for point in points:
            n = neighbours_4d(point)
            l = len(existing_neighbours(n, points))
            if l == 2 or l == 3:
                new_points.add(point)
            for neighbour in n:
                if len(existing_neighbours(neighbours_4d(neighbour), points)) == 3:
                    new_points.add(neighbour)
        points = new_points
    print(len(points))