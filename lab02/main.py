import sympy as sp
import graphics as gr
from typing import List, Tuple
from math import exp

# Потрібно побудувати графічно фазові траєкторії наступних задач:
# 1. є d2y(x)/dx2 + (1+x^2)dy(x)/dx - (x - 1/2)^2 y(x) = -(x^2+e^x)
#    x in (0, 1), y(0) = - 1, y(1) = 0, є = 1, 10, 0.00001, 0.1
# 2. є d2y(x)/dx2 + dy(x)/dx = 0
#    x in (0, 1), y(0) = 0, y(1) = 1, є = 1, 10, 0.00001, 0.1
# 3. -є d2y(x)/dx2 + dy(x)/dx = 0
#    x in (0, 1), y(0) = 1, y(1) = 1, є = 1, 10, 0,00001, 0.1
# 4. є d2y(x)/dx2 + 2x dy(x)/dx = 0
#    x in (-1, 1), y(-1) = -1, y(1) = 2, є = 1, 10, 0.00001, 0.1

if __name__ == '__main__':

    eps: List[float] = [1.0, 10.0, 0.00001, 0.1]
    x, y, q = sp.symbols('x y q')  # for reason instead of є there'll be q
    dy = sp.diff(y, x)
    ddy = sp.diff(dy, x)
    problems: List[Tuple[str, Tuple[float, float], Tuple[float, float]]] = [
        ('q*diff(diff(y, x), x) + (1 + x**2) * diff(y, x) - (x - 0.5)**2 * y = -(x**2 + exp(x))',
                                                                                             (0.0, 1.0),
                                                                                             (-1.0, 0.0)),
        ('q*diff(diff(y, x), x) + diff(y, x) = 0', (0.0, 1.0), (0.0, 1.0)),
        ('-q*diff(diff(y, x), x) + diff(y, x) = 0', (0.0, 1.0), (1.0, 1.0)),
        ('q*diff(diff(y, x), x) + 2*x*diff(y, x) = 0', (-1.0, 1.0), (-1.0, 2.0)),
    ]

    print((problems[0][0]))

    gr.draw_phase_trajectory()
