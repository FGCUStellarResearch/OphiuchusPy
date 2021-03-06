"""
    Name: get_components.py
    Original Author: Lindsey Carboneau    

    Takes the target FITS file and writes the header keywords
    and targets to a text file. Cannot currently handle FITS files
    not in the current working directory

    TODO : add regex to handle stripping filepaths from target files    
"""
import sys, argparse              # import some useful tools, including
                                                # command line argument parse
from astropy.io import fits	# import funtions relevant to FITS files

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="Must be a valid .fits target.")
args = parser.parse_args() 

print "\nUsing : {}".format(args.infile)

components_file = open("components_{}.txt".format(args.infile), "a")

hdulist = fits.open(args.infile)

for i in range(len(hdulist)):
    component_list = hdulist[i].header.keys()
    components_file.write("\n\nComponents of {} indexed header: ".format(i))
    for k in range(len(component_list)):
        component_comment = hdulist[i].header.comments[k]
        components_file.write("\n{}: {} \t \t \t{}".format(k, component_list[k], component_comment))
