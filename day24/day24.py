from file_reader import get_file_entries
import re
from collections import defaultdict, deque, OrderedDict, namedtuple
from itertools import islice
from copy import copy
try:
    from tqdm import tqdm
except:
    tqdm = lambda x:x

hex_point = namedtuple('HexPoint', ['x', 'y', 'z'])

directions = {
    'e': hex_point(+1, -1, 0),
    'se': hex_point(0, -1, +1),
    'sw': hex_point(-1, 0, +1),
    'w': hex_point(-1, +1, 0),
    'nw': hex_point(0, +1, -1),
    'ne': hex_point(+1, 0, -1)
}

def get_initial_tiles(filename='day24/input.txt'):
    points_visited = set()
    parsed = ''
    for line in get_file_entries(filename):
        current_point = hex_point(0, 0, 0)
        for character in line:
            full_direction = parsed + character
            if full_direction in directions.keys():
                parsed = ''
                vector = directions[full_direction]
                x = current_point.x + vector.x
                y = current_point.y + vector.y
                z = current_point.z + vector.z
                current_point = hex_point(x,y,z)
                assert(x + y + z == 0)
            else:
                parsed = full_direction
        if current_point in points_visited:
            points_visited.remove(current_point)
        else:
            points_visited.add(current_point)
    return points_visited

def sub1():
    points_visited = get_initial_tiles()
    print(len(points_visited))

def adjacent_tiles(tile, include_self=False):
    adjacent = set()
    for direction in directions.values():
        point = hex_point(tile.x + direction.x, tile.y + direction.y, tile.z + direction.z)
        assert(point.x + point.z + point.y == 0)
        adjacent.add(point)
    if include_self:
        adjacent.add(tile)
    return adjacent

def count_adjacent_black_tiles(tile, existing_tiles):
    neighbours = set()
    for adjacent in adjacent_tiles(tile, include_self=False):
        if adjacent in existing_tiles:
            neighbours.add(adjacent)
    return len(neighbours)

def sub2():
    tiles = get_initial_tiles('day24/input.txt')
    DAYS = 100

    for day in tqdm(range(DAYS)):
        new_tiles = set()
        for tile in tiles:
            adjacents = adjacent_tiles(tile, include_self=True)
            for current_tile in adjacents:
                if current_tile in new_tiles:
                    continue
                black_neighbours = count_adjacent_black_tiles(current_tile, tiles)
                if current_tile in tiles:
                    if black_neighbours == 1 or black_neighbours == 2:
                        new_tiles.add(current_tile)
                else:
                    if black_neighbours == 2:
                        new_tiles.add(current_tile)
        tiles = copy(new_tiles)
    print(len(tiles))
