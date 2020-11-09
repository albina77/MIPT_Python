import sys, itertools, random
from w8_6 import get_combinations

def test_for_get_combinations(data1, data2, data3):
    for i in [data1, data2, data3]:
        j = random.randint(1, len(i))
        arr = []
        for k in range (1, j+1):
            arr.append(list(itertools.combinations(i, k)))
        assert arr == get_combinations(i, j)