from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from tqdm import tqdm


def plot_mandelbrot(lim=2, increment=0.01, rangeX=(-2, 0.5), rangeY=(-1, 1), set_iters=100):
  x_iters = np.arange(rangeX[0], rangeX[1], increment)
  y_iters = np.arange(rangeY[0], rangeY[1], increment)
  arr = np.zeros([len(y_iters), len(x_iters)], dtype=np.float32)
  print(arr.shape)
  for i, x in enumerate(x_iters):
    for j, y in enumerate(y_iters):
      iterations = in_set(x + y * 1j, set_iters, lim=lim)
      arr[j, i] = 1 - iterations/set_iters
  
  plt.imshow(arr, cmap='gray')
  plt.show()

def in_set(c, iterations=100, lim=2):
  c_re = np.real(c)
  c_im = np.imag(c)
  z_re = 0
  z_im = 0
  for i in range(iterations):
    new_z_re = z_re**2 - z_im**2 + c_re
    z_im = 2*z_re*z_im + c_im
    z_re = new_z_re

    if abs(z_re + z_im*1j) > lim:
      return i
  
  return i

def in_set_equilibrium_cts(c, iter_prev=100, iter_after=1000, lim=2, tolerance=0.01):
  c_re = np.real(c)
  c_im = np.imag(c)
  z_re = 0
  z_im = 0
  arr = []
  for i in range(iter_prev + iter_after):
    new_z_re = z_re**2 - z_im**2 + c_re
    z_im = 2*z_re*z_im + c_im
    z_re = new_z_re

    if abs(z_re + z_im*1j) > lim:
      return False

    if i == iter_prev - 1:
      arr = [z_re]
    elif i > iter_prev - 1:
      arr.append(z_re)
      deviation = abs(arr[0] - z_re)
      if deviation < tolerance:
        return arr[:i - iter_prev + 1]

  return arr


def plot_mandelbrot_x_iters(lim=2, increment=0.01, rangeX=(-2, 0.5), set_iters=100):
  x_iters = np.arange(rangeX[0], rangeX[1]+increment, increment)
  # arr = np.zeros([len(x_iters)], dtype=np.float64)
  print("{} iterations".format(len(x_iters)))
  arr_x = []
  arr_y = []
  for i, x in tqdm(enumerate(x_iters)):
    eq_cts = in_set_equilibrium_cts(x, set_iters, lim=lim)
    if not eq_cts: continue
    for const in eq_cts:
      arr_x.append(i)
      arr_y.append(const)
  
  # plt.imshow(arr, cmap='gray')
  plt.scatter(arr_x, arr_y, s=.5)
  plt.show()


def mandelbrot_3d(increment=0.05, rangeX=(-2, 0.5), rangeY=(-1, 1), set_iters=100, lim=2):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  x_iters = np.arange(rangeX[0], rangeX[1], increment)
  y_iters = np.arange(rangeY[0], rangeY[1], increment)
  arr = np.zeros([len(y_iters), len(x_iters)], dtype=np.float32)
  print(arr.shape)
  for i, x in enumerate(x_iters):
    for j, y in enumerate(y_iters):
      iterations = in_set(x + y * 1j, set_iters, lim=lim)
      arr[j, i] = 1 - iterations/set_iters

  y_axis = np.repeat(y_iters, len(x_iters))
  x_axis = np.repeat([x_iters], len(y_iters), 0).reshape(-1)
  ax.scatter(
    xs=x_axis,
    ys=y_axis,
    zs=0,
    c=[c for c in arr.reshape(-1)],
    cmap="gray")

  plt.show()


if __name__ == '__main__':
  # plot_mandelbrot_x_iters(increment=0.00005, set_iters=100)
  # plot_mandelbrot(increment=0.005)
  mandelbrot_3d()
  # print(in_set(0))