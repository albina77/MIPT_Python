import pickle


a = open('1.txt', 'wb')
try:
    pickle.dumps(a)
except:
    print('Impossible to serialize I/O')
# Невозможно сериализовать только I/O объекты, т.к. непонятно, как они будут вести себя после десериализации.
# Закрыт ли будет файл или еще открыт, будет ли он перемещен во время "маринованного" состояния и т.д.


a = range
try:
    pickle.dumps(a)
except:
    print('Impossible to serialize iterable')
# Замариновать можно, после десериализации ведет себя так же.


a = abs
try:
    pickle.dumps(a)
except:
    print('Impossible to serialize built-in functions')
# Замариновать можно, после десериализации ведет себя так же.


from collections import deque
a = deque
try:
    pickle.dumps(a)
except:
    print('Impossible to serialize built-in classes')
# Замариновать можно, после десериализации ведет себя так же. Главное, чтобы при десериализации класс был доступен.


def sq():
    pass


a = sq
try:
    pickle.dumps(a)
except:
    print('Impossible to serialize functions')
# Замариновать можно, после десериализации ведет себя так же. Главное, что при десериализации функция была доступна.


class Sq:
    pass


a = Sq
try:
    pickle.dumps(a)
except:
    print('Impossible to serialize classes')
# Замариновать можно, после десериализации ведет себя так же. Главное, чтобы при десериализации класс был доступен.

