import imp, csv, urllib, os, json, shutil
import pandas as pd
from pandas import merge, DataFrame, ordered_merge
from time import strftime
from bs4 import BeautifulSoup
#from common import urlRetrieve

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/ferryModule/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists("DATA/"):
    os.makedirs(strftime("DATA/"))

if not os.path.exists("DATA/"):
    os.makedirs(strftime("DATA/"))

#INSERT TFL API UNIQUE API KEY AND APP NUMBER BELOW
key_no = "1739d498d997e956a2b80c62a8948ff0"
id_no = "5ee709d5"

lineId = ['RB1',
          'RB2',
          'RB4',
          'RB5',
          'RB6',
          #'westminster-passenger-service-association',
          'woolwich-ferry']

for lineNo in xrange(len(lineId)):
    print lineNo

    inUrlLines = 'https://api.tfl.gov.uk/Line/' + lineId[lineNo] +'/StopPoints?app_id=' + id_no + '&app_key=' + key_no
    outXmlLines = "DATA/ferryLine_"+lineId[lineNo] +".xml"

    print inUrlLines

    def apiJsonCsv(inUrlLines):
        response = urllib.urlopen(inUrlLines)
        fJson = json.load(response)

        print fJson

        fMain = csv.writer(open("DATA/ferryLine_" + lineId[lineNo] + ".csv", "wb+"))
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

    apiJsonCsv(inUrlLines) #activate function

    lineId = ['RB1',#0
          'RB2',#1
          'RB4',#2
          'RB5',#3
          'RB6',#4
          #'westminster-passenger-service-association',#5
          'woolwich-ferry']#6

    ferry = DataFrame(pd.read_csv("DATA/ferryLine_" + lineId[lineNo] + ".csv"))
    #print join
    ferry.to_csv("DATA/ferryLine_" + lineId[lineNo] + "_output.csv", index=False)

rb1 = DataFrame(
    pd.read_csv("DATA/ferryLine_" + lineId[0] + "_output.csv"))
rb2 = DataFrame(
    pd.read_csv("DATA/ferryLine_" + lineId[1] + "_output.csv"))
rb4 = DataFrame(
    pd.read_csv("DATA/ferryLine_" + lineId[2] + "_output.csv"))
rb5 = DataFrame(
    pd.read_csv("DATA/ferryLine_" + lineId[3] + "_output.csv"))
rb6 = DataFrame(
    pd.read_csv("DATA/ferryLine_" + lineId[4] + "_output.csv"))
#westminsterPassenger = DataFrame(
    #pd.read_csv("IN/ferryLine_" + lineId[5] + "_output.csv"))
woolwichFerry= DataFrame(
    pd.read_csv("DATA/ferryLine_" + lineId[5] + "_output.csv"))

lines = rb1.append([rb2, rb4,
                    rb5,
                         rb6,
                    #westminsterPassenger,
                    woolwichFerry], ignore_index=True)

lines.to_csv("./DATA/ferry.csv", index=False)

print lines

#shutil.rmtree("ferryModule/IN/"+ strftime("%Y%m%d")) #declutter, remove all temporary files containing line information and metadata. Comment to scrutinise content.






