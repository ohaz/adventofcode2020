from file_reader import get_file_entries

def partition(ticket, start, end, lower_character='F', upper_character='B'):
    if len(ticket) == 0:
        return start
    middle = int((end+start) / 2)
    character, ticket = ticket[0], ticket[1:]
    if character == lower_character:
        return partition(ticket, start, middle, lower_character, upper_character)
    else:
        return partition(ticket, middle+1, end, lower_character, upper_character)

def find_position(ticket):
    row_define = ticket[:7]
    seat_define = ticket[7:]
    row = partition(row_define, 0, 127)
    seat = partition(seat_define, 0, 7, lower_character='L', upper_character='R')
    seat_id = row*8 + seat
    return seat_id

def sub1():
    tickets = get_file_entries('day5/input.txt')
    highest_seat_id = -1
    for ticket in tickets:
        highest_seat_id = max(highest_seat_id, find_position(ticket))
    print(highest_seat_id)

def sub2():
    tickets = get_file_entries('day5/input.txt')
    seat_ids = []
    for ticket in tickets:
        seat_ids.append(find_position(ticket))
    seat_ids.sort()
    for i in range(seat_ids[0], seat_ids[-1]+1):
        if i not in seat_ids:
            if i-1 in seat_ids and i+1 in seat_ids:
                print(i)
                break