from file_reader import get_file_entries
import re
from collections import defaultdict, deque, OrderedDict
from itertools import islice
from copy import copy
try:
    from tqdm import tqdm
except:
    tqdm = lambda x:x

def sub1():
    cups = deque([int(x) for x in get_file_entries('day23/input.txt')[0]])
    indices = sorted(list(cups))
    lowest, highest = indices[0], indices[-1]
    moves = 100
    for move in range(moves):
        current_value = cups[0]
        cups.rotate(-1)
        afterwards = [cups.popleft(), cups.popleft(), cups.popleft()]
        destination = current_value - 1
        if destination < lowest:
            destination = highest
        while destination in afterwards:
            destination -= 1
            if destination < lowest:
                destination = highest
        destination = cups.index(destination)
        for cup in afterwards[::-1]:
            cups.insert(destination + 1, cup)

    one = cups.index(1) + 1
    cups.rotate(-one)
    result = ''.join([str(x) for x in cups if x != 1])
    print(result)

RANGE = 1000001
MOVES = 10000000

linked_list = [None] + [-1 for _ in range(RANGE-1)]

def sub2():
    cups = [int(x) for x in get_file_entries('day23/input.txt')[0]]
    lowest = min(cups)
    cups += [x for x in range(max(cups) + 1, RANGE)]
    for index, cup in enumerate(cups[:-1]):
        linked_list[cup] = cups[index + 1]
    linked_list[cups[-1]] = cups[0]
    highest = max(linked_list[1:])

    index = cups[-1]
    for move in tqdm(range(MOVES)):
        current_value = linked_list[index]
        next_value = linked_list[current_value]
        temp_value = linked_list[next_value]
        last_value = linked_list[temp_value]
        destination = current_value - 1
        if destination < lowest:
            destination = highest
        while destination in [next_value, temp_value, last_value]:
            destination -= 1
            if destination < lowest:
                destination = highest
        linked_list[current_value] = linked_list[last_value]
        linked_list[last_value] = linked_list[destination]
        linked_list[destination] = next_value
        index = current_value

    oneplus = linked_list[1]
    oneplusplus = linked_list[oneplus]
    print(f'{oneplus * oneplusplus}')