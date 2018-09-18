import wget
# import time	 # see NOTE below - uncomment for funtionality
# import datetime


# K2 Downloader - Python
#
#    Downloads a list of K2 raw data files from the archives.stsci.edu servers
#    List is input as a line-break delimited text file, listing the EPIC IDs


# K2 file extension for standard long cadence raw data files (Campaign 8)
filext = '-c08_lpd-targ.fits.gz'
folder = 'c8/weightedexp/'


# this input file is HARDCODED because methods for user-input filenames differ,
# depending on which version of python you are running (TODO: add filename input?)
with open('c8Targets') as file:
    targets = file.readlines()
file.close() 

# starte = time.time() # see NOTE below


for target in targets:

    # create base url for data download
    urlbase = 'https://archive.stsci.edu/pub/k2/target_pixel_files/c8/'
    # then add the directories for the target
    urlbase += target[:4] + '00000/' + target[4:6] + '000'

    # attach each file extension to the end of each KID
    url = urlbase + '/ktwo' + target[:-1] + filext
    # then request the download from the server
    wget.download(url, out=folder)


# NOTE: If you are downloading multiple files, you may find you want timestamps
#       so you can determine how long each file took to download; in this case,
#       uncommenting this section and moving it to within the main loop of this
#       program will allow you to monitor via terminal (TODO: add file output?)

    # start = time.time()

    # code goes here
    
    # timesec = time.time()
    # timestamp = datetime.datetime.fromtimestamp(timesec).strftime('%Y-%m-%d %H:%M:%S')
    # print timestamp

# totale = time.time() - starte
# print totale
