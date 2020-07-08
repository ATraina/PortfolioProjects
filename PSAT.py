import math

def Psat(T):
    x = T**(-1)
    y_1 = (-144381)*(x*x) + (-1702)*(x) + (8.704)
    y_2 = (-87709)*(x*x) + (-2040)*(x) + (9.093)
    y_3 = (-100774)*(x*x) + (-2084)*(x) + (9.221)
    y_4 = (-105808)*(x*x) + (-2182)*(x) + (9.278)
    psat_1 = math.exp(y_1)
    psat_2 = math.exp(y_2)
    psat_3 = math.exp(y_3)
    psat_4 = math.exp(y_4)
    return psat_1,psat_2,psat_3,psat_4
