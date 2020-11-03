from w8_2 import my_fib


def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

def test_for_positive():
    for i in range (1, 100):
        expected = [fib(k) for k in range(1, i+1)]
        assert list(my_fib(i)) == expected


def test_for_negative():
    for j in range (0, -100, -2):
        for i in my_fib(j):
            assert i == 'Nothing'


