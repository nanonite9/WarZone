import numpy as np
import scipy.integrate as integrate
import matplotlib.pylot as plt

# RK45 performed on arms race model
# country A is passive, country B is aggressive

def model(t,z):
    x = z[0]
    y = z[1]

    c_x, c_y = 0.8, 1.0 # spending constraints
    f_x, f_y = 1.2, 0.8 # fear factor that impacts spending
    e_x, e_y = 0.8, 0.7 # external factors that impacts spending

    # defining ODEs
    dxdt = f_x*y - c_x*x + e_x
    dydt = f_y*x - c_y*y + e_y

    # returning array
    dzdt = np.array([dxdt, dydt])
    return dzdt

# initialize time and x and y expenditure at initial time
t_0 = 0
init_data = np.array([14, 5])

# starting RK45 integration method
system1 = integrate.RK45(model, t_0, init_data, 1000, 0.001)

# storing initial data 
solnX = [system1.y[0]]
solnY = [system1.y[1]]
time = [t_0]

for i in range(5000):
    system1.step() # performing integration step
    solnX.append(system1.y[0]) # storing the results in our solution list, y is the attribute current state
    solnY.append(system1.y[1])
    time.append(system1.t)

plt.figure(figsize=(20, 10))

# plotting results in a graph
plt.plot(time, solnX, 'b--', label='Country A')
plt.plot(time, solnY, 'r--', label='Country B')
plt.ylabel('Military Expenditure (billions USD)', fontsize = 16)
plt.xlabel('Time (years)', fontsize = 16)
plt.legend(loc='best', fontsize = 22)
plt.title('Simple Arms Race: Aggressive vs. Passive', fontsize = 28)
plt.show()