# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:05:13 2015

@author: Roberto
"""
import time, zipfile
from time import strftime
from os.path import basename

##ZIP TFL DATA


#outPathf= "/Users/patrick/GitHub/knowledgebase/data/dump/london/tfl/"
#outPathf= "/Users/patrick/3cixty/IN/tfl/"

pathf = "/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/"
inFileB = pathf + "OUT/" + strftime("%Y%m%d") + "/tram.ttl"

zf = zipfile.ZipFile(pathf + "OUT/" + strftime("%Y%m%d") + "/tram.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)
zf = zipfile.ZipFile(pathf + "OUT/" + strftime("%Y%m%d") + "/tram.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)

print zf
try:
    print ('Creating tram zip file...')
    zf.write(inFileB)
    print zf
finally:
    print ('tram Zip created')
    zf.close()

