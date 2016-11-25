import fileinput, os
from time import strftime

import imp

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyCommon/commonFunctions.py')
from common import convertXsdDouble

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/london/') # @patrick CASA Mac setup
print os.getcwd()

def main():
    pathf = "./"
    #inFile = pathf + "IN/"+ strftime("%Y%m%d") +"/wunderground_dirty.ttl"
    inFile = pathf + "DATA/wunderground_dirty.ttl"
    outFile = pathf + "DATA/wunderground.ttl"

    print('Converting xsd:double')
    convertXsdDouble(inFile, outFile)

    print ('DONE!')

if __name__ == "__main__":
    main();

