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

theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols('theta_1, theta_2, theta_3, theta_4, theta_5, theta_6')
T01 = T.subs({d:0.680, a:0.2, alpha: -sp.pi/2})
T01 = T01.subs(theta, theta_1)
print("T01:")
sp.pprint(T01)

T12 = T.subs({d:0, a:0.89, alpha: 0}) #theta2 -sp.pi/2
T12 = T12.subs(theta, theta_2)
print("T12:")
sp.pprint(T12)

T23 = T.subs({d:0, a:0.15, alpha: -sp.pi/2}) #theta3 + sp.pi/2
T23 = T23.subs(theta, theta_3)
print("T23:")
sp.pprint(T23)

T34 = T.subs({d:0.88, a:0, alpha: sp.pi/2}) #theta4
T34 = T34.subs(theta, theta_4)
print("T34:")
sp.pprint(T34)

T45 = T.subs({d:0, a:0, alpha: -sp.pi/2}) #theta5
T45 = T45.subs(theta, theta_5)
sp.pprint(T45)

T56 = T.subs({d:0.14, a:0, alpha: 0}) #theta6
T56 = T56.subs(theta, theta_6)
print("T56:")
sp.pprint(T56)

T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
T06_s = T06.applyfunc(sp.simplify)
# imprimir la matrizota
# print("T06_s:")
# sp.pprint(T06_s)

#EJEMPLO Y VALUACION RAPIDA
#para modificar los ángulos cómodamente
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(30) - sp.pi/2 #offset de -90 grados para theta2
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T06_solved = T06_s.subs({theta_1: joint1, theta_2: joint2, theta_3: joint3, theta_4: joint4, theta_5: joint5, theta_6: joint6})
print("T06_solved:")
sp.pprint(T06_solved)   

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

T45_n = T45.subs(theta_5, joint5)
T05_n = T04_n @ T45_n
T05_n = np.array(T05_n).astype(np.float64)
trplot(T05_n, len=0.7, frame='5', color='y')

T56_n = T56.subs(theta_6, joint6)
T06_n = T05_n @ T56_n
T06_n = np.array(T06_n).astype(np.float64)
trplot(T06_n, len=0.7, frame='6', color='c')

T06_n = np.array(T06_solved).astype(np.float64)
trplot(T06_n, len=0.7, frame='6', color='c')

plt.grid(True)
plt.title('Brazo iRB4400 ABB')
plt.axis('equal')
plt.show()