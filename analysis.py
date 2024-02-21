import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.optimize import curve_fit

rc('font', **{'family': 'serif', 'serif': ['computer modern']})
rc('text', usetex=True)

def read_neutrons(file):
    data = np.genfromtxt(file)
    energy=data[:,2]
    return energy

no_shield = len(read_neutrons("no_shield.txt"))

# water
water_5cm = len(read_neutrons("water/water_5cm.txt"))
water_10cm = len(read_neutrons("water/water_10cm.txt"))
water_15cm = len(read_neutrons("water/water_15cm.txt"))
water_20cm = len(read_neutrons("water/water_20cm.txt"))
water_25cm = len(read_neutrons("water/water_25cm.txt"))
water_30cm = len(read_neutrons("water/water_30cm.txt"))

depths = [0,5,10,15,20,25,30]
counts = [no_shield, water_5cm, water_10cm, water_15cm, water_20cm, water_25cm, water_30cm]

plt.figure()
plt.scatter(depths, counts)
#plt.yscale("log")
plt.xlim(-0.1,150)
plt.show()