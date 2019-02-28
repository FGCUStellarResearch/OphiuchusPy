#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Python 3 script for creating little movies of Gamma Ray Burst targets
from TESS data stamps created from the FFIs using TESScut

NOTE: This is an updated version of the 'GRBvisual.py' script which
        provides both better functionality and some automation.
        Thanks to Oliver Hall for letting me watch over his shoulder
        when he made similar animations for TASOC background corrections

Created 07 Feb 2019
Updated 28 Feb 2019

.. codeauthor:: Lindsey Carboneau  <lmcarboneau@gmail.com>
"""

import numpy as np 
from astropy.io import fits
import matplotlib.pyplot as plt 
import matplotlib.colors as colors
import matplotlib.animation as animation
from IPython.display import HTML
#NOTE: the HTML functions may not be needed, since this was held over from a .ipynb

###############################################################################
# automation section
import os
import sys
import fnmatch

check_input = input("Input folder or nothing for default local: ")
if check_input == '':
    input_folder = os.getcwd()
else:
    input_folder = check_input

def check_for_data(input_folder):
    active_sectors = ['01', '02', '03', '04', '05', '06']
    postage_stamps = []
    if "input" in input_folder:
        try: 
            for sector in active_sectors:
                sector_folder = input_folder + '/S' + sector
                if os.path.isdir(sector_folder):
                    for filename in os.listdir(sector_folder):
                        if fnmatch.fnmatch(filename, '*.fits'):
                            postage_stamps.append(sector_folder + '/' + filename)
                    if not postage_stamps:
                        print('No valid FITS file folders were found in directory: ' + input_folder)
                        exit()
                else:
                    # should just try looping to the next sector (for now)
                    continue
        except NotADirectoryError:
            # should probably loop back into asking for input again
            pass
        except:
            print("Unexpected error: ", sys.exc_info()[0])
            exit()
    else:
        try:
            # try to find fits files
            raise NotImplementedError
        except:
            print("Not implemented!") 
            exit()
    
    return postage_stamps

###############################################################################
# data ingest
def get_fits_data(tess_file):
    fitsfile = fits.open(tess_file)
    headerdata = fitsfile[0].header
    checkdata = fitsfile[1].data
    fitsfile.close()
    pixeldata = np.asarray(checkdata)
    return (headerdata, pixeldata, checkdata)

###############################################################################
# animation helper
# NOTE: there's probably some bad practice here, in that 'pixels' is in a different
#       scope and isn't being passed, but is still being updated in here
def update_fig(idx): 
    image0 = np.stack(pixels['FLUX'][idx])
    try:
        imageN = np.stack(pixels['FLUX'][idx + 1])
    except IndexError:
        imageN = np.stack(pixels['FLUX'][idx])
    except Exception as ex:
        print('There was a different problem: ' + str(ex))
        
    im_im.set_array(image0)
    
    im_diff.set_array(np.subtract(imageN, image0))
    
    return im_im,


tess_files = check_for_data(input_folder)
for target in tess_files:
    target_id = target.split('/')[-1].split('_')[1:-1]
    # format: [RA, DEC, StampSize]
    header, pixels, check = get_fits_data(target)
    fig, ax = plt.subplots(1, 2, figsize=(9,4))
    fig.suptitle('GRB: '+','.join(target_id[0:-1]), fontsize=20) 

    ax_im = ax[0]
    ax_diff = ax[1]

    Z = np.stack(pixels['FLUX'][0])
    im_im = ax_im.imshow(Z, norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()),
                    cmap='PuBu_r', animated=True)
    im_diff = ax_diff.imshow(Z, norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()),
                    cmap='PuBu_r', animated=True)

    ax_im.set_title('Raw Flux from FFI - LogNorm')
    ax_diff.set_title('Diff Flux: Changes - LogNorm')
    ax_im.set_yticklabels([])
    ax_im.set_xticklabels([])
    ax_diff.set_yticklabels([])
    ax_diff.set_xticklabels([])

    ani = animation.FuncAnimation(fig, update_fig, frames=len(pixels), blit=True, repeat=True, interval=400)
    #HTML(ani.to_html5_video())
    ani.save('_'.join(target_id) + '.mp4')
    plt.close(fig)

    Z = np.stack(pixels['FLUX'][0])
    plt.imshow(Z)
    plt.savefig('_'.join(target_id) + '.png')
    plt.close()