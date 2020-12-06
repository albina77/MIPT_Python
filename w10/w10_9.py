from multiprocessing import Process, freeze_support
import random
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


def _mul(arg1, arg2):
    np.dot(arg1, arg2)


def cut(arr, number):
    res = np.array_split(arr, number)
    for i in res:
        yield i


if __name__ == '__main__':
    freeze_support()
    a = np.random.randint(10**9, size=10**6)
    b = np.random.randint(10**9, size=10**6)
    time_arr = []
    num = [1, 2, 4, 8]
    for j in num:
        ttt = []
        for qwerty in range(5):
            processes = []
            for values in zip(cut(a, j), cut(b, j)):
                processes.append(Process(target=_mul, args=(values[0], values[1])))
            for process in processes:
                process.start()
            start = datetime.now()
            for process in processes:
                process.join()
            ttt.append((datetime.now() - start).microseconds)
        time_arr.append(sum(ttt) / len(ttt))
    plt.plot(num, time_arr)
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число процессов')
    plt.show()

