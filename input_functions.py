def continuous_multivariable_fun(x: list[float]) -> float:
    return 2 * x[0]**2 + 2


def continuous_multivariable_fun_derivative(x: list[float]) -> float:
    return 4 * x[0]


def continuous_fun(x: float) -> float:
    return 2 * x**2 + 2


def continuous_fun_derivative(x: float) -> float:
    return 4 * x


def discrete_fun_table() -> dict[float, float]:
    var_table = {
        -1.5: -14.1014,
        -0.75: -0.931596,
        0.0: 0.0,
        0.75: 0.931596,
        1.5: 14.1014
    }
    return var_table


def discrete_fun(args: list):
    x = args[0]
    return discrete_fun_table()[x]


def eps() -> float:
    return 1e-9
