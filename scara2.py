import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import *
from sympy import symbols, Matrix, simplify

theta1, L1, theta2, L2 = symbols('theta1 L1 theta2 L2')

T01 = trotz(theta1) @ transl(L1, 0,0)
print(f"primera transformación T01:\n{T01}\n")

T12 = trotz(theta2) @ transl(L2, 0,0)
print(f"segunda transformación T12:\n{T12}\n")

T02 = T01 @ T12
print(f"transformación total T02:\n{T02}\n")

M = Matrix(T02)

M_simplified = M.applyfunc(simplify)

def nice_print_matrix(matrix):
    return '\n'.join(['\t'.join([str(entry.evalf()) for entry in row]) for row in matrix.tolist()])

print(nice_print_matrix(M_simplified))
print('\n')

M_evaluated = M_simplified.subs({theta1: np.deg2rad(30), L1: 4, theta2: np.deg2rad(0), L2: 3}).evalf()
print(nice_print_matrix(M_evaluated))