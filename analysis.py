
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.optimize import curve_fit

rc('font', **{'family': 'serif', 'serif': ['computer modern']})
rc('text', usetex=True)
"""
"""
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

depth = np.linspace(0, 100, 21)

print (depth)
print(water)

plt.figure()
plt.scatter(depth[:len(water)], water)
#plt.yscale("log")
#plt.xscale("log")
plt.xlim(-0.1,100)
plt.show()
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Given data
x_data = np.array([0., 5., 10., 15., 20., 25., 30., 35., 40., 45., 50., 55., 60., 65., 70., 75., 80., 85., 90., 95., 100.])
y_data = np.array([1003422, 902537, 562730, 302595, 150637, 73779, 35439, 17201, 8380, 4200, 2040, 1103, 574, 285, 190, 92, 36, 31, 11, 9, 4])

# Define the power-law function
def power_law(x, a, b, c, d, e, f):
    return np.cosh(b * np.sqrt(x)) * (np.exp(-c * x) + np.exp(-d * x))

# Fit the curve using least squares
popt, pcov = curve_fit(power_law, x_data, y_data)

# Generate y values for the fitted curve
y_fit = power_law(x_data, *popt)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_data, y_fit, 'r-', label='Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting with Logarithmic Scale on y-axis (Power Law)')
plt.legend()
plt.yscale("log")
plt.grid(True)
plt.show()

# Print the optimized parameters
print("Optimized Parameters:", popt)