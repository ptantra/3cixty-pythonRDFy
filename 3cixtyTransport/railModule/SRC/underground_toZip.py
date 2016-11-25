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

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/railModule/') # @patrick CASA Mac setup
print os.getcwd()

inFileB = "DATA/underground.ttl"
zf = zipfile.ZipFile("DATA/underground.zip" , mode='w', compression=zipfile.ZIP_DEFLATED)

print zf
try:
    print ('Creating zip file...')
    zf.write(inFileB, basename(inFileB))
    print zf
finally:
    print ('Zip created')
    zf.close()

