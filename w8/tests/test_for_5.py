import sys, itertools, random
from w8_5 import get_permutations

def test_for_get_permutations(data1, data2, data3):
    for i in [data1, data2, data3]:
        j = random.randint(1, len(i))
        assert list(itertools.permutations(i, j)) == get_permutations(i, j)