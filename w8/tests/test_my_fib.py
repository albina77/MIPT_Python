from w8_2 import my_fib




def test_for_positive(expected):
    for i in range (1, 100):
        assert list(my_fib(i)) == expected[i]


def test_for_negative():
    for j in range (0, -100, -2):
        for i in my_fib(j):
            assert i == 'Nothing'



