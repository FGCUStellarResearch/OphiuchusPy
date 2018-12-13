#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Python script for trying to visualize data stored in the TESScut output
DS9 and FV viewer both had trouble properly displaying data, so the goals are:
1) prove the data is actually there
2) find a way to create a gif/movie from the data

Static Parameters:
    

TODO:   Consider if this can just reformat the FITS file so that DS9 accepts the format

Created 11 Dec 2018

.. codeauthor:: Lindsey Carboneau
"""

from astropy.io import fits
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
#import os

# TODO: 'interactive' to play with all FITS in folder/give an input
tessfile = 'tess-s0002-3-4_49.19939_-58.53253_25x25_astrocut.fits'

# step 1: read in data
fitsfile = fits.open(tessfile)
pixeldata = fitsfile[1].data
fitsfile.close()
pixeldata = np.asarray(pixeldata)
#print(pixeldata['FLUX'][0])
# step 2: reduce data (?)
# pixeldata['FLUX'] is a big ol' array o' arrays;
# pixeldata['FLUX'][0] is the first cadence
# pixeldata['FLUX'][0][0] is the first column(row?) of the first cadence

postagestamp = plt.figure()

x = np.arange(0, 25)
y = np.arange(0, 25).reshape(-1, 1)
ims = []
for cadence in range(len(pixeldata['FLUX'])):
     ims.append((plt.pcolor(x, y, pixeldata['FLUX'][cadence]),))


# step : plot the images
im_ani = animation.ArtistAnimation(postagestamp, ims, interval=20, 
                                   blit=True)

plt.show()
#im_ani.save(tessfile.split('_')[0] +'.mp4')