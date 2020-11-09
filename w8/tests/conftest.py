import pytest
import random
import itertools
from w8_2 import my_fib
from w8_3 import my_zip, my_map, my_enumerate
from w8_4 import get_cartesian_product


def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


@pytest.fixture()
def data1():
    return ["Alex", "Bob", "Alice", "John", "Ann"]

@pytest.fixture()
def data2():
    return [25, 17, 34, 24, 42]

@pytest.fixture()
def data3():
    return ["M", "M", "F", "M", "F"]

@pytest.fixture()
def big_datas():
    big_array = []
    n1 = random.randint(1, 5)
    for p in range (n1):
        array = []
        n2 = random.randint(1, 5)
        array = [[] for k in range(n2)]
        for k in range (n2):
            n3 = random.randint(1, 5)
            for j in range (n3):
                    array[k].append(random.randint(1, 1000))
        big_array.append(array)
    return big_array

@pytest.fixture()
def expected():
    EXP = [[]]
    for i in range (1, 100):
        expected = [fib(k) for k in range(1, i+1)]
        EXP.append(expected)
    return EXP

def square(value):
    return value * 2

@pytest.fixture()
def big_list_zip(data1, data2):
    big_list_zip = []
    for i in range(5):
        list_zip = []
        list_my_zip = []
        for values in zip(data1[i:], data2[i:]):
            list_zip.append(values)
        for values in my_zip(data1[i:], data2[i:]):
            list_my_zip.append(values)
        big_list_zip.append(list_zip)
    return big_list_zip

@pytest.fixture()
def big_list_my_zip(data1, data2):
    big_list_my_zip = []
    for i in range(5):
        list_zip = []
        list_my_zip = []
        for values in zip(data1[i:], data2[i:]):
            list_zip.append(values)
        for values in my_zip(data1[i:], data2[i:]):
            list_my_zip.append(values)
        big_list_my_zip.append(list_my_zip)
    return big_list_my_zip

@pytest.fixture()
def big_big_list_zip(data1, data2, data3):
    big_big_list_zip = []
    for i in range(5):
        list_zip = []
        list_my_zip = []
        for values in zip(data1[:i], data2[:i], data3[:i]):
            list_zip.append(values)
        for values in my_zip(data1[:i], data2[:i], data3[:i]):
            list_my_zip.append(values)
        big_big_list_zip.append((list_zip))
    return big_big_list_zip

@pytest.fixture()
def big_big_list_my_zip(data1, data2, data3):
    big_big_list_my_zip = []
    for i in range(5):
        list_zip = []
        list_my_zip = []
        for values in zip(data1[:i], data2[:i], data3[:i]):
            list_zip.append(values)
        for values in my_zip(data1[:i], data2[:i], data3[:i]):
            list_my_zip.append(values)
        big_big_list_my_zip.append(list_my_zip)
    return big_big_list_my_zip

@pytest.fixture()
def big_list_map(data1, data2, data3):
    big_list_map = []
    for i in data1, data2, data3:
        list_map = list(map(square, i))
        list_my_map = list(my_map(square, i))
        big_list_map.append(list_map)
    return big_list_map

@pytest.fixture()
def big_list_my_map(data1, data2, data3):
    big_list_my_map = []
    for i in data1, data2, data3:
        list_map = list(map(square, i))
        list_my_map = list(my_map(square, i))
        big_list_my_map.append(list_my_map)
    return big_list_my_map

@pytest.fixture()
def big_list_enum(data1, data2, data3):
    big_list_enum = []
    big_list_my_enum = []
    for data in data1, data2, data3:
        j = random.randint(0, 1000)
        list_enum, list_my_enum = [], []
        for num, item in enumerate(data, j):
            list_enum.append([num, item])
        for num, item in my_enumerate(data, j):
            list_my_enum.append([num, item])
        big_list_enum.append(list_enum)
        big_list_my_enum.append(list_my_enum)
    return (big_list_enum, big_list_my_enum)



