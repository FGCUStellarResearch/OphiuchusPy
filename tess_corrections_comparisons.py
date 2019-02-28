#!/user/bin/env python3 
"""
Module documentation.


"""

import os
import argparse
import fnmatch
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input', help='Folder path of the first corrected data sets')
parser.add_argument('-c','--compare', help='Folder path of the data sets for comparison')
parser.add_argument('-o','--output', help='Folder path to saved final comparisons')
parser.add_argument('--ext', help='Extension of detrended data', default='*.ext')
args = parser.parse_args()

tess_files = []
base_time, base_flux, base_corr, comparison_time, comparison_corr = [], [], [], [], []

for filename in os.listdir(args.input):
    if fnmatch.fnmatch(filename, args.ext):
        tess_files.append(os.path.join(args.input, filename))
if not tess_files[0]:
    print("No valid inputs found in ", args.input)
    quit()
else:
    tess_files.sort()
    for filename in tess_files:
        print(filename.split('/')[-1])
        print(os.path.join(args.compare,filename.split('/')[-1]))
        try:
            comparison = open(os.path.join(args.compare,filename.split('/')[-1]), 'r')
            base = open(filename,'r')
            base_time, base_flux, base_corr = np.loadtxt(base,unpack=True)
            comparison_time, comparison_flux, comparison_corr = np.loadtxt(comparison,unpack=True)
            base.close()
            comparison.close()

        except:
            print("File/Input does not exist in comparison: ",filename)
            #NOTE: this isn't actually a useful or relevant error message
            pass
        

        plt.figure(figsize=(14,9))
        plt.suptitle('Comparison of '+filename.split('/')[-1])
        plt.subplot(221)
        plt.plot(base_time, (base_flux/np.median(base_flux)),'.', color='black')
        plt.plot(base_time, (base_corr/np.median(base_corr)), '.', color='xkcd:bright blue')
        plt.title('raw vs algorithm correction')
        plt.subplot(222)
        plt.plot(comparison_time, (comparison_flux/np.median(comparison_flux[~np.isnan(comparison_flux)])),'.', color='black')
        plt.plot(comparison_time, (comparison_corr/np.median(comparison_corr[~np.isnan(comparison_corr)])),'.', color='xkcd:pumpkin')
        plt.title('raw vs pipeline correction')
        plt.subplot(223)
        plt.plot(base_time, (base_corr/np.median(base_corr)),'.', color='xkcd:bright blue')
        plt.plot(comparison_time, (comparison_corr/np.median(comparison_corr[~np.isnan(comparison_corr)])),'.', color='xkcd:pumpkin')
        plt.title('algorithm correction vs pipeline correction')
        plt.subplot(224)
        #plt.plot(base_time, (base_corr - (comparison_corr[np.isfinite(comparison_corr)])), '.')
        plt.title('correction algorithm difference')
        plt.show(block=True)