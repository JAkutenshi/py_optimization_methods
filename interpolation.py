from typing import Callable


def build_Lagrange_interpolation(table: dict[float, float]) -> Callable[[float], float]:
    def interpolation(x : float) -> float:
        def monominal(table : dict[float, float], xi: float, x: float) -> float:
            xes = list(table.keys())
            xes.remove(xi)
            result = 1.0
            for xj in xes:
                numerator = (x - xj)
                denominator = (xi - xj)
                coeff =  numerator / denominator
                result *= coeff
            return result

        interpolation_result = 0
        for xi in table.keys():
            interpolation_result += table[xi] * monominal(table, xi, x)
        return interpolation_result

    return interpolation
