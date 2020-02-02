from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm


def plot_mandelbrot(lim=2, increment=0.01, rangeX=(-2, 0.5), rangeY=(-1, 1), set_iters=100):
  # x_iters = round((rangeX[1] - rangeX[0]) / increment)
  # y_iters = round((rangeY[1] - rangeY[0]) / increment)
  x_iters = np.arange(rangeX[0], rangeX[1]+increment, increment)
  y_iters = np.arange(rangeY[0], rangeY[1]+increment, increment)
  arr = np.zeros([len(y_iters), len(x_iters)], dtype=np.float32)
  print(arr.shape)
  for i, x in enumerate(x_iters):
    for j, y in enumerate(y_iters):
      iterations = in_set(x + y * 1j, set_iters, lim=lim)
      # if iterations == set_iters-1:
      #   arr[j, i] = 0
      # else:
      #   arr[j, i] = 1
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

def in_set_value(c, iterations=100, lim=2):
  c_re = np.real(c)
  c_im = np.imag(c)
  z_re = 0
  z_im = 0
  for i in range(iterations):
    new_z_re = z_re**2 - z_im**2 + c_re
    z_im = 2*z_re*z_im + c_im
    z_re = new_z_re

    if abs(z_re + z_im*1j) > lim:
      return False
  
  return z_re


def plot_mandelbrot_x_iters(lim=2, increment=0.01, rangeX=(-2, 0.5), set_iters=100):
  x_iters = np.arange(rangeX[0], rangeX[1]+increment, increment)
  # arr = np.zeros([len(x_iters)], dtype=np.float64)
  print("{} iterations".format(len(x_iters)))
  arr = []
  for i, x in tqdm(enumerate(x_iters)):
    value = in_set_value(x, set_iters, lim=lim)
    if not value: continue
    # arr[i] = iterations
    arr.append(value)
  
  # plt.imshow(arr, cmap='gray')
  plt.scatter(list(range(len(arr))), arr, s=.5)
  plt.show()


if __name__ == '__main__':
  plot_mandelbrot_x_iters(increment=0.00005, set_iters=100)
  # plot_mandelbrot(increment=0.005)
  # print(in_set(0))