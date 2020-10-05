str = input()
try:
    str = int(str)
except ValueError:
        print("Oops")
finally: print("Дошел до finally")