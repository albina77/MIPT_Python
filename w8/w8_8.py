import itertools

def compress_string(s):
    arr = []
    for key, value in itertools.groupby(s):
        arr.append((len(list(value)), key))
    return arr

