import pytest
import random
import numpy as np
from my_mathematics.linear_algebra import Vector


@pytest.fixture()
def n1():
    n1 = []
    for i in range (100):
        a1, b1, c1 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        n1.append(np.array([a1, b1, c1]))
    return n1

@pytest.fixture()
def v1(n1):
    v1 = []
    for i in range (100):
        v1.append(Vector(n1[i][0], n1[i][1], n1[i][2]))
    return v1

@pytest.fixture()
def n2():
    n2 = []
    for i in range (100):
        a2, b2, c2 = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        n2.append(np.array([a2, b2, c2]))
    return n2


@pytest.fixture()
def v2(n2):
    v2 = []
    for i in range (100):
        v2.append(Vector(n2[i][0], n2[i][1], n2[i][2]))
    return v2
