from pylab import *
import matplotlib.pylot as plt

# budget, fear factor and external factor constraints
b_x, b_y = 2.0, 2.8
c_x, c_y = (x/b_x), (y/b_y)
f_x, f_y = (1.0+y/x), (2.0+y/x)
e_x, e_y = 1.0, 1.0

x, y = meshgrid(arrange(0, 13, 0.1), arrange(0, 13, 0.1))
xdot = f_x*y - c_x*x + e_x
ydot = f_y*x - c_y*y + e_y

plt.figure(figsize=(10, 10))
plt.title('Phase Plot: Aggressive vs. Aggressive', fontsize = 28)
streamplot(x, y, xdot, ydot)

show()