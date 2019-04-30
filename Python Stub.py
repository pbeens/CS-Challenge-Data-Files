# This stub can be used to read a data file in from this repository

from urllib.request import urlopen

url = '' # <--- enter the URL here

textFile = urlopen(url).readlines() # adapt for your specific needs >> readline? readlines? read?

print(textFile) # Just to check if the data got read in correctly. Delete once you're satisfied eveything is working okay.
