import numpy as np
import math

T = [140,160,180,200,220,230,240,250,270,280,320,360,380,400,420]
P = [8.30e-6,2.00e-4,2.19e-3,1.38e-2,5.95e-2,0.1105,1.93e-1,0.3209,0.7766,1.14,4.1,10.8,16.3,23.6,33.14]

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
