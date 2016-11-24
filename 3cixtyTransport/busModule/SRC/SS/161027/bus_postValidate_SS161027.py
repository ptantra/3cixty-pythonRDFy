import os
from time import strftime

import imp

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/busModule/') # @patrick CASA Mac setup
print os.getcwd()

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import convertXsdDouble

def main():
    inFileB = '/Users/patrick/3cixty/codes/3cixtyTransport/busModule/OUT/validation/bus_dirty.ttl'
    outFileB = '/Users/patrick/3cixty/codes/3cixtyTransport/busModule/OUT/bus.ttl'

    print('Converting xsd:double')
    convertXsdDouble(inFileB, outFileB)

    print ('DONE!')

if __name__ == "__main__":
    main();

