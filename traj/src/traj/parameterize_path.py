from sympy import Matrix, Piecewise, Symbol

from piecewise_function import PiecewiseFunction

def parameterize_path(path):
    """
    Represent the given joint-space path as a function q = f(s).

    To make this useful as a first step to creating smooth trajectories, we consruct the
    parameterization such that it has a few important properties:

    1. s = 0 is the start point of the path in joint space.
    2. As s increases, we move along the path monononically.
    3. The length of path traversed for a given increase in s is constant.

    Out of convenience, we choose a parameterization such that the value of s is equal
    to the length of path travesed. This "length" is in N-dimensional joint space, but
    otherwise is the same as we would compute a path length.

    """
    s = Symbol('s')
    boundaries = [0.0]
    functions = []
    for q0, q1 in zip(path[:-1], path[1:]):
        q0 = Matrix(q0)
        q1 = Matrix(q1)
        s0 = boundaries[-1]
        length = (q1 - q0).norm()
        s1 = s0 + length
        direction = (q1 - q0) / length
        boundaries.append(float(s1))
        functions.append(q0 + direction * (s - s0))
    return PiecewiseFunction(boundaries, functions, s)
