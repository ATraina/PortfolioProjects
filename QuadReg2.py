import numpy as np
import math

T = [140,160,180,200,220,240,260,270,300,320,340,360,380,400]
P = [4.80e-5,8.20e-4,7.00e-3,3.69e-2,0.1374,0.3989,0.9600,1.4081,3.705,6.33,10.14,15.43,22.55,31.93]

f = lambda x: x**(-1)
g = lambda x: math.log(x)

s = lambda x: x**2
c = lambda x: x**3
q = lambda x: x**4

X = np.array(list(map(f,T)))
Xs = np.array(list(map(s,X)))
Xc = np.array(list(map(c,X)))
Xq = np.array(list(map(q,X)))
Y = np.array(list(map(g,P)))

Sx_0 = len(X)
Sx_1 = sum(X)
Sx_2 = sum(Xs)
Sx_3 = sum(Xc)
Sx_4 = sum(Xq)
Sy = sum(Y)
Syx_1 = Y @ X
Syx_2 = Y @ Xs

M = np.array([[Sx_4,Sx_3,Sx_2],[Sx_3,Sx_2,Sx_1],[Sx_2,Sx_1,Sx_0]])
Minv = np.linalg.inv(M)
d = np.array([[Syx_2],[Syx_1],[Sy]])

z = Minv @ d
A = z[0][0]
B = z[1][0]
C = z[2][0]

print(A,B,C)
