import sys, itertools, random
sys.path.append('C:\\Users\\79821\\FilesForGit\\MIPT_Python\\w8')
from w8_7 import get_combinations_with_r

def test_for_get_combinations_with_r(data1, data2, data3):
    for i in [data1, data2, data3]:
        j = random.randint(1, len(i))
        assert list(itertools.combinations_with_replacement(i, j)) == get_combinations_with_r(i, j)