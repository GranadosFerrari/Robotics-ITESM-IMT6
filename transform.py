import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import symbols, Matrix

# theta = symbols('theta')
# R = Matrix(rotz(theta))
# print(R)

theta_deg = 30
theta_rad = np.deg2rad(theta_deg)

# R = rot2(theta_rad)
# print(R)

# trplot2(R)
# plt.axis('equal')
# plt.grid()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Rotación 2D')
# plt.show()

T0 = transl2(0,0)
trplot2(T0, frame='0', color='k')

TA = transl2(1,2) @ trot2(30, "deg")
print(TA)
trplot2(TA, frame='A', color='b')

TB = trot2(30, "deg") @ transl2(1,2)
print(TB)
trplot2(TB, frame='B', color='r')

P = np.array([4,3])  # Punto en coordenadas homogéneas
plot_point(P, "ko", text="P")

P1 = homtrans(np.linalg.inv(TA), P)
print(P1)

plt.axis('equal')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Transformación Homogénea 2D')
plt.show()