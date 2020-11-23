from multiprocessing import Process, freeze_support, Pool
import random
import matplotlib.pyplot as plt
from datetime import datetime


def _mul(values):
    s = 0
    for value in zip(values[0], values[1]):
        s += value[0] * value[1]
    return s


def cut(arr1, number):
    step = len(arr1) // number
    i = 0
    while i < number - 1:
        yield arr1[step * i : step * (i + 1)]
        i += 1
    yield arr1[step * i:]


if __name__ == '__main__':
    freeze_support()
    a = [random.randint(0, 10 ** 10) for x in range(2 * 10 ** 6)]
    b = [random.randint(0, 10 ** 10) for x in range(2 * 10 ** 6)]
    time_arr = []
    pr = [1, 2, 3, 4, 6, 8]
    for j in pr:
        tmp = []
        pool = Pool(processes=j)
        start = datetime.now()
        result = pool.map(_mul, zip(cut(a, j), cut(b, j)))
        print('result: {}, number of processes: {}'.format(sum(result), j))
        time_arr.append((datetime.now() - start).microseconds)
    plt.plot(pr, time_arr)
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число потоков')
    plt.show()

