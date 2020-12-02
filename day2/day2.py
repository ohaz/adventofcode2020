import re
from file_reader import get_file_entries

regex = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<policy>\w):\s(?P<password>.*)')

def is_valid_sub1_password(line):
    parsed = regex.match(line)
    amount = parsed.group('password').count(parsed.group('policy'))
    return int(parsed.group('min')) <= amount <= int(parsed.group('max'))

def sub1():
    lines = get_file_entries('./day2/input.txt')
    amount = 0
    for line in lines:
       amount += is_valid_sub1_password(line)
    print(amount)

def is_valid_sub2_password(line):
    parsed = regex.match(line)
    position1 = int(parsed.group('min')) - 1
    position2 = int(parsed.group('max')) - 1
    password = parsed.group('password')
    policy = parsed.group('policy')
    amount = 0
    amount = amount + 1 if password[position1] == policy else amount
    amount = amount + 1 if password[position2] == policy else amount
    return amount == 1

def sub2():
    lines = get_file_entries('./day2/input.txt')
    amount = 0
    for line in lines:
        amount += is_valid_sub2_password(line)
    print(amount)