from my_mathematics.math import MyMath, MyComplexMath
from my_mathematics.linear_algebra import Vector
import math, cmath
import numpy as np
import random

def test_for_sin():
    k = 0
    while k <= 1:
        a = MyMath()
        assert MyMath.sin(a, k) == math.sin(k)
        k += 0.1

def test_for_sqrt():
    list1 = [x for x in range(100)]
    list2 = [x**2 for x in range(100)]
    a = MyMath()
    for x in range (100):
        assert list1[x] == MyMath.sqrt(a, list2[x])


def test_for_complexsqrt():
    list2 = [x**2 for x in range(1, 100)]
    b = MyComplexMath()
    for x in range (99):
        tmp2 = -list2[x]
        assert (cmath.sqrt(tmp2).real, cmath.sqrt(tmp2).imag) == MyComplexMath.sqrt(b, tmp2)


def test_for_vector_add():
    for i in range (100):
        a1, b1, c1 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        a2, b2, c2 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        n1 = np.array([a1, b1, c1])
        v1 = Vector(a1, b1, c1)
        n2 = np.array([a2, b2, c2])
        v2 = Vector(a2, b2, c2)
        n = n1+n2
        assert Vector(n[0], n[1], n[2]) == v1 + v2

def test_for_vector_neg():
    for i in range (100):
        a1, b1, c1 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        n1 = np.array([a1, b1, c1])
        v1 = Vector(a1, b1, c1)
        n = -n1
        assert -v1 == Vector(n[0], n[1], n[2])

def test_for_vector_mul():
    for i in range (100):
        a1, b1, c1 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        n1 = np.array([a1, b1, c1])
        v1 = Vector(a1, b1, c1)
        n = random.randint(1, 10000)
        n2 = n1 * n
        v2 = v1 * n
        assert Vector(n2[0], n2[1], n2[2]) == v2

def test_for_vector_eq():
    for i in range (100):
        a1, b1, c1 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        n1 = np.array([a1, b1, c1])
        v1 = Vector(a1, b1, c1)
        n2 = np.array([a1, b1, c1])
        v2 = Vector(a1, b1, c1)
        a = n1 == n2
        assert a.any() == (v1 == v2)

