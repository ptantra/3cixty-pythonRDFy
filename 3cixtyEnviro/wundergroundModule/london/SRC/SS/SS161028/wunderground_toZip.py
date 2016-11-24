# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:05:13 2015

@author: Roberto
"""
import time, zipfile, os
from time import strftime
from os.path import basename

#outPathf= "/Users/patrick/GitHub/knowledgebase/data/dump/london/tfl/"
#outPathf= "/Users/patrick/3cixty/IN/tfl/"

#os.chdir('Z:/3cixty/3cixty_160822/3cixtyEnviro/wundergroundModule/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/') # @patrick CASA Mac setup

#inFile = "OUT/" + strftime("%Y%m%d") + "/wunderground.ttl"
inFile = "OUT/wunderground.ttl"

#zf = zipfile.ZipFile("OUT/" + strftime("%Y%m%d") + "/wunderground.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)
zf = zipfile.ZipFile("OUT/wunderground.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)


try:
    print ('Creating zip file...')
    zf.write(inFile, basename(inFile))
    print zf
finally:
    print ('Zip created')
    zf.close()


