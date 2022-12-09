""" Cubic Spline Interpolation """

import numpy as np
from matplotlib import pyplot as plt
from piecewise import Function
from datas import Datas


def find_tertiary(x0, x1, y0, y1, dy0, dy1):
    coeff = np.matrix([
        [1, x0, x0**2, x0**3],
        [0, 1,  2*x0,  3*(x0**2)],
        [1, x1, x1**2, x1**3],
        [0, 1,  2*x1,  3*(x1**2)]
    ])

    const = np.matrix([
        [y0],
        [dy0],
        [y1],
        [dy1]
    ])

    return (np.linalg.inv(coeff) * const).transpose().tolist()[0][::-1]


def simple_spline(data: Datas) -> Function:
    result = Function()
    n = data.len()

    for i in range(n-1):
        coeff = np.matrix([
            [data.x[i], 1],
            [data.x[i+1], 1]
        ])

        const = np.matrix([
            [data.y[i]],
            [data.y[i+1]]
        ])

        result.data.append((data.x[i], data.x[i+1], 
            np.poly1d((np.linalg.inv(coeff)*const).transpose().tolist()[0]))
        )

    return result


def monotone_cubic_spline(data: Datas) -> Function:
    result = Function()
    n = data.len()

    delta = [(data.y[i+1] - data.y[i]) / (data.x[i+1] - data.x[i]) for i in range(n-1)]
    delta.append(delta[-1])
    m = [(delta[i+1] + delta[i]) / 2 for i in range(n-2)]
    
    for i in range(1, n-1):
        delta[i] = m[i-1]

    for i in range(n-1):
        result.data.append((data.x[i], data.x[i+1], np.poly1d(find_tertiary(
            data.x[i], data.x[i+1], data.y[i], data.y[i+1], delta[i], delta[i+1]
        ))))
    
    return result


def polynomial_spline(data: Datas) -> Function:
    n = data.len()

    coeff = np.matrix([
        [
            data.x[j]**(n-i-1) for i in range(n)
        ] for j in range(n)
    ])

    const = np.matrix(data.y).transpose()

    result = Function()

    result.data.append((
        data.x[0], data.x[-1], np.poly1d(
            (np.linalg.inv(coeff) * const).transpose().tolist()[0]
        )
    ))

    return result
