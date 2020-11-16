'''def real_coroutine():
    s = 0
    n = 0
    s_square = 0
    while True:
        x = yield ('Number of the transferred values: {}. \n'.format(n))
        n += 1
        s += x
        s_square += x ** 2
        print('The average of the transferred values: {}.'.format(s/n))
        print('Dispersion of the transferred values: {}.'.format(s_square/n - (s/n)**2))'''

def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"

def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]

for i in connection():
    print(i)
