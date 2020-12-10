from file_reader import get_file_entries_numbers
from collections import defaultdict

def sub1():
    numbers = get_file_entries_numbers('day10/input.txt')
    adapter = max(numbers) + 3
    numbers.sort()
    numbers.append(adapter)
    numbers.insert(0, 0)

    diffs = defaultdict(int)

    for i in range(len(numbers) - 1):
        difference = numbers[i+1] - numbers[i]
        diffs[difference] += 1
    
    print(diffs[1] * diffs[3])


def sub2():
    numbers = get_file_entries_numbers('day10/input.txt')
    adapter = max(numbers) + 3
    numbers.sort()
    numbers.append(adapter)
    numbers.insert(0, 0)

    options = defaultdict(lambda: -1)
    need_to_visit = numbers[::-1]
    options[need_to_visit[0]] = 1
    need_to_visit.pop(0)
    for number in need_to_visit:
        my_options = 0
        for i in range(1,4):
            if options[number + i] != -1:
                my_options += options[number + i]
        options[number] = my_options
    
    print(options[0])