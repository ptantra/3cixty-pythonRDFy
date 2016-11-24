import imp, csv, urllib, os, json
import pandas as pd
from pandas import merge, DataFrame
from time import strftime
from bs4 import BeautifulSoup
#from common import urlRetrieve


#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists("subwayModule/IN/"+ strftime("%Y%m%d")):
    os.makedirs(strftime("subwayModule/IN/"+ strftime("%Y%m%d")))

#imp.load_source('common','commonModule/transportCommon.py')
#imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')

#INSERT TFL API UNIQUE API KEY AND APP NUMBER BELOW
key_no = "1739d498d997e956a2b80c62a8948ff0"
id_no = "5ee709d5"

inUrl = "http://data.tfl.gov.uk/tfl/syndication/feeds/stations.kml?app_id=" + id_no + "&app_key=" + key_no
outXml = "subwayModule/IN/subway-stations.xml"

inputfile = outXml
with open(inputfile, 'r') as f:
  soup = BeautifulSoup(f, "lxml")

'''
f = csv.writer(open("subwayModule/IN/" + strftime("%Y%m%d") +"/" + "tfl_subway.csv", "wb+"))
f.writerow(["stationName",
            "lat",
            "lon",
            "wktgeom",
            "style",
            "streetAddress",
            "locality",
            "postcode"])

for node in soup.select('placemark'):
    for item in node.select('name'):
        for x in node.select('coordinates'):
            for y in node.select('description'):
                for z in node.select('styleurl'):
                    f.writerow([item.string,
                                x.string.split(',')[0],
                                x.string.split(',')[1],
                                'POINT(' + x.string.split(',')[0] + "," + x.string.split(',')[1] +')',
                                z.string.replace('#','').replace("Style",''),
                                y.string.split(',')[-3],
                                y.string.split(',')[-2],
                                y.string.split(',')[-1]])

    #print postcode
    #print list
#return x
'''

print "retrieve subway stations - done"

lineId = ['bakerloo',
          'central',
          'circle',
          'district',
          'jubilee',
          'metropolitan',
          'northern',
          'piccadilly',
          'victoria'
          ]#'waterloo&20%26&20city'

#Bakerloo, Central, Circle, District, Hammersmith & City, Jubilee, Metropolitan, Northern, Piccadilly, Victoria, Waterloo & City

for lineNo in xrange(len(lineId)):
    print lineNo

    inUrlLines = 'https://api.tfl.gov.uk/Line/' + lineId[lineNo] +'/StopPoints?app_id=' + id_no + '&app_key=' + key_no
    outXmlLines = "subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_"+lineId[1] +".xml"

    print inUrlLines

    def apiJsonCsv(inUrlLines):
        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)


        fMain = csv.writer(open("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + ".csv", "wb+"))
        fMain.writerow(['stationNaptan',
                        'stationName',
                        "stopType",
                        'lat',
                        'lon',
                        'lineName'])

        for fJson in fJson:
            #print fJson
            fMain.writerow([fJson['naptanId'],
                            fJson['commonName'],
                            fJson['stopType'],
                            fJson['lat'],
                            fJson['lon'],
                            lineId[1]
                            ])
        response.close()

        fWifi= csv.writer(open("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_wifi.csv", "wb+"))
        fWifi.writerow(['wifi'])

        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)
        for fJson in fJson:

            for no in xrange(len(fJson["additionalProperties"])):
                if fJson["additionalProperties"][no]['key'] == 'WiFi':
                    fWifi.writerow([fJson["additionalProperties"][no]['value']])

        response.close()

        fZone = csv.writer(open("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_zone.csv", "wb+"))
        fZone.writerow(['zone'])

        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)
        for fJson in fJson:

            for no in xrange(len(fJson["additionalProperties"])):
                if fJson["additionalProperties"][no]['key'] == 'Zone':
                    fZone.writerow([fJson["additionalProperties"][no]['value']])

        response.close()

        fAddress = csv.writer(open("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_address.csv", "wb+"))
        fAddress.writerow(['address'])

        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)
        for fJson in fJson:

            for no in xrange(len(fJson["additionalProperties"])):
                if fJson["additionalProperties"][no]['key'] == 'Address':
                    fAddress.writerow([fJson["additionalProperties"][no]['value']])

        response.close()

    apiJsonCsv(inUrlLines)

    lineId = ['bakerloo',
              'central',
              'circle',
              'district',
              'jubilee',
              'metropolitan',
              'northern',
              'piccadilly',
              'victoria']

    subway = DataFrame(pd.read_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + ".csv"))
    subwayWifi = DataFrame(pd.read_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_wifi.csv"))
    subwayZone = DataFrame(pd.read_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_zone.csv"))
    subwayAddress = DataFrame(pd.read_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_address.csv"))

    join = subway.join([subwayWifi, subwayZone, subwayAddress])
    print join
    join.to_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_output.csv", index=False)




