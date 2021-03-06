def my_zip(*iters):
    if len(iters) == 0:
        yield None
    else:
        min_len = len(iters[0])
    for i in iters:
        if len(i) < min_len:
            min_len = len(i)
    for i in range (min_len):
        yield tuple(j[i] for j in  iters)

def my_map(function, iterable):
    for i in iterable:
        yield function(i)

def my_enumerate(iterable, start = 0):
    for i in iterable:
        yield start, i
        start += 1

