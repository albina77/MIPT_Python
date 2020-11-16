import threading
import random
import matplotlib.pyplot as plt
from datetime import datetime

sum = 0

def _mul(arg1, arg2):
    s = 0
    for values in zip(arg1, arg2):
        s += values[0] * values[1]
    global sum
    sum += s

a = [random.randint(0, 10**10) for x in range (2 * 10**6)]
b = [random.randint(0, 10**10) for x in range (2 * 10**6)]
n = len(a)
'''
start = datetime.now()
_mul(a, b)
time1 = (datetime.now() - start).seconds
'''
time_arr = []
for j in range(1, 5):
    tmp = []
    for qwerty in range (3):
        start = datetime.now()
        step = n // j
        for i in range(j):
            a1 = a[step*(i-1):step*i]
            b1 = b[step*(i-1):step*i]
            threading.Thread(target=_mul, args=(a1, b1)).start()
        a1 = a[step*(j-1):]
        b1 = b[step*(j-1):]
        threading.Thread(target=_mul, args=(a1, b1)).start()
        tmp.append((datetime.now() - start).microseconds)
    time_ = 0
    for i in tmp:
        time_ += i
    time_iter = time_/len(tmp)
    time_arr.append(time_iter)
plt.plot([1, 2, 3, 4], time_arr)
plt.grid()
plt.ylabel('Время выполнения, [мс]')
plt.xlabel('Число потоков')
plt.show()

