class MyError(Exception):
    def __init__(self, text):
        self.txt = text

try:
    a = int(input("Rate yourself:" ))
    if a <= 0:
        raise MyError("Wrong! You're so beautiful!")
finally: print("Try again")