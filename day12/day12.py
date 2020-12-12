from file_reader import get_file_entries
from collections import defaultdict
from operator import add, mul
import math

def rotate_facing(facing, rotation):
    locationmap = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    rotation = rotation % 360
    offset = None
    if rotation == 90:
        offset = 1
    elif rotation == 180:
        offset = 2
    elif rotation == 270:
        offset = 3
    elif rotation == 360:
        offset = 4
    facing = locationmap[(locationmap.index(facing) + offset) % len(locationmap)]
    return facing

def walk(commands):
    location = [0, 0]
    facing = [0, 1]
    for command in commands:
        c, a = command[0], int(command[1:])
        if c == 'N':
            location[0] -= a
        elif c == 'S':
            location[0] += a
        elif c == 'W':
            location[1] -= a
        elif c == 'E':
            location[1] += a
        elif c == 'F':
            location[0] += facing[0] * a
            location[1] += facing[1] * a
        elif c == 'R':
            facing = rotate_facing(facing, a)
        elif c == 'L':
            facing = rotate_facing(facing, 360-a)
        else:
            print('Boguscommand', c)
    return location, facing

def sub1():
    commands = get_file_entries('day12/input.txt')
    location, facing = walk(commands)
    print(abs(location[0]) + abs(location[1]))


def rotate_waypoint(waypoint_offset, rotation):
    if rotation == 90:
        waypoint_offset = [waypoint_offset[1], -waypoint_offset[0]]
    elif rotation == 180:
        waypoint_offset = [-waypoint_offset[0], -waypoint_offset[1]]
    elif rotation == 270:
        waypoint_offset = [-waypoint_offset[1], waypoint_offset[0]]
    elif rotation == 360:
        waypoint_offset = waypoint_offset
    return waypoint_offset

def sub2():
    commands = get_file_entries('day12/input.txt')
    ship_location = [0, 0]
    waypoint_offset = [-1, 10]
    for command in commands:
        c, a = command[0], int(command[1:])
        if c == 'N':
            waypoint_offset[0] -= a
        elif c == 'S':
            waypoint_offset[0] += a
        elif c == 'W':
            waypoint_offset[1] -= a
        elif c == 'E':
            waypoint_offset[1] += a
        elif c == 'F':
            ship_location[0] += waypoint_offset[0] * a
            ship_location[1] += waypoint_offset[1] * a
        elif c == 'R':
            waypoint_offset = rotate_waypoint(waypoint_offset, a)
        elif c == 'L':
            waypoint_offset = rotate_waypoint(waypoint_offset, 360-a)
        else:
            print('Boguscommand', c)
    print(abs(ship_location[0]) + abs(ship_location[1]))