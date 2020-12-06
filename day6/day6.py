from file_reader import get_file_entries

def parse_groups(answers):
    groups = [[]]
    for line in answers:
        if line.strip() == '':
            groups.append([])
        else:
            groups[-1].append(line)
    return groups

def get_group_set(group):
    s = set()
    for person in group:
        for answer in person:
            s.add(answer)
    return s

def group_size(group):
    return len(group)

def sub1():
    all_answers = get_file_entries('day6/input.txt')
    total_answers = 0
    for group in parse_groups(all_answers):
        group_set = get_group_set(group)
        total_answers += len(group_set)
    print(total_answers)

def get_all_yes(group):
    s = get_group_set(group)
    for person in group:
        person_set = set(person)
        s = s - (s - person_set)
    return s

def sub2():
    all_answers = get_file_entries('day6/input.txt')
    total_answers = 0
    for group in parse_groups(all_answers):
        group_set = get_all_yes(group)
        total_answers += len(group_set)
    print(total_answers)