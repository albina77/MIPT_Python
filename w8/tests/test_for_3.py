import sys, random
from w8_3 import my_zip, my_map, my_enumerate


def square(value):
    return value * 2

def test_for_zip(big_list_zip, big_list_my_zip):
    for i in zip(big_list_zip, big_list_my_zip):
        assert i[0] == i[1]

def test_for_zip2(big_big_list_zip, big_big_list_my_zip):
    for i in zip(big_big_list_zip, big_big_list_my_zip):
        assert i[0] == i[1]

def test_for_map(big_list_map, big_list_my_map):
    for i in zip(big_list_my_map, big_list_map):
        assert i[0] == i[1]

def test_for_enumerate(big_list_enum):
    for i in zip(big_list_enum[0], big_list_enum[1]):
        assert i[0] == i[1]
