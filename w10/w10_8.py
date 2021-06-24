from pythonping import ping
from multiprocessing import Process, freeze_support
from datetime import datetime
import matplotlib.pyplot as plt

def _ping(names):
    for name in names:
        ping(name)

def split_array(arr, number):
    n = len(arr)
    step = n // number
    i = 0
    while i < number - 1:
        yield arr[step*i:step*(i+1)]
        i += 1
    yield arr[step*i:]


if __name__ == '__main__':
    freeze_support()
    hosts = ['8.8.8.8', '93.175.2.172', '17.253.144.10', '93.175.29.204', '192.188.189.145', '87.240.190.78']
    # dns.google, my iphone, apple.com, cs.mipt.ru, 3ka.mipt.ru, vk.com
    data = [[], []]
    for qwerty in range (1, 5):
        tmp = []
        tmp_processes = []
        data[0].append(qwerty)
        for k in range(3):
            for piece in split_array(hosts, qwerty):
                tmp_processes.append(Process(target=_ping, args=(piece,)))
            start = datetime.now()
            for proc in tmp_processes:
                proc.start()
            for proc in tmp_processes:
                proc.join()
            tmp.append((datetime.now() - start).microseconds)
            tmp_processes.clear()
        s = sum(tmp)
        tmp.clear()
        data[1].append(s / 3)


    plt.plot(data[0], data[1])
    plt.grid()
    plt.ylabel('Время выполнения, [мс]')
    plt.xlabel('Число процессов')
    plt.show()

