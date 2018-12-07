#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Python script for downloading single target or batch TESS data in FITS format
from MAST; large batches of data can be retrieved in an automated fashion 
TODO: while more gracefully recovering from issues

Static Parameters:
    

TODO:   Determine if this can be integrated into a common data downloader; see getFITS.py

Created 7 Dec 2018

.. codeauthor:: Lindsey Carboneau
"""

# for arguements without stupid argparse nonsense
import sys, getopt, os
import wget
import glob

# set some defaults
inputFile = ""
outputFolder = os.getcwd() + "/output"

# command line entries 
allArgs = sys.argv
argList = allArgs[1:]

# create valid parameters
unixOptions = "ho:i:" # ':' means the same as '=' below
gnuOptions = ["help", "output=", "input="]

try:
    args, values = getopt.getopt(argList, unixOptions, gnuOptions)
except getopt.error as err:
    # let us know what went wrong
    print (str(err))
    sys.exit(2)

for thisArg, thisValue in args:
    if thisArg in ("-h", "--help"):
        print ("help message")
        sys.exit() # not strictly an error, but execution shouldn't continue 
    if thisArg in ("-o", "--output"):
        # set output path to user-specified
        outputFolder = os.getcwd() + "/" + str(thisValue) # NOTE: only accepts relative paths!
    if thisArg in ("-i", "--input"):
        # set input file to user-specified
        inputFile = str(thisValue) # NOTE: only accepts relative or full paths!

if not os.path.exists(inputFile):
    print("No input file found at: " + inputFile)
    sys.exit(1) # can't run without input, so exit with error; TODO: some smart handling?

if not os.path.exists(outputFolder):
    try:
        os.makedirs(outputFolder)
    except OSError as err:
        if err.errno != err.errno.EEXIST:
            raise # NOTE: this is to avoid a possible race condition

with open(inputFile) as file:
    TIClist = [line.rstrip() for line in file]

###############################################################################
#
# THIS SECTION IS HARDCODED - SECTORS MUST BE SPECIFIED SOMEWHERE
# IT ALSO ONLY ALLOWS DOWNLOAD OF CR MITIGATION METHOD 's' - SPACECRAFT
# TODO: fix this
#
###############################################################################
sector1prefix = "tess2018206045859-s0001-"
sector1postfix = "-0120-s_lc.fits"

sector2prefix = "tess2018234235059-s0002-"
sector2postfix = "-0121-s_lc.fits"

mastURL = "https://mast.stsci.edu/api/v0.1/Download/file/?uri=mast:TESS/product/"

for target in TIClist:
    padding = "0" * (16 - len(target))
    targetp = padding + target
    try:
        print("\ntrying sector1")
        url = mastURL + sector1prefix + targetp + sector1postfix
        outPath = outputFolder + "/" + sector1prefix + targetp + sector1postfix
        test = wget.download(url, out=outPath)
        if (os.path.exists(test)):
            print("\nGot target: " + target)
            continue
    except:
        pass
    try:
        print("trying sector2")
        url = mastURL + sector2prefix + targetp + sector2postfix
        outPath = outputFolder + "/" + sector2prefix + targetp + sector2postfix
        test = wget.download(url, out=outPath)
        if (os.path.exists(test)):
            print("\nGot target: " + target)
            continue
    except:
        pass

    if ~(os.path.isfile(outputFolder + "/" + sector1prefix + targetp + sector1postfix) or 
        os.path.isfile(outputFolder + "/" + sector2prefix + targetp + sector2postfix)):
        print("Could not download target: " +  str(target))
        continue





