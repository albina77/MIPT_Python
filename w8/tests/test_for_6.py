import sys, itertools, random
sys.path.append('C:\\Users\\79821\\FilesForGit\\MIPT_Python\\w8')
from w8_6 import get_combinations

def test_for_get_combinations(data1, data2, data3):
    for i in [data1, data2, data3]:
        j = random.randint(1, len(i))
        arr = []
        for k in range (1, j+1):
            arr.append(list(itertools.combinations(i, k)))
        assert arr == get_combinations(i, j)