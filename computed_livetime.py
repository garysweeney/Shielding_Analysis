import numpy as np

def compute_livetime(nEvents):

    # Load the norite rock data
    file = "sim_data.dat"
    data = np.genfromtxt(file, dtype=str)

    # Obtain production rates [n/g/s/ppb]
    production_rate = (data[2:,1])
    production_rate = [float(i) for i in production_rate]

    # Obtain activity [ppb]
    activity = (data[2:,2])
    activity = [float(i) for i in activity]

    # Compute mass of norite sphere
    volume = ((4 * np.pi) / 3) * (10.**3)#(340.**3 - 270.**3) # 4pi/3 r^3 [cm3]
    density = 2.88 # [g/cm3]
    mass = volume * density #[g]

    # Apply U-235 abundance factor
    livetime = (nEvents / (production_rate[3] * activity[3] * mass)) * 0.007
    for i in range(3):
        livetime += (nEvents / (production_rate[i] * activity[i] * mass))

    # Convert to years
    livetime /= (365 * 24 * 3600)

    return livetime