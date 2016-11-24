import fileinput, os
from time import strftime

import imp

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import convertXsdDouble

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/') # @patrick CASA Mac setup
print os.getcwd()

def main():
    inFileB ="OUT/" + strftime("%Y%m%d") + "/overground_dirty" +".ttl"
    outFileB = "OUT/" + strftime("%Y%m%d") + "/overground" + ".ttl"

    print('Converting xsd:double')
    convertXsdDouble(inFileB, outFileB)

    print ('DONE!')

if __name__ == "__main__":
    main();

