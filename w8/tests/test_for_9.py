import sys, itertools, random
sys.path.append('C:\\Users\\79821\\FilesForGit\\MIPT_Python\\w8')
from w8_9 import maximize

def func(i, tup):
    sum = 0
    for k in tup:
        sum += k**2
    return sum % i

def test_for_maximize(big_datas):
    for data in big_datas:
        i = random.randint(1, 100)
        a = list(itertools.product(*data))
        b = []
        for j in a:
            b.append(func(i, j))
        assert max(b) == maximize(data, i)