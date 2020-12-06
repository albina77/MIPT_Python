from multiprocessing import Process, freeze_support, Pipe
import random
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


def _mul(arg1, arg2, pre):
    pre.send(np.dot(arg1, arg2))



if __name__ == '__main__':
    freeze_support()
    a = np.random.randint(10**3, size=10**6)
    b = np.random.randint(10**3, size=10**6)
    parent, child = Pipe()
    a1 = np.array_split(a, 2)
    b1 = np.array_split(b,2)
    processes = []
    for first, second, conn in zip(a1, b1, [parent, child]):
        processes.append(Process(target=_mul, args=(first, second, conn)))
    for i in processes:
        i.start()
    for i in processes:
        i.join()
    s = 0
    s += parent.recv()
    s += child.recv()
    print(s)



