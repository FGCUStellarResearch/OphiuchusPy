"""
File Manipulation

This script file contains basics for using Python to manipulate files.
The output of this script is a tab delimited file containing a list
of files found in the designated folder matching the requirements.

NOTE:
This script is written primarily for Python 2.7 and its behavior in
environments running Python 3 is untested and not supported

This script uses the "os" package to allow for easy interaction with the
OS directory structure - documentation: https://docs.python.org/2/library/os.html

This script uses "argparse" to allow for arguments to be passed in at
runtime - documentation here: https://docs.python.org/2/howto/argparse.html


TODO:



Author: Lindsey Carboneau
Python3 edition: 12 June 2018
Original: 7 November 2017
"""

# lets you interact with files using OS/terminal commands:
import os
# lets you read in arguments passed when running the script from
# a terminal or wrapper script:
import argparse
# easy way to compare and find matches in file names:
import fnmatch

# list of files to run through
fitsfiles = []


# parse input arguements to determine filepath folder, specified output; optional
# os.getcwd: full path of current working directory (ex: '/home/user/Documents/')
parser = argparse.ArgumentParser(description='Data File reduction for and K2 output files')

parser.add_argument('-i', '--input', help='input folder, default local: ' + os.getcwd(),
        default=os.getcwd())

parser.add_argument('-o', '--output', help='output path, default local: ' + os.getcwd(),
        default=os.getcwd())

parser.add_argument('-f', '--format', help='use alternate output format, default tab-delimited',
        nargs='?', const='latex', default='tab')	
	
args = parser.parse_args()


# find the files to sort through - will pull the whole folder
for filename in os.listdir(args.input):
    if fnmatch.fnmatch(filename, '*.fits'):
        fitsfiles.append(args.input+'/'+filename)
if not fitsfiles:
    # for the case of the wrong folder/empty folder/no matching files
    print('No valid FITS files were found in directory: ' + args.input)
    quit()

# sorting is a best practice for most cases - the OS order may not be useful otherwise
fitsfiles.sort()