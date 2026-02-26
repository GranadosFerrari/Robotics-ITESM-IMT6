import sympy as sp
from sympy.matrices import rot_axis3
#Para graficar
import matplotlib.pyplot as plt
import numpy as np
from spatialmath import *
from spatialmath.base import *

#definir simbolos
theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

# #matriz RzTzTxRx
# TDH = trotz(theta) @ transl(0, 0, d) @ transl(a, 0, 0) @ trotx(alpha)
# sp.pprint(TDH)
# print(type(TDH))

T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(alpha)*sp.sin(theta), a*sp.cos(theta)],
    [sp.sin(theta), sp.cos(alpha)*sp.cos(theta), -sp.sin(alpha)*sp.cos(theta), a*sp.sin(theta)],
    [0, sp.sin(alpha), sp.cos(alpha), d],
    [0, 0, 0, 1]
])
sp.pprint(T)
print(type(T))

theta_1, theta_2, theta_3, theta_4 = sp.symbols('theta_1, theta_2, theta_3, theta_4')
T01 = T.subs({d:0.160, a:0.350, alpha: 0})
T01 = T01.subs(theta, theta_1)
print("T01:")
sp.pprint(T01)

T12 = T.subs({d:0, a:0.300, alpha: 0}) #theta2 -sp.pi/2
T12 = T12.subs(theta, theta_2)
print("T12:")
sp.pprint(T12)

T23 = T.subs({d:0, a:0.0, alpha: sp.pi}) #theta3 + sp.pi/2
T23 = T23.subs(theta, theta_3)
print("T23:")
sp.pprint(T23)

T34 = T.subs({d:0.0, a:0, alpha: 0}) #theta4
T34 = T34.subs(theta, theta_4)
print("T34:")
sp.pprint(T34)

# imprimir la matrizota
# print("T06_s:")
# sp.pprint(T06_s)

#EJEMPLO Y VALUACION RAPIDA
#para modificar los ángulos cómodamente
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = 0
joint4 = np.deg2rad(0)

#  T04_solved = T04_s.subs({theta_1: joint1, theta_2: joint2, d_3: joint3, theta_4: joint4})
# print("T06_solved:")
# sp.pprint(T06_solved)  

T0 = rotz(0, unit='deg')
trplot(T0, len=0.7, frame='0', color='k')

T01_n = T01.subs(theta_1, joint1)
T01_n = np.array(T01_n).astype(np.float64)
trplot(T01_n, len=0.7, frame='1', color='b')

T12_n = T12.subs(theta_2, joint2)
T02_n = T01_n @ T12_n
T02_n = np.array(T02_n).astype(np.float64)
trplot(T02_n, len=0.7, frame='2', color='r')

T23_n = T23.subs(theta_3, joint3)
T03_n = T02_n @ T23_n
T03_n = np.array(T03_n).astype(np.float64)
trplot(T03_n, len=0.7, frame='3', color='g')

T34_n = T34.subs(theta_4, joint4)
T04_n = T03_n @ T34_n
T04_n = np.array(T04_n).astype(np.float64)
trplot(T04_n, len=0.7, frame='4', color='m')

plt.grid(True)
plt.title('Brazo SCARA SR-6iA')
plt.axis('equal')
plt.show()