import numpy as np
import matplotlib.pyplot as plt

time_1_thread = []
time_2_thread = []
time_4_thread = []
time_8_thread = []

prom_1_thread = sum(time_1_thread)/len(time_1_thread)
prom_2_thread = sum(time_2_thread)/len(time_2_thread)
prom_4_thread = sum(time_3_thread)/len(time_4_thread)
prom_8_thread = sum(time_4_thread)/len(time_8_thread)

print(prom_1_thread)
X = np.array([1, 2, 4, 8])
Y = np.array([
        prom_1_thread,
        prom_2_thread,
        prom_4_thread,
        prom_8_thread
    ])

plt.plot(X, Y)
plt.plot(X, Y)
plt.title('Rendimiento')
plt.ylabel('time (ms)')
plt.xlabel('thread')
plt.show()