def real_coroutine():
    s = 0
    n = 0
    s_square = 0
    while True:
        x = yield ('Number of the transferred values: {}. \n'.format(n))
        n += 1
        s += x
        s_square += x ** 2
        print('The average of the transferred values: {}.'.format(s/n))
        print('Dispersion of the transferred values: {}.'.format(s_square/n - (s/n)**2))


