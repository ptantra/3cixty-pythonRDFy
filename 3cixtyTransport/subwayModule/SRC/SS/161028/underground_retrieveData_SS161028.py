import imp, csv, urllib, os, json, shutil
import pandas as pd
from pandas import merge, DataFrame, ordered_merge
from time import strftime
from bs4 import BeautifulSoup
#from common import urlRetrieve

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists("IN/"):
    os.makedirs(strftime("IN/"))

if not os.path.exists("IN/_"):
    os.makedirs(strftime("IN/_"))

#INSERT TFL API UNIQUE API KEY AND APP NUMBER BELOW
key_no = "1739d498d997e956a2b80c62a8948ff0"
id_no = "5ee709d5"

lineId = ['bakerloo',
          'central',
          'circle',
          'district',
          'hammersmith-city',
          'jubilee',
          'metropolitan',
          'northern',
          'piccadilly',
          'victoria',
          'waterloo-city',
          'tfl-rail',
          'dlr',
          'tram',
          'london-overground']

for lineNo in xrange(len(lineId)):
    print lineNo

    inUrlLines = 'https://api.tfl.gov.uk/Line/' + lineId[lineNo] +'/StopPoints?app_id=' + id_no + '&app_key=' + key_no
    outXmlLines = "IN/subwayLine_"+lineId[lineNo] +".xml"

    print inUrlLines

    def apiJsonCsv(inUrlLines):
        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)

        fMain = csv.writer(open("IN/subwayLine_" + lineId[lineNo] + ".csv", "wb+"))
        fMain.writerow(['stationNaptan',
                        'stationName',
                        "stopType",
                        'lat',
                        'lon',
                        'line'])

        for fJson in fJson:
            fMain.writerow([fJson['naptanId'],
                            fJson['commonName'],
                            fJson['stopType'],
                            fJson['lat'],
                            fJson['lon'],
                            lineId[lineNo]
                            ])
        response.close()

        fWifi= csv.writer(open("IN/subwayLine_" + lineId[lineNo] + "_wifi.csv", "wb+"))
        fWifi.writerow(['wifi'])

        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)
        for fJson in fJson:

            for no in xrange(len(fJson["additionalProperties"])):
                if fJson["additionalProperties"][no]['key'] == 'WiFi':
                    fWifi.writerow([fJson["additionalProperties"][no]['value']])

        response.close()

        fZone = csv.writer(open("IN/subwayLine_" + lineId[lineNo] + "_zone.csv", "wb+"))
        fZone.writerow(['zone'])

        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)
        for fJson in fJson:

            for no in xrange(len(fJson["additionalProperties"])):
                if fJson["additionalProperties"][no]['key'] == 'Zone':
                    fZone.writerow([fJson["additionalProperties"][no]['value']])

        response.close()

        fAddress = csv.writer(open("IN/subwayLine_" + lineId[lineNo] + "_address.csv", "wb+"))
        fAddress.writerow(['address'])

        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)
        for fJson in fJson:

            for no in xrange(len(fJson["additionalProperties"])):
                if fJson["additionalProperties"][no]['key'] == 'Address':
                    fAddress.writerow([fJson["additionalProperties"][no]['value'].replace("\r\n", "").replace("  ", "")])
                #if not fJson["additionalProperties"][no]['key'] == 'Address':
                 #   fAddress.writerow(['NA'])

        response.close()

    apiJsonCsv(inUrlLines) #activate function

    lineId = ['bakerloo',#0
              'central',#1
              'circle',#2
              'district',#3
              'hammersmith-city',#4
              'jubilee',#5
              'metropolitan',#6
              'northern',#7
              'piccadilly',#8
              'victoria',#9
              'waterloo-city',#10
              'dlr',#11
              'tfl-rail',#12
              'tram',
              'london-overground']#14

    subway = DataFrame(pd.read_csv("IN/subwayLine_" + lineId[lineNo] + ".csv"))
    subwayWifi = DataFrame(pd.read_csv("IN/subwayLine_" + lineId[lineNo] + "_wifi.csv"))
    subwayZone = DataFrame(pd.read_csv("IN/subwayLine_" + lineId[lineNo] + "_zone.csv"))
    subwayAddress = DataFrame(pd.read_csv("IN/subwayLine_" + lineId[lineNo] + "_address.csv"))

    join = subway.join([subwayWifi, subwayZone, subwayAddress])
    #print join
    join.to_csv("IN/subwayLine_" + lineId[lineNo] + "_output.csv", index=False)

bakerloo = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[0] + "_output.csv"))
central = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[1] + "_output.csv"))
circle = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[2] + "_output.csv"))
district = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[3] + "_output.csv"))
hammersmith_city = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[4] + "_output.csv"))
jubilee = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[5] + "_output.csv"))
metropolitan= DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[6] + "_output.csv"))
northern = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[7] + "_output.csv"))
picadilly = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[8] + "_output.csv"))
victoria =  DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[9] + "_output.csv"))
waterloo_city = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[10] + "_output.csv"))
dlr = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[11] + "_output.csv"))
tfl_rail = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[12] + "_output.csv"))
tram = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[13] + "_output.csv"))
london_overground = DataFrame(
    pd.read_csv("IN/subwayLine_" + lineId[14] + "_output.csv"))

lines = bakerloo.append([central, circle, district,
                         hammersmith_city, jubilee, metropolitan, northern, picadilly,
                         victoria, waterloo_city, tfl_rail], ignore_index=True)#london_overground,

#lines = bakerloo.append([central, circle, district, hammersmith_city, jubilee, metropolitan, northern, picadilly, victoria, waterloo_city, london_overground, tfl_rail, dlr, tram], ignore_index=True)

lines.to_csv("IN/subwayLine_" + "ALL.csv", index=False)
tram.to_csv("IN/tram_" + "ALL.csv", index=False)
dlr.to_csv("IN/dlr_" + "ALL.csv", index=False)
london_overground.to_csv("IN/overground_" + "ALL.csv", index=False)

print lines

#shutil.rmtree("IN/"+ strftime("%Y%m%d")) #declutter, remove all temporary files containing line information and metadata. Comment to scrutinise content.






