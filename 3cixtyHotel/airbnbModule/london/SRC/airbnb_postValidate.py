import os, imp
from time import strftime

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import convertXsdDouble

os.chdir('/Users/patrick/3cixty/codes/3cixtyHotel/airbnbModule/london/') # @patrick CASA Mac setup
print os.getcwd()

def main():
    inFileB = 'DATA/airbnb_LondondirtySmall.ttl'
    outFileB = 'DATA/airbnb_londonSmall.ttl'

    print('Converting xsd:double')
    convertXsdDouble(inFileB, outFileB)

    print ('DONE!')

if __name__ == "__main__":
    main();

