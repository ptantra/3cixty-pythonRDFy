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

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/ferryModule/') # @patrick CASA Mac setup
print os.getcwd()


pathf = "/Users/patrick/3cixty/codes/3cixtyTransport/ferryModule/"
#inFileB = "OUT/" + strftime("%Y%m%d") + "/ferry.ttl"
inFileB = "DATA/ferry.ttl"

#zf = zipfile.ZipFile("OUT/" + strftime("%Y%m%d") + "/ferry.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)
zf = zipfile.ZipFile("DATA/ferry.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)

print zf
try:
    print ('Creating ferry zip file...')
    zf.write(inFileB, basename(inFileB))
    print zf
finally:
    print ('ferry Zip created')
    zf.close()




