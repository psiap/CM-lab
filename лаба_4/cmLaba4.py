from scipy import integrate
from math import *

func = lambda x: pow(e,x) + tan(x)

answer = integrate.quad(func, 0, pi)
print(answer)