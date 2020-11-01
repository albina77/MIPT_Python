class Vector:
    __x = None
    __y = None
    __z = None

    def __init__(self, a, b, c = 0):
        self.__x = a
        self.__y = b
        self.__z = c


    def __str__(self):
        return '('+str(self.__x)+', '+str(self.__y)+', '+str(self.__z)+')'

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __neg__(self):
        return Vector(-self.__x, -self.__y, -self.__z)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Vector(self.__x * other, self.__y * other, self.__z * other)

    def __eq__(self, other):
        if (self.__x == other.__x) and (self.__y == other.__y) and (self.__z == other.__z): # как я поняла, все наши векторы имеют начало в нуле
            return True
        return False

    def __and__(self, other):
        if other.__x != 0:
            if self.__x / other.__x * other.__y == self.__y and self.__x / other.__x * other.__z == self.__z:
                return 0
        elif other.__y != 0:
            if self.__y / other.__y * other.__x == self.__x and self.__y / other.__y * other.__z == self.__z:
                return 0
        elif other.__z != 0:
            if self.__z / other.__z * other.__x == self.__x and self.__z / other.__z * other.__y == self.__y:
                return 0
        elif self.__x == 0 and self.__z == 0 and self.__y == 0:
            return 0
        return Vector(self.__y * other.__z - self.__z * other.__y, self.__z * other.__x - self.__x * other.__z,
                          self.__x * other.__y - self.__y * other.__x)

    def length(self):
        return (self.__x**2 + self.__y**2 + self.__z**2)**0.5

'''

N = int(input())
max = 0
maxV = None
for i in range(N):
    array = [int(x) for x in input().split()]
    vec = Vector(array[0], array[1], array[2])
    if vec.length() > max:
        max = vec.length()
        maxV = vec
print('The most remote point: '+str(maxV))

'''
