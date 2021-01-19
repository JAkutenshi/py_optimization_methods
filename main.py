from input_functions import *
from interpolation import *
from inverse_quadratic_interpolation import inverse_quadratic_interpolation_solver


if __name__ == '__main__':
    interpolation = build_Lagrange_interpolation(discrete_fun_table())
    test = {}
    for xi in discrete_fun_table():
        test[xi] = interpolation(xi)
    print(test)
    print(interpolation(0.3))

    print(inverse_quadratic_interpolation_solver(lambda x: 3*x**4-5*x**3+2*x**2-x-1, -5, 0, 5))
