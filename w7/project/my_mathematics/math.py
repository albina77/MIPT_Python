import math
import cmath


class MyMath():
    _complex = False # инкапсуляция!
    pi = 3.14

    def sin(self, x):
        return math.sin(x)

    def sqrt(self, x):
        if (x < 0):
            if self._complex == False:
                raise ValueError("Нельзя! Мы работаем с действительными числами")
            else:
                return (cmath.sqrt(x).real, cmath.sqrt(x).imag)
        return math.sqrt(x) # здесь при self.complex == True подразумевается, что корень из отрицательного числа существует. => полиморфизм



class MyComplexMath(MyMath): # наследование! Изменяем значение переменной
    _complex = True # инкапсуляция!

'''

Мы используем классовый метод, а не статический, т.к. статические методы не знают, к какому классу они относятся. А в нашей задаче этот фактор решающий. Между созданными классами есть принципиальная разница, хоть и один является потомком другого.

'''





