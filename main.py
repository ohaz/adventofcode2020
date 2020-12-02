from day1 import day1
from day2 import day2

days = [(day1.sub1, day1.sub2), (day2.sub1, day2.sub2)]

for index, day in enumerate(days):
    print(f'* Running day {index}')
    print('- Running part 1')
    day[0]()
    print('- Running part 2')
    day[1]()