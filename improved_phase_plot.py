from pylab import *
import matplotlib.pylot as plt

# budget, fear factor and external factor constraints
b_x, b_y = 2.0, 5.0
c_x, c_y = (x/b_x), (y/b_y) # variable constraints
f_x, f_y = (1.0+y/x), (1.0-y/x)
e_x, e_y = 0.7, 0.7

x, y = meshgrid(arrange(0, 7, 0.1), arrange(0, 7, 0.1))
xdot = f_x*y - c_x*x + e_x
ydot = f_y*x - c_y*y + e_y

plt.figure(figsize=(10, 10))
plt.title('Phase Plot: Aggressive vs. Passive', fontsize = 28)
streamplot(x, y, xdot, ydot)

show()