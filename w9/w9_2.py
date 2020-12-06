import zipfile as zf
import os
import string
from pathlib import Path


class TextLoader:
    way = None
    my_zip_file = None

    def __init__(self, way):
        self.way = way
        self.my_zip_file = zf.ZipFile(way)
        self.my_zip_file.extractall()

    def __len__(self):
        t = os.listdir(self.way.rstrip('.zip'))
        return len(t)

    def __next__(self):
        tmp = os.listdir(self.way.rstrip('.zip'))
        for i in tmp:
            with open(self.way.rstrip('.zip') + '\\' + i, 'rt', encoding='utf8') as j:
                # удаляем из way расширение ".zip" -> получаем название соответствующей папки
                # i - название файла в нынешней итерации
                tt = str.maketrans(dict.fromkeys(string.punctuation))
                # string.punctuation - даёт строку из всех занков препинания

                # dict.fromkeys(string.punctuation) - создаёт словарь, где ключами являются символы
                # строки string.punctuation

                # str.maketrans - задаёт "таблицу", обозначающую, какой символ (ключ) на что необходимо заменить (зн-е)
                return j.read().lower().translate(tt)  # .lower() - приводит строки к нижнему регистру,
                # .translate() - заменяет в тексте знаки пунктуации на None в соответствии с таблицей tt
        raise StopIteration()

    def __iter__(self):
        return self


basedir = str(Path(__file__).parent)
basedir = os.path.join(basedir, 'sample.zip')
a = TextLoader(basedir)
print(len(a))
print(next(a))
