from file_reader import get_file_entries
import re
from collections import defaultdict, deque, OrderedDict, namedtuple
from itertools import islice
from copy import copy
try:
    from tqdm import tqdm
except:
    tqdm = lambda x:x

def crack_loop_size(key, subject_number=7):
    value = 1
    loop_size = 0
    while value != key:
        value *= subject_number
        value %= 20201227
        loop_size += 1
    return loop_size

def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value

def sub1():
    card_pub_key = 19774466
    door_pub_key = 7290641

    card_encryption_key = transform(card_pub_key, crack_loop_size(door_pub_key))
    door_encryption_key = transform(door_pub_key, crack_loop_size(card_pub_key))
    print(card_encryption_key)
    assert card_encryption_key == door_encryption_key

def sub2():
    pass