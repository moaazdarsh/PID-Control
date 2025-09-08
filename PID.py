import numpy as np
import matplotlib.pyplot as plt

surroundings = -12
T = -11
Tlog = [T]

E = []
DesiredT = 37
K_p = 0.1
K_i = 0.01
K_d = 0.05
P, I, D = 0, 0, 0

t_end = 200
t = 0
while t < t_end:
    T += (surroundings - T) * 0.01
    Tlog.append(T)

    E.append(DesiredT - T)
    
    P = K_p * E[-1]
    if len(E) > 1:
        I = K_i * np.trapezoid(E)
        D = K_d * (E[-1] - E[-2])
    
    T += P + I + D

    t += 1 

W, graph = plt.subplots()
graph.plot(Tlog)
graph.axhline(DesiredT, color='r', linestyle='--', label='Desired Temperature')
graph.set_title("PID Control Simulation")
graph.set_xlabel("Time")
graph.set_ylabel("Temperature (°C)")
plt.show()