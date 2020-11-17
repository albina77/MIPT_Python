class PrintCurrent(Exception):
    pass

class PrintSum(Exception):
    pass

def sum_coroutine():
    print("Starting coroutine")
    s = 0
    try:
        while True:
            try:
                x = yield
                s += x
            except PrintCurrent:
                yield x
            except PrintSum:
                yield s
    finally:
        print("Stop coroutine")

coroutine = sum_coroutine()
next(coroutine)
for i in range(12):
    coroutine.send(i)
    if i%2 == 0:
        print("Current element:", coroutine.throw(PrintCurrent))
        next(coroutine)
    if i%3 == 0:
        print("Current sum:", coroutine.throw(PrintSum))
        next(coroutine)

print()
print(coroutine.throw(PrintCurrent))
next(coroutine)

print(coroutine.throw(PrintSum))
next(coroutine)

coroutine.close()