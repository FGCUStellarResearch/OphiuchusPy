#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Python script for downloading single target or batch data in FITS format
from MAST without using the FTP server. Large batches of data can be 
retrieved in an automated fashion while more gracefully recovering from issues

Static Parameters:
    __C6_ID__ (int)         :   Spica C6 EPIC ID TODO: change to str?
    __C17_ID__ (int)        :   Spica C17 EPIC ID TODO: change to str?
    __output_folder__ (str) :   Location of output data

TODO:   Create new/Modify this script to handle non-MAST/FITS sources (like Gaia)

Created 18 Sept 2018

.. codeauthor:: Lindsey Carboneau
"""

import os
import wget
import argparse

# parse input arguements to determine filepath folder, specified output; optional
# os.getcwd: full path of current working directory (ex: '/home/user/Documents/')
parser = argparse.ArgumentParser(description='Automated data retrival from MAST')

parser.add_argument('-i', '--input', help='input target or list file, default local: ' + os.getcwd(),
        default=os.getcwd())

parser.add_argument('-o', '--output', help='output path, default local: ' + os.getcwd(),
        default=os.getcwd() + '/data')

parser.add_argument('-f', '--format', help='use alternate output format, default tab-delimited',
        nargs='?', const='latex', default='tab')	
	
args = parser.parse_args()

# check if output folder exists, and make if not
if not os.path.isdir(args.output):
    os.mkdir(args.output)

# figure out where the data is (by name or by list)


# download the data, file-by-file; try each, then if there's an issue log it and move on; if 5(+?) fail in a row, exit
for filename in targetlist:
    try:
        # create the url
        url = ''
        wget.download(url, out=filename)
    except expression as identifier:
        pass
    finally:
        pass