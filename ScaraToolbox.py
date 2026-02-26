import sympy as sp
from sympy.matrices import rot_axis3
#para el ejemplo, generamos la matriz DH
from spatialmath import *
from spatialmath.base import *
#Para graficar
import matplotlib.pyplot as plt
import numpy as np
#para usar el DH
import roboticstoolbox as rtb

scara = rtb.DHRobot([
    rtb.RevoluteDH(d=0.160, a=0.350, alpha=0, qlim=[-2.58, 2.58]),
    rtb.RevoluteDH(d=0, a=0.300, alpha=0, qlim=[-2.61, 2.61]),
    rtb.PrismaticDH(theta=0, a=0.0, alpha=np.pi, offset=0.21, qlim=[-0.370, 0.0]),
    rtb.RevoluteDH(d=0.0, a=0, alpha=0, qlim=[-6.28, 6.28])
], name='SR-6iA', base=SE3(0, 0, 0))
print("Matriz de transformación homogénea del efector final respecto a la base (T06):")
print(scara)

joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = 0 - 0.21 #offset de 210 mm para el prismatico
joint4 = np.deg2rad(0)

# T04DH = scara.fkine([joint1, joint2, joint3, joint4])
# print("T04DH:")
# print(T04DH)

q = np.array([[0,0,0,0], [joint1, 0, 0, 0], [joint1, joint2, 0, 0], [joint1, joint2, joint3, 0], [joint1, joint2, joint3, joint4]])

scara.plot(q=q, backend='pyplot', dt=3, limits=[-1, 1, -1, 1, -0.4, 0.5], shadow=True, jointaxes=True, loop=False, movie='scara_animation.gif')