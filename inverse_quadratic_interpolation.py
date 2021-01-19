from input_functions import *
from typing import Callable

def inverse_quadratic_interpolation_solver(f: Callable[[float], float],
                                           x0 : float,
                                           x1 : float,
                                           x2: float) -> float:
    def compute_next_step(f, x_n_2, x_n_1, x_n):
        return f(x_n_1) * f(x_n) * x_n_2 / ((f(x_n_2) - f(x_n_1)) * (f(x_n_2) - f(x_n))) + \
               f(x_n_2) * f(x_n) * x_n_1 / ((f(x_n_1) - f(x_n_2)) * (f(x_n_1) - f(x_n))) + \
               f(x_n_2) * f(x_n_1) * x_n / ((f(x_n) - f(x_n_2)) * (f(x_n) - f(x_n_1)))

    x = [x0, x1, x2]
    while abs(x[1] - x[2]) > eps():
        x_next = compute_next_step(f, x[0], x[1], x[2])
        x.pop(0)
        x.append(x_next)

    return x[2]
