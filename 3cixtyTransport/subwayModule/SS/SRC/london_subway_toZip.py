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
inFileB = pathf + "OUT/" + strftime("%Y%m%d") + "/subwayLine.ttl"

zf = zipfile.ZipFile(pathf + "OUT/" + strftime("%Y%m%d") + "/subwayLine.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)
zf = zipfile.ZipFile(pathf + "OUT/" + strftime("%Y%m%d") + "/subwayLine.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)

print zf
try:
    print ('Creating zip file...')
    zf.write(inFileB)
    print zf
finally:
    print ('Zip created')
    zf.close()



'''
busPathf = "./"
inFileB = busPathf + "OUT/" + "bus_" + strftime("%Y%m%d") + ".ttl"

zf = zipfile.ZipFile(busPathf + "OUT/" + "bus_" + strftime("%Y%m%d") +'.zip' , mode='w', compression=zipfile.ZIP_DEFLATED)
try:
    print ('Creating zip file...')
    zf.write((inFileB), basename(inFileB))
    print zf
finally:
    print ('Zip created')
    zf.close()
'''

