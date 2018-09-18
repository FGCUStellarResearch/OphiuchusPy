# script to turn the K2Campaign#targets.csv files, found at 
# keplerscience.arc.nasa.gov/K2/docs/Campaigns/C#/K2Campaign#targets.csv or
# keplerscience.arc.nasa.gov/data/campaigns/c#/K2Campaign#targets.csv
# and saved locally as c#TargetsGO, to input file for the downloader script

from sys import version_info

py3 = version_info[0] > 2 # (bool) check if version is not 2.7
if py3:
    num = input("Enter campaign: ")
else:
    num = raw_input("Enter campaign: ")


# open original GO .csv file to read in target list
with open('c' + num + 'TargetsGO') as file:
    targets = file.readlines()
# close it again
file.close()

# open/create new target-only input list for the downloader script
with open('c' + num + 'Targets','w') as file:
    for target in targets:
    # print every line, unless there is ONLY short cadence data
        if 'LC' in target:
            file.write(target[:9] + '\n')
# file closes on program exit
