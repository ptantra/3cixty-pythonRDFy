# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:05:13 2015

@author: Roberto
"""
import time, zipfile, os
from time import strftime
from os.path import basename

##ZIP TFL DATA

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/') # @patrick CASA Mac setup
print os.getcwd()

#outPathf= "/Users/patrick/GitHub/knowledgebase/data/dump/london/tfl/"
#outPathf= "/Users/patrick/3cixty/IN/tfl/"

#inFileB = pathf + "OUT/" + strftime("%Y%m%d") + "/tram.ttl"
inFileB = "OUT/tram.ttl"

zf = zipfile.ZipFile("OUT/tram.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)
#zf = zipfile.ZipFile(pathf + "OUT/" + strftime("%Y%m%d") + "/tram.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)

print zf
try:
    print ('Creating tram zip file...')
    zf.write(inFileB, basename(inFileB))
    print zf
finally:
    print ('tram Zip created')
    zf.close()

