import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(t, A, h, T, phi):
    return A*np.exp(-h*t)*np.sin(2*np.pi/T*t + phi)

t = np.array([1,2,3,4,5,6,7,8])
y = np.array([0.6,2.3,2.1,3.5,4.2,6.0,7.8,9.2])

popt, pcov = curve_fit(func, t, y, (1e3, 1e-2, 1., -1e1), maxfev=10**6)
A, h, T, phi = popt

print('A={0}\nh={1}\nT={2}\nphi={3}'.format(*tuple(popt)))

A=2.5799396598541523e+33
h=0.037592823141341276
T=1.0293760398048617
phi=348.9653603351754

plt.scatter(t, y, s=30, color='orange')
plt.plot(t, func(t, *popt))