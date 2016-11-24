import imp, os
from time import strftime

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import urlRetrieve

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/busModule/') # @patrick CASA Mac setup
print os.getcwd()


if not os.path.exists("DATA/"):
    os.makedirs(strftime("DATA/"))

pathf = "./"

inUrl = "http://data.tfl.gov.uk/tfl/syndication/feeds/bus-stops.csv?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0"
outFile = pathf + "DATA/bus-stopsAPI.csv"

urlRetrieve(inUrl, outFile)

print "DONE retrieving file"