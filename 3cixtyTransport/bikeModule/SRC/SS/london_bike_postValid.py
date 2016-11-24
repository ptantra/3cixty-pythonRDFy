import fileinput
from time import strftime

import imp

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import convertXsdDouble

def main():
    pathf = "./"
    inFileB = pathf + "OUT/"+"bike_" + strftime("%Y%m%d") +"dirty.ttl"
    outFileB = pathf + "OUT/" + "bike_" + strftime("%Y%m%d") + ".ttl"

    print('Converting xsd:double')
    convertXsdDouble(inFileB, outFileB)

    print ('DONE!')

if __name__ == "__main__":
    main();

