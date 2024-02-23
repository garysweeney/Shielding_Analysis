import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.optimize import curve_fit
from computed_livetime import compute_livetime

rc('font', **{'family': 'serif', 'serif': ['computer modern']})
rc('text', usetex=True)

nEvents = 1e6
livetime = compute_livetime(nEvents)

def read_neutrons(file):
    data = np.genfromtxt(file)
    energy=data[:,2]
    return energy

def integrate_spectrum(file):
    flux = read_neutrons(file)
    return(len(flux))

no_shield = integrate_spectrum("no_shield.txt")

HDPE = [no_shield]
water = [no_shield]
borated_water = [no_shield]

for i in range(1,21):
    water.append(integrate_spectrum("water/water_{}cm.txt".format(i*5)))

for i in range(1,20):
    borated_water.append(integrate_spectrum("borated_water/borated_water_{}cm.txt".format(i*5)))
borated_water.append(1)

for i in range(1,19):
    HDPE.append(integrate_spectrum("HDPE/HDPE_{}.txt".format(i*5)))

depth = np.linspace(0, 100, 21)

# Compute normalization to  n/m2/yr
# Detector sphere surface area:
surf_area = 4 * np.pi * 1.1**2 #m2

water_normalized = [i / (surf_area * livetime) for i in water]
borated_water_normalized = [i / (surf_area * livetime) for i in borated_water]
HDPE_normalized =  [i / (surf_area * livetime) for i in HDPE]

plt.figure()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel("Depth (cm)", fontsize=12)
plt.ylabel(r"Observed Flux (n/m$^2$/yr)", fontsize=12)
plt.scatter(depth[:19], HDPE_normalized, label = "HDPE", color='green')
plt.scatter(depth, water_normalized, label = "Water", color='blue')
plt.scatter(depth, borated_water_normalized, label = "Borated Water", color='red')
plt.yscale("log")
#plt.xscale("log")
plt.xlim(0,150)
plt.ylim(0,10000000)
plt.show()