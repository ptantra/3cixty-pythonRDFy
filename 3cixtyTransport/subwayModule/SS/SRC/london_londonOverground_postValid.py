import fileinput, os
from time import strftime

import imp

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import convertXsdDouble

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/') # @patrick CASA Mac setup
print os.getcwd()

def main():
    pathf = "./"
    inFileB = pathf + "subwayModule/OUT/" + strftime("%Y%m%d") + "/londonOverground_dirty" +".ttl"
    outFileB = pathf + "subwayModule/OUT/" + strftime("%Y%m%d") + "/londonOverground" + ".ttl"

    print('Converting xsd:double')
    convertXsdDouble(inFileB, outFileB)

    print ('DONE!')

if __name__ == "__main__":
    main();

