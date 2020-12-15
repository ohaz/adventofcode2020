import sys
import importlib
import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


days = [x for x in os.listdir() if x.startswith('day')]
days.sort(key=natural_keys)

def run_day(day):
    module = importlib.import_module(f'{day}.{day}')
    print(f'* Running {day}')
    print('- Running part 1')
    module.sub1()
    print('- Running part 2')
    module.sub2()

if len(sys.argv) > 1:
    day_number = int(sys.argv[1])
    run_day(f'day{day_number}')
    exit()
    

for day in enumerate(days):
    run_day(day)