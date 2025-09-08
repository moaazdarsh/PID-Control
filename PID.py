import numpy as np
import matplotlib.pyplot as plt

surrounding = -12 #Surrounding Temperature
T = -11 #Current Temperature
Tlog = [T] #Temperature Log

D = [] #Difference Log
DesiredT = 37 #Desired Temperature
K_p = 0.1
K_i = 0.01
K_d = 0.05
P, I, D = 0, 0, 0

t_end = 200
t = 0
while t < t_end:
    T += (surrounding - T) * 0.01 #Natural Cooling
    Tlog.append(T)

    D.append(DesiredT - T)
    
    P = K_p * D[-1] # The P term is proportional to the current error
    if len(D) > 1:
        I = K_i * np.trapezoid(D) # The I term is proportional to the integral of the error
        D = K_d * (D[-1] - D[-2]) # The D term is proportional to the derivative of the error
    
    T += P + I + D

    t += 1 

W, graph = plt.subplots()
graph.plot(Tlog)
graph.axhline(DesiredT, color='r', linestyle='--', label='Desired Temperature')
graph.set_title("PID Control Simulation")
graph.set_xlabel("Time")
graph.set_ylabel("Temperature (°C)")
plt.show()