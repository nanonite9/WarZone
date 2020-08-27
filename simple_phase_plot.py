from pylab import *
import matplotlib.pylot as plt

# spending, fear factor and external factor constraints
c_x, c_y = 0.8, 1.0
f_x, f_y = 1.2, 0.8
e_x, e_y = 0.8, 0.7

x, y = meshgrid(arrange(0, 7, 0.1), arrange(0, 7, 0.1))
xdot = f_x*y - c_x*x + e_x
ydot = f_y*x - c_y*y + e_y

plt.figure(figsize=(10, 10))
plt.title('Simple Phase Plot: Aggressive vs. Passive', fontsize = 28)
streamplot(x, y, xdot, ydot)

show()