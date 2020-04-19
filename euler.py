# arguments: initial conditions, ending condition, number of steps, return value

import numpy as np

def euler(x0, y0, xf, n, z):

  dx = (xf - x0)/(n - 1)

  x = np.linspace(x0, xf, n)

  y = np.zeros([n])

  y[0] = y0

  for i in range(1, n):
    y[i] = dx * (x[i - 1] ** x[i - 1]) + y[i - 1]

  return x[z], y[z]

euler(0, 1, 10, 101, 12)