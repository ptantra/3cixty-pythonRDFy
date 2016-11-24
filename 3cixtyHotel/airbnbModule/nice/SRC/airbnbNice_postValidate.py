import os
from time import strftime

import imp

os.chdir('/Users/patrick/3cixty/codes/3cixtyHotel/airbnbModule/nice/') # @patrick CASA Mac setup
print os.getcwd()

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import convertXsdDouble

def convertFaultyUri(inFile, outFile):
    s = open(inFile).read()
    print s
    s = s.replace("locationResPLACEHOLDER:", "locationRes:")
    s = s.replace("^^xsd:placeholder", "^^xsd:double")


    #print list.index(s)

    f = open(outFile, 'w')
    f.write(s)
    print s
    f.close()


def main():
    inFileB = '/Users/patrick/3cixty/codes/3cixtyHotel/airbnbModule/nice/DATA/airbnbNice_dirty.ttl'


    print inFileB
    outFileB = '/Users/patrick/3cixty/codes/3cixtyHotel/airbnbModule/nice/DATA/airbnb_Nice.ttl'

    print('Converting xsd:double')
    #convertXsdDouble(inFileB, outFileB)
    convertFaultyUri(inFileB, outFileB)

    print ('DONE!')

if __name__ == "__main__":
    main();

