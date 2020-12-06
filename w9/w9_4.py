class Disconnect(Exception):
    pass

def write_to_file(f_obj):
    while True:
        try:
            x = yield
            f_obj.write(x + '\n')
        except Disconnect:
            yield
            pass


def connect_user(name):
    with open(name + '.txt', 'w+') as file:
        # c = write_to_file(file)
        # next(c)
        yield from write_to_file(file)
        # x = yield
        # c.send(x)


def task_planner(message, logins):
    len_auth = len('auth ')
    len_disconnect = len('disconnect ')
    len_login = len('0000000000')
    if 'auth' in message:
        _coroutine = connect_user(message[len_auth:])
        next(_coroutine)
        logins[message[len_auth:]] = _coroutine
    elif 'disconnect' in message:
        logins[message[len_disconnect:]].throw(Disconnect)
    elif message[:len_login] in logins:
        logins[message[:len_login]].send(message[len_login + 1:])

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

logins = dict()
for i in connection():
    task_planner(i, logins)






