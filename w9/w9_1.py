class BinTree:
    tree = []
    __curr = None
    length = None
    zero = None

    def __init__(self):
        self.tree = []
        self.__curr = -0.5
        self.length = len(self.tree)
        self.zero = False

    def add(self, value):
        self.tree.append(value)
        self.length += 1

    def __next__(self):
        if self.__curr * 2 + 1 < self.length:
            self.__curr = int(self.__curr * 2 + 1)
            return self.tree[self.__curr]
        while True:
            if self.__curr % 2 == 1:
                self.__curr = self.__curr // 2
            else:
                self.__curr = self.__curr // 2 - 1
                if self.__curr % 2 == 0:
                    while self.__curr % 2 == 0 and self.__curr > 0:
                        self.__curr = self.__curr // 2 - 1
                    self.__curr = self.__curr // 2
                else:
                    self.__curr = self.__curr // 2
            if self.__curr == 0:
                if self.zero == True:
                    raise StopIteration()
                self.zero = True
            if self.__curr * 2 + 2 < self.length:
                self.__curr = self.__curr * 2  + 2
                return self.tree[self.__curr]


    def __iter__(self):
        return self


oak = BinTree()
#for i in range (29):
#    oak.add(i)
for i in oak:
    print(i)