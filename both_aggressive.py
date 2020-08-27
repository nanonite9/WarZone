import numpy as np
import scipy.integrate as integrate
import matplotlib.pylot as plt

# RK45 performed on arms race model
# each parameter is a function of one or both country's spending
# country A is aggressive, country B is aggressive

def model(t,z):
    x = z[0]
    y = z[1]

    b_x, b_y = 2.0, 2.8 # budget constraints
    c_x, c_y = (x/b_x), (y/b_y) # variable constraints
    f_x, f_y = (1.0+y/x), (2.0+y/x) # fear factor that impacts spending
    e_x, e_y = 1.0, 1.0 # external factors that impacts spending

    # defining ODEs
    dxdt = f_x*y - c_x*x + e_x
    dydt = f_y*x - c_y*y + e_y

    # returning array
    dzdt = np.array([dxdt, dydt])
    return dzdt

# initialize time and x and y expenditure at initial time
t_0 = 0
init_data = np.array([5, 5])

# starting RK45 integration method
sys_1 = integrate.RK45(model, t_0, init_data, 1000, 0.001)

# storing initial data 
sol_x = [sys_1.y[0]]
sol_y = [sys_1.y[1]]
time = [t_0]

for i in range(5000):
    sys_1.step() # performing integration step
    sol_x.append(sys_1.y[0]) # storing the results in our solution list, y is the attribute current state
    sol_y.append(sys_1.y[1])
    time.append(sys_1.t)

plt.figure(figsize=(20, 10))

# plotting results in a graph
plt.ylim(4, 10)
plt.plot(time, sol_x, 'b--', label='Country A (aggressive)')
plt.plot(time, sol_y, 'r--', label='Country B (aggressive)')
plt.ylabel('Military Expenditure (billions USD)', fontsize = 16)
plt.xlabel('Time (years)', fontsize = 16)
plt.legend(loc='best', fontsize = 22)
plt.title('Arms Race: Aggressive vs. Aggressive', fontsize = 28)
plt.show()