# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:05:13 2015

@author: Roberto
"""
import time
import zipfile, os
from time import strftime
from os.path import basename

##ZIP TFL DATA

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/bikeModule/') # @patrick CASA Mac setup
print os.getcwd()

inPathf="/Users/patrick/3cixty/codes/3cixtyTransport/bikeModule/OUT/"
#outPathf= "/Users/patrick/GitHub/knowledgebase/data/dump/london/tfl/"
outPathf= "/Users/patrick/3cixty/codes/3cixtyTransport/bikeModule/OUT/"

#zf = zipfile.ZipFile(outPathf + 'tfl_bikes' + strftime("%Y%m%d") +'.zip' , mode='w', compression=zipfile.ZIP_DEFLATED)
zf = zipfile.ZipFile('20160822/tfl_bikes.zip' , mode='w', compression=zipfile.ZIP_DEFLATED)
try:
    print ('Creating zip file...')
    #zf.write((inPathf + 'tfl_bikes' + strftime("%Y%m%d")+ '.ttl'), basename(inPathf + 'tfl_bikes' + strftime("%Y%m%d") +'.ttl'))
    zf.write(('20160822/tfl_bikes.ttl'), basename('20160822/tfl_bikes.ttl'))
    print zf
finally:
    print ('Zip created')
    zf.close()

