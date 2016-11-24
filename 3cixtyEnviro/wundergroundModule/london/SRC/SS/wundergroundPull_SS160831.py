import imp, csv, urllib, os, json, threading, itertools
import pandas as pd
from pandas import merge, DataFrame, ordered_merge
from time import strftime
from bs4 import BeautifulSoup
from crontab import CronTab
#from common import urlRetrieve
from Tkinter import Tk

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/') # @patrick CASA Mac setup
print os.getcwd()

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import getUid, ConvertProj, definePrefixes, bindingPrefixes, readDict

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists("IN/"+ strftime("%Y%m%d")):
    os.makedirs(strftime("IN/"+ strftime("%Y%m%d")))

if not os.path.exists("IN/_" + strftime("%Y%m%d")):
    os.makedirs(strftime("IN/_" + strftime("%Y%m%d")))


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

inFileB = 'IN/stations_full.csv' #change to stations
csvB = list(readCsv(inFileB))
csvX = readCsv(inFileB)

csvDivide = len(csvB)/100

def pullForecast():
    with open(inFileB, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        idNo_array = [row[0] for row in spamreader]

        fMain = csv.writer(open("IN/" + strftime("%Y%m%d") + "/wunderground.csv", "wb+"))
        fMain.writerow(['stationId',
                        'epoch',
                        'period',
                        'icon',
                        'icon_url'])

        for row in itertools.islice(idNo_array, 0, csvDivide, 1):
            idNo = ', '.join([row])
            key_no = '3d776fe610a62562'
            inUrl = ('http://api.wunderground.com/api/%s/forecast/q/pws:%s.json?bestfct=1') % (key_no, idNo)
            response = urllib.urlopen(inUrl)

            fJson = json.load(response)

            for no in xrange(len(fJson['forecast']['simpleforecast']['forecastday'])):
                fMain.writerow([idNo,
                                fJson['forecast']['simpleforecast']['forecastday'][no]['date']['epoch'],
                                fJson['forecast']['simpleforecast']['forecastday'][no]['period'],
                                fJson['forecast']['simpleforecast']['forecastday'][no]['icon'],
                                fJson['forecast']['simpleforecast']['forecastday'][no]['icon_url']])
            response.close()

pullForecast()

'''
def pulldata2():
    with open(inFileB, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')

        for row in itertools.islice(spamreader, csvDivide+1, csvDivide*2, 1):
            print "result2" + (', '.join(row))

def pulldata3():
    with open(inFileB, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')

        for row in itertools.islice(spamreader, (csvDivide*2)+1, csvDivide*3, 1):
            print "result3" + (', '.join(row))

threads = []


t = threading.Thread(target=pulldata1)
threads.append(t)
t.start()
t.join()

l = threading.Thread(target=pulldata1)
threads.append(l)
l.start()
l.join()

m = threading.Thread(target=pulldata1)
threads.append(m)
m.start()
m.join()

'''


'''
root = Tk()
def countdown(n, bps, root):
    if n == 0:
        root.destroy() # exit mainloop
    else:
        print(n)
        root.after(1000 / bps, countdown, n - 1, bps, root)  # repeat the call

root = Tk()
root.withdraw() # don't show the GUI window
root.after(4000, apiJsonCsv(inUrl)) # call foo() in 4 seconds
root.after(0, countdown, 10, 2, root)  # show that we are alive
root.mainloop()
print("done")
'''

#print csvB[0]

writer = []

for row in csvB:
    id_na = writer.append(row[0])



'''
##Pull hourly data from wunderground api
def pulldataHourly():
    with open(inFileB, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')

        #print [row[0] for row in spamreader]
        idNo_array = [row[0] for row in spamreader]
        #print idNo_array

        for row in itertools.islice(idNo_array, 0, csvDivide, 1):
            print ', '.join([row])

            key_no = '3d776fe610a62562'
            inUrl = ('http://api.wunderground.com/api/%s/hourly/q/pws:%s.json?bestfct=1') % (key_no, row)
            print inUrl
            def apiJsonCsv(inUrl):
                fMain = csv.writer(open("IN/" + strftime("%Y%m%d") + "/wunderground.csv", "wb+"))
                fMain.writerow(['stationId',
                                'epoch',
                                'civil',
                                'temp_metric',
                                'condition',
                                'fctcode'])

                response = urllib.urlopen(inUrl)
                fJson = json.load(response)

                for no in xrange(len(fJson['hourly_forecast'])):
                    fMain.writerow([id_no, fJson['hourly_forecast'][no]['FCTTIME']['epoch'],
                                    fJson['hourly_forecast'][no]['FCTTIME']['civil'],
                                    fJson['hourly_forecast'][no]['temp']['metric'],
                                    fJson['hourly_forecast'][no]['condition']])

                    # print fJson['hourly_forecast'][1]['FCTTIME']['epoch']
                    # print fJson['hourly_forecast'][1]['FCTTIME']['civil']
                    # print fJson['hourly_forecast'][1]['temp']['metric']
                    # print fJson['hourly_forecast'][1]['condition']
                    # print fJson['hourly_forecast'][1]['fctcode']
                    # print len(fJson)

                response.close()


        apiJsonCsv(inUrl)
pulldataHourly()


for row in csvB:
    #id_no = row[0]
    key_no = '6bd6b559a24c1785'

    id_no = "IGREENFO2"
    inUrl = 'http://api.wunderground.com/api/' + key_no + '/hourly/q/pws:' + id_no + '.json?bestfct=1'

    def apiJsonCsv(inUrl):

        fMain = csv.writer(open("IN/" + strftime("%Y%m%d") + "/wunderground.csv", "wb+"))
        fMain.writerow(['stationId',
                        'epoch',
                        'civil',
                        'temp_metric',
                        'condition',
                        'fctcode'])


        response = urllib.urlopen(inUrl)
        fJson = json.load(response)

        for no in xrange(len(fJson['hourly_forecast'])):

            fMain.writerow([id_no, fJson['hourly_forecast'][no]['FCTTIME']['epoch'],
                            fJson['hourly_forecast'][no]['FCTTIME']['civil'],
                            fJson['hourly_forecast'][no]['temp']['metric'],
                            fJson['hourly_forecast'][no]['condition']])

            # print fJson['hourly_forecast'][1]['FCTTIME']['epoch']
            # print fJson['hourly_forecast'][1]['FCTTIME']['civil']
            # print fJson['hourly_forecast'][1]['temp']['metric']
            # print fJson['hourly_forecast'][1]['condition']
            # print fJson['hourly_forecast'][1]['fctcode']
            # print len(fJson)

        response.close()


#apiJsonCsv(inUrl)



def main():

    inFileB = 'IN/' + strftime("%Y%m%d") + '/validation/bus_validated.csv'
    outFileB= 'OUT/' + strftime("%Y%m%d") + '/validation/bus_dirty.ttl'

    csvB=readCsv(inFileB)
    busline_store = plugin.get('IOMemory', Store)()
    bus_g= Graph(busline_store)

    prefixes=definePrefixes()

    print('Binding Prefixes')
    bindingPrefixes(bus_g, prefixes)

    print('Creating graph-Bus...')
    for row in csvB:
        lstData = getBusData(row)
        createBusGraph(lstData,bus_g).serialize(outFileB,format='turtle')

    print ('DONE - Bus rdfy')

if __name__ == "__main__":
    main();
'''



