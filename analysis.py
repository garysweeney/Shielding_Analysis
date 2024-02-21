import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['computer modern']})
rc('text', usetex=True)

def read_neutrons(file):
    data = np.genfromtxt(file)
    energy=data[:,2]
    return energy

def integrate_spectrum(file):
    flux = read_neutrons(file)
    return(len(flux))

no_shield = integrate_spectrum("no_shield.txt")

# water
water = [no_shield]
for i in range(1,21):
    water.append(integrate_spectrum("water/water_{}cm.txt".format(i*5)))

depth = np.linspace(0, 150, 31)

plt.figure()
plt.scatter(depth[:len(water)], water)
#plt.yscale("log")
#plt.xscale("log")
plt.xlim(-0.1,100)
plt.show()