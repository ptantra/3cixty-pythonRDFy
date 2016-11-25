import imp, csv, urllib, os, json, threading, itertools
import pandas as pd
from pandas import merge, DataFrame, ordered_merge
from time import strftime
from bs4 import BeautifulSoup
from crontab import CronTab
#from common import urlRetrieve
from Tkinter import Tk

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyCommon/commonFunctions.py')
from common import getUid, ConvertProj, definePrefixes, bindingPrefixes, readDict

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/london/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists("DATA"):
    os.makedirs("DATA")

def readCsv(inputfile):
    try:
        f = open(inputfile, 'rU');
        rf = csv.reader(f, delimiter=';');
        return rf;
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        raise


#INSERT TFL API UNIQUE API KEY AND APP NUMBER BELOWimport imp, csv, urllib, os, json, threading, itertools
import pandas as pd
from pandas import merge, DataFrame, ordered_merge
from time import strftime
from bs4 import BeautifulSoup
from crontab import CronTab
#from common import urlRetrieve
from Tkinter import Tk

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import getUid, ConvertProj, definePrefixes, bindingPrefixes, readDict

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/london/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists("DATA"):
    os.makedirs("DATA")

def readCsv(inputfile):
    try:
        f = open(inputfile, 'rU');
        rf = csv.reader(f, delimiter=';');
        return rf;
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        raise


#INSERT TFL API UNIQUE API KEY AND APP NUMBER BELOW
#key_no = "6bd6b559a24c1785"
#id_no = "IGREENFO2"

inFileB = 'DATA/stations_fullNoDuplicate.csv' #change to stations
csvB = list(readCsv(inFileB))
csvX = readCsv(inFileB)

#csvDivide = len(csvB)/70
csvDivide = len(csvB)/1

def pullForecast():
    with open(inFileB, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        idNo_array = [row[0] for row in spamreader]

        fMain = csv.writer(open("DATA/wunderground_realTime.csv", "wb+"))
        fMain.writerow(['stationId',
                        'epoch',
                        'condition'])

        for row in itertools.islice(idNo_array, 0, csvDivide, 1):
            idNo = ', '.join([row])
            key_no = '3d776fe610a62562'
            inUrl = ('http://api.wunderground.com/api/%s/forecast/q/pws:%s.json?bestfct=1') % (key_no, idNo)
            response = urllib.urlopen(inUrl)

            fJson = json.load(response)

            fMain.writerow([idNo,
                            fJson['forecast']['simpleforecast']['forecastday'][0]['date']['epoch'],
                            fJson['forecast']['simpleforecast']['forecastday'][0]['icon']])

            response.close()

pullForecast()






#key_no = "6bd6b559a24c1785"
#id_no = "IGREENFO2"

inFileB = 'DATA/stations_fullNoDuplicate.csv' #change to stations
csvB = list(readCsv(inFileB))
csvX = readCsv(inFileB)

#csvDivide = len(csvB)/70
csvDivide = len(csvB)/1

def pullForecast():
    with open(inFileB, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        idNo_array = [row[0] for row in spamreader]

        fMain = csv.writer(open("DATA/wunderground_realTime.csv", "wb+"))
        fMain.writerow(['stationId',
                        'epoch',
                        'condition'])

        for row in itertools.islice(idNo_array, 0, csvDivide, 1):
            idNo = ', '.join([row])
            key_no = '3d776fe610a62562'
            inUrl = ('http://api.wunderground.com/api/%s/forecast/q/pws:%s.json?bestfct=1') % (key_no, idNo)
            response = urllib.urlopen(inUrl)

            fJson = json.load(response)

            fMain.writerow([idNo,
                            fJson['forecast']['simpleforecast']['forecastday'][0]['date']['epoch'],
                            fJson['forecast']['simpleforecast']['forecastday'][0]['icon']])

            response.close()

pullForecast()





