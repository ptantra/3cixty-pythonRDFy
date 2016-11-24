# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:05:13 2015

@author: Roberto
"""
import time, zipfile, os
from time import strftime
from os.path import basename

##ZIP TFL DATA

#outPathf= "/Users/patrick/GitHub/knowledgebase/data/dump/london/tfl/"
#outPathf= "/Users/patrick/3cixty/IN/tfl/"

os.chdir('/Users/patrick/3cixty/codes/3cixtyHotel/airbnbModule/london/') # @patrick CASA Mac setup
print os.getcwd()

inFileB = 'DATA/airbnb_LondonSmall.ttl'

zf = zipfile.ZipFile('DATA/airbnb.zip' , mode='w', compression=zipfile.ZIP_DEFLATED)

try:
    print ('Creating airbnb zip file...')
    zf.write(inFileB, basename(inFileB))
    print zf
finally:
    print ('airbnb Zip created')
    zf.close()

