from matplotlib import pyplot as plt
from tqdm import tqdm


# Calculate the equilibrium constant
def equilibrium(r, x, iterations=100):
  ans = x
  for _ in range(iterations):
    ans = r * ans * (1 - ans)

  return ans

# Calculate the equilibrium constant(s) (even if there are several)
def equilibrium_cts(r, x, iter_prev=1000, iter_after=1000, tolerance=0.01):
  ans = equilibrium(r, x, iter_prev)
  arr = [ans]
  for i in range(iter_after):
    ans = r * ans * (1 - ans)
    arr.append(ans)
    deviation = abs(arr[0] - ans)
    if deviation < tolerance:
      return arr[:i+1]
  
  return arr

# Plot equilibrium function
def plot_equilibrium(r, x, iterations=100):
  ans = x
  arr = [ans]
  for _ in range(iterations):
    ans = r * ans * (1 - ans)
    arr.append(ans)

  plt.plot(arr)
  print(arr)
  plt.ylim(0, 1)
  plt.xlim(0, iterations)
  plt.show()

def plot_chaos(r, iterations, iter_prev=1000, iter_after=2000, tolerance=0.001):
  increment = 4. / iterations
  arr_x = []
  arr_y = []
  for i in tqdm(range(iterations)):
    eq_cts = equilibrium_cts(r, .4, iter_prev=iter_prev, iter_after=iter_after, tolerance=tolerance)

    for const in eq_cts:
      arr_x.append(r)
      arr_y.append(const)
    
    r += increment
  
  plt.scatter(arr_x, arr_y, s=.5)
  plt.ylim(0, 1)
  plt.show()


if __name__ == '__main__':
  # print(equilibrium_cts(3.1, .4))
  # plot_equilibrium(3.1, .4)
  plot_chaos(0, 50000)