def print_map(func, iterable):
    while True:
        try:
            print(func(next(iterable)))
        except StopIteration:
            break


def function(x):
    return x ** 2


a = iter([1, 2, 3, 4, 5])
print_map(function, a)

