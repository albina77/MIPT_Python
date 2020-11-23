from multiprocessing import Process, freeze_support
import random
import matplotlib.pyplot as plt
from datetime import datetime


def _mul(arg1, arg2):
    s = 0
    for i in zip(arg1, arg2):
        s += i[0] * i[1]


def cut(arr, number):
    step = len(arr) // number
    i = 0
    while i < number - 1:
        yield arr[step * i, step * (i + 1)]
        i += 1
    yield arr[step * i:]


if __name__ == '__main__':
    freeze_support()
    a = [random.randint(0, 10 ** 10) for x in range(2 * 10 ** 6)]
    b = [random.randint(0, 10 ** 10) for x in range(2 * 10 ** 6)]
    time_arr = []
    pr = [1, 2, 3, 4, 6, 8]
    for j in pr:
        tmp = []
        for qwerty in range(3):
            processes = []
            for values in zip(cut(a, j), cut(b, j)):
                processes.append(Process(target=_mul, args=(values[0], values[1])))
            for process in processes:
                process.start()
                start = datetime.now()
            for process in processes:
                process.join()
            tmp.append((datetime.now() - start).total_seconds())
        time_arr.append(sum(tmp) / len(tmp))
    plt.plot(pr, time_arr)
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число потоков')
    plt.show()

