# This stub can be used to read a data file in from this repository

from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/pbeens/CS-Challenge-Data-Files/master/ECOO/2016/Round%202/DATA10.txt' # <--- enter the URL here

textFile = urlopen(url).read().decode('utf-8') # adapt for your specific needs >> readline? readlines? read?

 # Just to check if the data got read in correctly. Delete once you're satisfied everything is working okay.
lines = textFile.strip().split('\n')
print(lines)
print(textFile)
