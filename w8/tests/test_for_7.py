import sys, itertools, random
from w8_7 import get_combinations_with_r

def test_for_get_combinations_with_r(data1, data2, data3):
    for i in [data1, data2, data3]:
        j = random.randint(1, len(i))
        assert list(itertools.combinations_with_replacement(i, j)) == get_combinations_with_r(i, j)