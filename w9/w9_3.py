class Average(Exception):
    pass


class Dispersion(Exception):
    pass


class Number(Exception):
    pass


def real_coroutine_1():
    s = 0
    n = 0
    s_square = 0
    while True:
        x = yield
        n += 1
        s += x
        s_square += x ** 2
        print('r_c_1: Number of the transferred values: {}.'.format(n))
        print('r_c_1: The average of the transferred values: {}.'.format(s/n))
        print('r_c_1: Dispersion of the transferred values: {}. \n'.format(s_square/n - (s/n)**2))


def real_coroutine_2():
    s = 0
    n = 0
    s_square = 0
    while True:
        try:
            x = yield
            n += 1
            s += x
            s_square += x ** 2
        except Number:
            yield 'r_c_2: Number of the transferred values: {}.'.format(n)
        except Average:
            yield 'r_c_2: The average of the transferred values: {}.'.format(s/n)
        except Dispersion:
            yield 'r_c_2: Dispersion of the transferred values: {}. \n'.format(s_square/n - (s/n)**2)


if __name__ == '__main__':
    a = real_coroutine_1()
    next(a)
    for i in range(10):
        a.send(i)
    a.close()


    a = real_coroutine_2()
    next(a)
    for i in range(10):
        a.send(i)
        if True:
            print(a.throw(Number))
            next(a)
            print(a.throw(Average))
            next(a)
            print(a.throw(Dispersion))
            next(a)
    a.close()

