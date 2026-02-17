import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import symbols, Matrix

T0 = transl2(0,0)
trplot2(T0, frame='0', color='k')

#rotación seguida de traslación respecto a A T0
TA = trot2(45, "deg")
trplot2(TA, frame='A', color='b')
plot_circle(4, (0,0), 'b--')

TBA = TA @ transl2(4,0) @ trot2(60, "deg")
trplot2(TBA, frame='B', color='g')
origin_TBA = TBA[:2, 2]
plot_circle(3, (origin_TBA[0], origin_TBA[1]), 'g--')

TCBA = TBA @ transl2(3,0)
trplot2(TCBA, frame='C', color='r')
print(TCBA)

origin_TCBA = TCBA[:2, 2]
P = np.array([origin_TCBA[0], origin_TCBA[1]])  # Punto en coordenadas homogéneas
plot_point(P, "ko", text="P")
print("Coordenadas de P en T0:", P)

plt.axis('equal')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('gráfica de workspace de un SCARA')
plt.show()