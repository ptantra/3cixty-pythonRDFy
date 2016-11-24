import imp, csv, urllib, os, json
import pandas as pd
from pandas import merge, DataFrame, ordered_merge
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
'''
for lineNo in xrange(len(lineId)):
    print lineNo

    inUrlLines = 'https://api.tfl.gov.uk/Line/' + lineId[lineNo] +'/StopPoints?app_id=' + id_no + '&app_key=' + key_no
    outXmlLines = "subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_"+lineId[lineNo] +".xml"

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
                        'line_'+lineId[lineNo]])

        for fJson in fJson:
            #print fJson
            fMain.writerow([fJson['naptanId'],
                            fJson['commonName'],
                            fJson['stopType'],
                            fJson['lat'],
                            fJson['lon'],
                            lineId[lineNo]
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
    #print join
    join.to_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[lineNo] + "_output.csv", index=False)
'''
######


bakerloo = DataFrame(pd.read_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[0] + "_output.csv"))
central = DataFrame(pd.read_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[1] + "_output.csv"))
picadilly = DataFrame(pd.read_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + lineId[7] + "_output.csv"))


om = ordered_merge(central, picadilly, fill_method='ffill', left_by='stationNaptan').drop_duplicates()
print om
om.to_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + "_OM.csv", index=False)



print bakerloo.index

frames = bakerloo.append([central, picadilly], ignore_index=True)

frames.drop_duplicates(['stationNaptan',
                        'stationName',
                        "stopType",
                        'lat',
                        'lon', 'wifi', 'zone', 'address'], keep='last')

#frames = frames.drop_duplicates()



'''
test = central.join(picadilly, on=['stationNaptan',
                        'stationName',
                        "stopType",
                        'lat',
                        'lon', 'wifi', 'zone', 'address'])

print test
'''
'''
frames = pd.concat([central, picadilly], axis=1, index = "stationNaptan", join = "inner")

frames2 = merge(picadilly, central, how='left', on=['stationNaptan', 'stationName', "stopType",'lat','lon', 'wifi', 'zone', 'address'], copy=False)
'''



#print frames
frames.to_csv("subwayModule/IN/"+ strftime("%Y%m%d") +"/subwayLine_" + "_TEST.csv", index=False)




