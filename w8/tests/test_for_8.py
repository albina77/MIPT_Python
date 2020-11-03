import sys, itertools, random
sys.path.append('C:\\Users\\79821\\FilesForGit\\MIPT_Python\\w8')
from w8_8 import compress_string

def test_for_groupby(data1, data2, data3):
    for i in [data1, data2, data3]:
        for el in range (len(i)):
            i.append(itertools.repeat([i[el]], random.randint(1, 100)))
        assert list((len(list(value)), key) for key, value in itertools.groupby(i)) == compress_string(i)