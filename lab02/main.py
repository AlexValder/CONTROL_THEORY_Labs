#!/bin/python3

import sympy as sp
import graphics as gr
from typing import List, Tuple, Set

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

    x = sp.Symbol('x')
    f = sp.Function('f')
    df = sp.diff(f, x)
    ddf = sp.diff(df, x)

    eq = sp.dsolve(sp.Eq(ddf(x) + (1 + x**2)*df(x) - (x - 0.5)**2 * f(x), -x**2 - sp.exp(x)), f, ics={f(0): -1, f(1): 0})
    p = sp.plot(eq, show=False)
    p.show()

#    plots: List = [sp.plot(problem, (x, 0.0, 1.0), show=False) for problem in problems]

    # plots[0].extend(plots[1])
    # plots[0].extend(plots[2])
    # plots[0].extend(plots[3])

#    plots[0].show()
