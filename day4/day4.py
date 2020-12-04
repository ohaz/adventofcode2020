from file_reader import reader
import re

def parse_passports(filename='day4/input.txt'):
    file = reader('day4/input.txt')
    passports = [{}]
    for line in file.splitlines():
        if line.strip() == '':
            passports.append({})
            continue
        pairs = line.split(' ')
        for pair in pairs:
            key, value = pair.split(':')
            passports[-1][key] = value
    return passports

def keys_valid(passport):
    required_keys_full = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
    required_keys_optional = required_keys_full - set(['cid'])
    keys = set(passport.keys())
    return keys == required_keys_full or keys == required_keys_optional

def birth_year_valid(passport):
    return passport['byr'].isdigit() and 1920 <= int(passport['byr']) <= 2002

def issue_year_valid(passport):
    return passport['iyr'].isdigit() and 2010 <= int(passport['iyr']) <= 2020

def expiration_year_valid(passport):
    return passport['eyr'].isdigit() and 2020 <= int(passport['eyr']) <= 2030

def height_valid(passport):
    height_regex = re.compile(r'^(?P<number>\d+)(?P<unit>cm|in)$')
    if (m := height_regex.match(passport['hgt'])):
        number = int(m.group('number'))
        unit = m.group('unit')
        if unit == 'cm' and 150 <= number <= 193:
            return True
        if unit == 'in' and 59 <= number <= 76:
            return True
    return False

def hair_colour_valid(passport):
    hair_colour_regex = re.compile(r'^\#[0-9a-f]{6}$')
    return hair_colour_regex.match(passport['hcl']) is not None

def eye_colour_valid(passport):
    return passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def passport_id_valid(passport):
    passport_id_regex = re.compile(r'^\d{9}$')
    return passport_id_regex.match(passport['pid']) is not None

def sub1():
    passports = parse_passports()
    valid = 0
    for passport in passports:
        valid += keys_valid(passport)
    print(f'{valid}')

def sub2():
    passports = parse_passports()
    valid_passwords = 0
    for passport in passports:
        is_valid = keys_valid(passport)
        if not is_valid:
            continue
        is_valid &= birth_year_valid(passport)
        is_valid &= issue_year_valid(passport)
        is_valid &= expiration_year_valid(passport)
        is_valid &= height_valid(passport)
        is_valid &= hair_colour_valid(passport)
        is_valid &= eye_colour_valid(passport)
        is_valid &= passport_id_valid(passport)

        valid_passwords += is_valid

    print(f'{valid_passwords}')