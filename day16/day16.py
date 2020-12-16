from file_reader import get_file_entries
import re
from collections import defaultdict, deque
from pprint import pprint

def parse_file(lines):
    rules_re = re.compile(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)')
    rules = {}
    my_ticket = []
    other_tickets = []
    mode = 0
    for line in lines:
        if '' == line.strip():
            continue
        if 'your ticket:' in line:
            mode = 1
            continue
        elif 'nearby tickets:' in line:
            mode = 2
            continue
        
        if mode == 0:
            if (m:=rules_re.match(line)) is not None:
                rules[m.group(1)] = list(range(int(m.group(2)), int(m.group(3)) + 1)) + list(range(int(m.group(4)), int(m.group(5)) + 1))
        elif mode == 1:
            my_ticket = [int(x) for x in line.split(',')]
        elif mode == 2:
            other_tickets.append([int(x) for x in line.split(',')])
    return rules, my_ticket, other_tickets

def sub1():
    lines = get_file_entries('day16/input.txt')
    rules, my_ticket, other_tickets = parse_file(lines)
    invalid = 0
    for other_ticket in other_tickets:
        for number in other_ticket:
            valid = False
            for rule in rules.values():
                if number in rule:
                    valid = True
            if not valid:
                invalid += number
    print(invalid)

def could_match(number, rule):
    return number in rule

def sub2():
    lines = get_file_entries('day16/input.txt')
    rules, my_ticket, other_tickets = parse_file(lines)
    invalid_tickets = []
    for other_ticket in other_tickets:
        for number in other_ticket:
            valid = False
            for rule in rules.values():
                if number in rule:
                    valid = True
            if not valid:
                invalid_tickets.append(other_ticket)
                break
    for invalid_ticket in invalid_tickets:
        other_tickets.remove(invalid_ticket)

    rules_locations = {}
    for rulekey in rules.keys():
        rules_locations[rulekey] = -1
    
    matches = [set()]
    for number in other_tickets[0]:
        for key, value in rules.items():
            if could_match(number, value):
                matches[-1].add(key)
        matches.append(set())
    del matches[-1]

    for ticket in other_tickets[1:]:
        for index, number in enumerate(ticket):
            not_possible = set()
            for possible_match in matches[index]:
                if not could_match(number, rules[possible_match]):
                    not_possible.add(possible_match)
            matches[index] -= not_possible
    
    while not all([len(x) == 1 for x in matches]):
        for match in matches:
            if len(match) == 1:
                for second_match in matches:
                    if second_match != match:
                        second_match -= match
    
    matches = [list(x)[0] for x in matches]
    mul = 1
    for index, match in enumerate(matches):
        if match.startswith('departure'):
            mul *= my_ticket[index]
    print(mul)