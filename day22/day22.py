from file_reader import get_file_entries
import re
from collections import defaultdict, deque, OrderedDict
from itertools import islice
from copy import copy

def parse_cards(filename='day22/input.txt'):
    players = [[], []]
    index = 0
    for line in get_file_entries(filename):
        if 'Player 1:' in line:
            index = 0
            continue
        if 'Player 2:' in line:
            index = 1
            continue
        if '' == line.strip():
            continue
        players[index].append(int(line.strip()))
    return deque(players[0]), deque(players[1])

def sub1():
    player1, player2 = parse_cards('day22/input.txt')
    while len(player1) > 0 and len(player2) > 0:
        c1, c2 = player1.popleft(), player2.popleft()
        if c1 >= c2:
            player1.append(c1)
            player1.append(c2)
        else:
            player2.append(c2)
            player2.append(c1)
    points = 0
    winner = list(player1 if len(player1) > 0 else player2)
    for index, value in enumerate(winner[::-1]):
        points += (index+1)*value
    print(points)


def game(player1, player2):
    previous_rounds = []
    while len(player1) > 0 and len(player2) > 0:
        winner = None
        memory = (list(player1)[:], list(player2)[:])
        if memory in previous_rounds:
            return 1, player1
        else:
            previous_rounds.append(memory)
        c1, c2 = player1.popleft(), player2.popleft()
        if len(player1) >= c1 and len(player2) >= c2:
            new_p1 = deque(islice(copy(player1), 0, c1))
            new_p2 = deque(islice(copy(player2), 0, c2))
            winner, _ = game(new_p1, new_p2)
        else:
            if c1 >= c2:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            player1.append(c1)
            player1.append(c2)
        else:
            player2.append(c2)
            player2.append(c1)
    if len(player1) > 0:
        return 1, player1
    return 2, player2
    

def sub2():
    player1, player2 = parse_cards('day22/input.txt')

    winner, cards = game(player1, player2)
    cards = list(cards)
    points = 0
    for index, value in enumerate(cards[::-1]):
        points += (index+1)*value
    print(points)

