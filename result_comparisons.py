# -*- coding: utf-8 -*-
"""
automating light curve correction comparisons 

also for use as example for comparison graphing with numpy and matplotlib

.. codeauthor:: Lindsey Carboneau
"""

import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path 

def normalize(v):
    v = v[~np.isnan(v)]
    norm = np.sqrt((v**2))
    if norm.sum() == 0:
        return v
    return (v / np.median(norm))

# read in raw photometry 
# option A - simulations
raw_data = (input("Target photometry file: "))
if not (Path(raw_data).is_file()):
    print("make sure to use full path to sysnoise file")
    exit()
try:
    with open(raw_data) as data_in:
        phot_time, phot_flux = np.loadtxt(data_in, usecols=range(0, 2), unpack=True)
except:
    print("Couldn't open photometry file")
    exit()
# TODO: option B - tasoc photometry


# read in correction results
# plot 1, 0: og ensemble seg_detrend (T'DA5)
tda5_data = (input("Comparison ensemble detrend file: "))
if not (Path(tda5_data).is_file()):
    print("make sure to use the full path to the corrected sysnoise file")
    exit()
try: 
    with open(tda5_data) as data_in:
        tda5_time, og_flux, tda5_flux = np.loadtxt(data_in, usecols=range(0, 3), unpack=True)
except:
    print("Couldn't open TDA5 file")
    exit()

# plot 1, 1: cbv detrend (TODO - real data)

# plot 2, 0: devel ensemble detrend (T'DA8)
tda8_data = (input("Development ensemble detrend file: "))
if not (Path(tda8_data).is_file()):
    print("make sure to use the full path to the corrected sysnoise file")
    exit()
try:
    with open(tda8_data) as data_in:
        tda8_time, tda8_flux = np.loadtxt(data_in, usecols=range(0, 2), unpack=True)
except:
    print("Couldn't open TDA8 file")
    exit()

# plot 2, 1: KASOC filter (TODO - real data)

# TODO: normalize? 

# NOTE: ncols = 2  # for doing real comparisons 
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(7, 7))

# plot original tasoc photometry lightcurve
print(str(raw_data).split("/")[-1].split(".")[0])
axes[0, 0].set_title(str(raw_data).split("/")[-1].split(".")[0]) # TODO: string formatting, should be TIC# and tasoc photometry
axes[0, 0].plot(phot_time, phot_flux) # TODO: data goes here, need to read in first
axes[0, 0].set_xlabel("Time")
axes[0, 0].set_ylabel("Flux")

tda5_time = tda5_time[~np.isnan(tda5_flux)]
axes[1, 0].set_title("Comparison Ensemble")
axes[1, 0].plot(tda5_time, normalize(tda5_flux))
axes[1, 0].set_xlabel("Time")
axes[1, 0].set_ylabel("Normalized Flux")

# axes[1, 1].set_title()
# axes[1, 1].plot()
# axes[1, 1].set_xlabel("Time")
# axes[1, 1].set_ylabel("Normalized Flux")

tda8_time = tda8_time[~np.isnan(tda8_flux)]
axes[2, 0].set_title("Development Ensemble")
axes[2, 0].plot(tda8_time, normalize(tda8_flux))
axes[2, 0].set_xlabel("Time")
axes[2, 0].set_ylabel("Normalized Flux")

# axes[2, 1].set_title()
# axes[2, 1].plot()
# axes[2, 1].set_xlabel("Time")
# axes[2, 1].set_ylabel("Normalized Flux")

fig.tight_layout()
plt.show(block=True)