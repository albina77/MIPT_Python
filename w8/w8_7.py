import itertools

def get_combinations_with_r(s, n):
    return list(itertools.combinations_with_replacement(s, n))
