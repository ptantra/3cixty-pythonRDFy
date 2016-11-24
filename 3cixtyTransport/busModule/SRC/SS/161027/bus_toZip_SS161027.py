# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:05:13 2015

@author: Roberto
"""
import zipfile, os, time
from time import strftime
from os.path import basename

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/busModule/') # @patrick CASA Mac setup
print os.getcwd()

#inFileB = busPathf + "OUT/" + "bus_" + strftime("%Y%m%d") + ".ttl"
inFileB = "OUT/bus.ttl"

#zf = zipfile.ZipFile(busPathf + "OUT/" + "bus_" + strftime("%Y%m%d") +'.zip' , mode='w', compression=zipfile.ZIP_DEFLATED)
zf = zipfile.ZipFile("OUT/bus.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)
try:
    print ('Creating zip file...')
    zf.write((inFileB), basename(inFileB))
finally:
    print ('Zip created')
    zf.close()

