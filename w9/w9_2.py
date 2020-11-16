import zipfile as zf
import os
import string
class TextLoader:

    way = None
    my_zip_file = None

    def __init__(self, way):
        self.way = way
        self.my_zip_file = zf.ZipFile(way)
        self.my_zip_file.extractall()

    def __len__(self):
        t =  os.listdir(self.way.rstrip('.zip'))
        return len(t)

    def __next__(self):
        tmp = os.listdir(self.way.rstrip('.zip'))
        for i in tmp:
            with open(self.way.rstrip('.zip') + '\\' + i, 'rt', encoding = 'utf8') as j:
                tt = str.maketrans(dict.fromkeys(string.punctuation))
                return j.read().lower().translate(tt)
        raise StopIteration()

    def __iter__(self):
        return self


a = TextLoader('C:\\Users\\79821\\FilesForGit\\MIPT_Python\\w9\\sample.zip')
print(len(a))
print(next(a))