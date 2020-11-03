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


def test_for_vector_add(n1, v1, n2, v2):
    for n1_, n2_, v1_, v2_ in zip(n1, n2, v1, v2):
        n = n1_+n2_
        assert Vector(n[0], n[1], n[2]) == v1_ + v2_

def test_for_vector_neg(n1, v1):
    for n, v in zip(n1, v1):
        n_ = -n
        assert -v == Vector(n_[0], n_[1], n_[2])

def test_for_vector_mul(n1, v1):
    for n1_, v1_ in zip(n1, v1):
        n = random.randint(1, 10000)
        n2 = n1_ * n
        v2 = v1_ * n
        assert Vector(n2[0], n2[1], n2[2]) == v2

def test_for_vector_eq(n1, v1):
    for n1_, n2_, v1_, v2_ in zip(n1, n1, v1, v1):
        a = n1_ == n2_
        assert a.any() == (v1_ == v2_)

def test_for_vector_and(n1, v1, n2, v2):
    for n1_, n2_, v1_, v2_ in zip(n1, n2, v1, v2):
        if n2_[0] != 0:
            if n1_[0] / n2_[0] * n2_[1] == n1_[1] and n1_[0] / n2_[0] * n2_[2] == n1_[2]:
                assert 0 == v1_ & v2_
        elif n2_[1] != 0:
            if n1_[1] / n2_[1] * n2_[0] == n1_[0] and n1_[1] / n2_[1] * n2_[2] == n1_[2]:
                assert 0 == v1_ & v2_
        elif n2_[2] != 0:
            if n1_[2] / n2_[2] * n2_[0] == n1_[0] and n1_[2] / n2_[2] * n2_[1] == n1_[1]:
                assert 0 == v1_ & v2_
        elif n1_[0] == 0 and n1_[1] == 0 and n1_[2] == 0:
            assert 0 == v1_ & v2_
        else:
            assert Vector(n1_[1]*n2_[2] - n2_[1]*n1_[2], n1_[2]*n2_[0] - n1_[0]*n2_[2], n1_[0]*n2_[1] - n1_[1]*n2_[0]) == v1_ & v2_

'''
def test_for_vector_length(n1, v1):
    for n1_, v1_ in zip(n1, v1):
        a = (n1_[0]**2 + n1_[1]**2 + n1[2]**2)**0.5
        assert a == v1_.length()
'''

def test_for_vector_sub(n1, n2, v1, v2):
    for n1_, n2_, v1_, v2_ in zip(n1, n2, v1, v2):
        n = n1_ - n2_
        assert Vector(n[0], n[1], n[2]) == v1_ - v2_

def test_for_vector_str(n1, v1):
    for n1_, v1_ in zip(n1, v1):
        assert '({0}, {1}, {2})'.format(str(n1_[0]), str(n1_[1]), str(n1_[2])) == str(v1_)