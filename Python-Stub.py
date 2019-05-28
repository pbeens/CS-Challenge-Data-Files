'''
This stub can be used to read a data file in from this repository
'''

# import(s)
from urllib.request import urlopen

# substitute in the URL you need to read from
url ='https://raw.githubusercontent.com/pbeens/CS-Challenge-Data-Files/master/ECOO/2016/Round%202/DATA10.txt'

# read in and split text file into list of lines
lines = urlopen(url).readlines() # adapt for your specific needs >> readline? readlines? read?

# let's see what we've got...
for line in lines:
    print(line.decode().strip())