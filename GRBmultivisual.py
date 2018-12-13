#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Python script for trying to visualize data stored in the TESScut output
Different views of the data in subplots

Created 12 Dec 2018

.. codeauthor:: Lindsey Carboneau
"""

from astropy.io import fits
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        # create an initial figure handle
        fig = plt.figure()
        # common practice is to name each subplot as 'ax#', but it gets hard to read
        axflux = fig.add_subplot(1, 2, 1)
        axlog = fig.add_subplot(2, 2, 2)
        axdiff = fig.add_subplot(2, 2, 4)

        # these are the bounds for the axes, hardcoded for a 25x25 pixel postage stamp
        self.x = np.arrange(0, 25)
        self.y = np.arrange(0, 25).reshape(-1, 1)

        ''' Setting up subplots one by one '''
        # 1: pixel data (image) subplot
        # might not actually need any? axes are coords
        axflux.set_title('Calibrated Flux Pixel Cutout')

        # 2: log pixel data (image) subplot
        # same as above; TODO: look into if this is where to put labels/colorbars
        axlog.set_title('Log Flux - relative flux levels?')

        # 3: differenced pixel data (image) subplot
        # see above;
        axdiff.set_title('Difference image - changes')

        # actually call out to the animation engine
        animation.TimedAnimation.__init__(self, fig, interval=25, blit=True)

    def _draw_frame(self, framedata):
        # possibly an overloaded function of TimedAnimation, otherwise I'd name it 'update'



# TODO: 'interactive' to play with all FITS in folder/give an input
tessfile = 'tess-s0002-3-4_49.19939_-58.53253_25x25_astrocut.fits'

# step 1: read in data
fitsfile = fits.open(tessfile)
pixeldata = fitsfile[1].data
fitsfile.close()
pixeldata = np.asarray(pixeldata['FLUX'])

# print(pixeldata[0]) # list of lists of lists; probably columns? in frames

plot_animation = SubplotAnimation()
# plot_animation.save('test.mp4')
plt.show()