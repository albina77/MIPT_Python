from itertools import starmap, product

def function(*args):
    sum = 0
    for i in args:
        sum += i**2
    return sum


def maximize(lists, m):
    maxxx = 0
    for item in starmap(function, list(product(*lists))):
        if item % m > maxxx:
            maxxx = item % m
    return maxxx

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, 1000))