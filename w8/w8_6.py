import itertools

def get_combinations(s, k):
    arr = []
    for i in range(1, k+1):
        arr.append(list(itertools.combinations(s, i)))
    return arr