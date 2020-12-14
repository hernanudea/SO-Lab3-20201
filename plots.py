import numpy as np
import matplotlib.pyplot as plt

#p, i, s = 1000000, 1000, 1
#time_1_thread = [4381.376, 4419.389, 4454.744,  4432.020, 4426.351, 4383.399, 4485.386, 4482.734, 4504.200, 4442.614 ]
#time_2_thread = [2377.642, 2382.870, 2369.016, 2395.645, 2366.142, 2361.959, 2378.567, 2378.033, 2532.676, 2489.959]
#time_4_thread = [2211.693, 2208.533, 2205.870, 2236.260, 2206.899, 2224.007, 2219.321, 2243.976, 2254.706, 2330.645]
#time_8_thread = [2435.449, 2429.286, 2425.925, 2457.193, 2454.506, 2496.416, 2478.696, 2459.691, 2463.381, 2453.902]

p, i, s = 10000000, 1000, 1
time_1_thread = [43049.476, 42705.792, 42717.520, 42542.677, 45285.559, 42791.156, 42938.359, 43464.595, 42690.705, 42820.573]
time_2_thread = [23794.853, 22865.851, 22908.587, 24510.835, 26170.937, 23685.125, 24913.082, 26514.446, 31089.880, 23355.480]
time_4_thread = [24296.087, 22596.397, 22821.097, 21481.434, 23444.086, 21845.145, 32296.622, 22704.262, 21932.873, 22543.631]
time_8_thread = [25622.047, 25083.279, 24979.656, 24864.517, 24455.713, 24977.938, 23786.691, 22448.258, 23141.270, 25119.681]

time_seqential = [48924.750, 49964.114, 49600.533, 52482.922, 52408.334, 52545.296, 51876.559, 52567.154, 52927.057, 50223.278]
avg_sequential = sum(time_seqential)/len(time_seqential)



prom_1_thread = sum(time_1_thread)/len(time_1_thread)
prom_2_thread = sum(time_2_thread)/len(time_2_thread)
prom_4_thread = sum(time_4_thread)/len(time_4_thread)
prom_8_thread = sum(time_8_thread)/len(time_8_thread)

X = np.array([1, 2, 4, 8])
Y = np.array([
    prom_1_thread,
    prom_2_thread,
    prom_4_thread,
    prom_8_thread
])

Y_speedup = Y/avg_sequential

#Y_sequential = np.array([])

# plt.plot(X, Y, label='p='.format(p))
# plt.title('SAXPY Paralelo\np = {}, s = {}, s = {}'.format(p, i, s), c='b')
# plt.ylabel('time (ms)', c='b')
plt.plot(X, Y_speedup, label='speedup')
plt.title('Speedup', c='b')
plt.xlabel('num thread', c='b')
plt.ylabel('SpeedUp', c='b')
plt.legend()
plt.savefig('plot_speedup.png'.format(p, i, s), dpi=600)
plt.show()
