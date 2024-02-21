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

def compute_area(radius):
    return 4. * np.pi * radius**2

no_shield = len(read_neutrons("no_shield.txt")) / compute_area(0.001)

# water
water_5cm = len(read_neutrons("water/water_5cm.txt")) / compute_area(0.05)
water_10cm = len(read_neutrons("water/water_10cm.txt")) / compute_area(0.10)
water_15cm = len(read_neutrons("water/water_15cm.txt")) / compute_area(0.15)

depths = [0,5,10,15]
counts = [no_shield, water_5cm, water_10cm, water_15cm]

plt.figure()
plt.scatter(depths, counts)
plt.yscale("log")
plt.show()