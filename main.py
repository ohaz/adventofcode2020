import sys

from day1 import day1
from day2 import day2
from day3 import day3
from day4 import day4
from day5 import day5
from day6 import day6
from day7 import day7
from day8 import day8
from day9 import day9
from day10 import day10
from day11 import day11
from day12 import day12

days = [
    (day1.sub1, day1.sub2),
    (day2.sub1, day2.sub2),
    (day3.sub1, day3.sub2),
    (day4.sub1, day4.sub2),
    (day5.sub1, day5.sub2),
    (day6.sub1, day6.sub2),
    (day7.sub1, day7.sub2),
    (day8.sub1, day8.sub2),
    (day9.sub1, day9.sub2),
    (day10.sub1, day10.sub2),
    (day11.sub1, day11.sub2),
    (day12.sub1, day12.sub2),
    ]

def run_day(index, day):
    print(f'* Running day {index + 1}')
    print('- Running part 1')
    day[0]()
    print('- Running part 2')
    day[1]()


if len(sys.argv) > 1:
    index = int(sys.argv[1]) - 1
    run_day(index, days[index])
    exit()
    

for index, day in enumerate(days):
    run_day(index, day)