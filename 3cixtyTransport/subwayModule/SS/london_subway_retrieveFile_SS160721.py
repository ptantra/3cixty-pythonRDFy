import imp, csv, urllib, os, json
import pandas as pd
from pandas import merge, DataFrame
from time import strftime
from bs4 import BeautifulSoup
#from common import urlRetrieve


#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/') # @patrick CASA Mac setup
print os.getcwd()

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

f = csv.writer(open("subwayModule/IN/tfl_subway" + strftime("%Y%m%d") + ".csv", "wb+"))
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

print "retrieve subway stations - done"


lineId = ['bakerloo',
          'central',
          'circle',
          'district',
          'hammersmith & city',
          'jubilee',
          'metropolitan',
          'northern',
          'piccadilly',
          'victoria',
          'waterloo&20%26&20city']

#Bakerloo, Central, Circle, District, Hammersmith & City, Jubilee, Metropolitan, Northern, Piccadilly, Victoria, Waterloo & City

inUrlLines = 'https://api.tfl.gov.uk/Line/' + lineId[1] +'/StopPoints?app_id=' + id_no + '&app_key=' + key_no
outXmlLines = "subwayModule/IN/subway-lines.xml"

print inUrlLines



def apiJsonCsv(inUrlLines):
    response = urllib.urlopen(inUrlLines)
    fJson = json.load(response)


    fMain = csv.writer(open("subwayModule/IN/tfl_subwayLines" + strftime("%Y%m%d") + ".csv", "wb+"))
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
                        lineId[9]
                        ])
    response.close()

    fWifi= csv.writer(open("subwayModule/IN/tfl_subwayLines_Wifi" + strftime("%Y%m%d") + ".csv", "wb+"))
    fWifi.writerow(['wifi'])

    response = urllib.urlopen(inUrlLines)
    fJson = json.load(response)
    for fJson in fJson:

        for no in xrange(len(fJson["additionalProperties"])):
            if fJson["additionalProperties"][no]['key'] == 'WiFi':
                fWifi.writerow([fJson["additionalProperties"][no]['value']])

    response.close()

    fZone = csv.writer(open("subwayModule/IN/tfl_subwayLines_Zone" + strftime("%Y%m%d") + ".csv", "wb+"))
    fZone.writerow(['zone'])

    response = urllib.urlopen(inUrlLines)
    fJson = json.load(response)
    for fJson in fJson:

        for no in xrange(len(fJson["additionalProperties"])):
            if fJson["additionalProperties"][no]['key'] == 'Zone':
                fZone.writerow([fJson["additionalProperties"][no]['value']])

    response.close()

    fAddress = csv.writer(open("subwayModule/IN/tfl_subwayLines_address" + strftime("%Y%m%d") + ".csv", "wb+"))
    fAddress.writerow(['address'])

    response = urllib.urlopen(inUrlLines)
    fJson = json.load(response)
    for fJson in fJson:

        for no in xrange(len(fJson["additionalProperties"])):
            if fJson["additionalProperties"][no]['key'] == 'Address':
                fAddress.writerow([fJson["additionalProperties"][no]['value']])

    response.close()









    ##############################combine ... ????? FAILED ATTEMPT

    '''
    f1 = open("subwayModule/IN/tfl_subwayLines" + strftime("%Y%m%d") + ".csv", "r")  # open input file for reading

    with open('subwayModule/IN/tfl_subwayLines_out.csv', 'wb') as f:  # output csv file
        writer = csv.writer(f)
        with open("subwayModule/IN/tfl_subwayLines_Wifi" + strftime("%Y%m%d") + ".csv", 'r') as csvfile:  # input csv file
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                row[0] = f1.readline()  # edit the 8th column
                writer.writerow(row)

    f1.close()
    '''

    ######################
    '''
    fWifi = csv.writer(open("subwayModule/IN/tfl_subwayLines_Wifi" + strftime("%Y%m%d") + ".csv", "wb+"))
    fWifi.writerow(['wifi'])

    response = urllib.urlopen(inUrlLines)
    fJson = json.load(response)
    for fJson in fJson:

        for no in xrange(len(fJson["additionalProperties"])):
            if fJson["additionalProperties"][no]['key'] == 'WiFi':
                fWifi.writerow([fJson["additionalProperties"][no]['value']])

    #with open("subwayModule/IN/tfl_subwayLines" + strftime("%Y%m%d") + ".csv", 'wb') as fileNew:
    '''
    '''
    with open("subwayModule/IN/tfl_subwayLines" + strftime("%Y%m%d") + ".csv",  'r') as fileTransform:
        reader = csv.reader(fileTransform, delimiter=',')
        print reader
        for js in fx:
            #print js
            for no in xrange(len(js["additionalProperties"])):
                print xrange(len(js["additionalProperties"]))
                for row in reader :
                    print row
                    if js["additionalProperties"][no]['key'] == 'WiFi':
                        #flines.writerow([js["additionalProperties"][no]['value']])
                        row[6] = [js["additionalProperties"][no]['value'].readline()]
                        print row[6]
                        flines.writerow(row)
    '''


    #print fx

    '''

    for fx in fx:
        flines.writerow([fx["naptanId"],
                         fx["commonName"],
                         fx["stopType"],
                         fx['lat'],
                         fx['lon'],
                         lineId[9]
                         ])

    for js in fx:
        for no in xrange(len(js["additionalProperties"])):
            if js["additionalProperties"][no]['key'] == 'WiFi':
                flines.writerow(js["additionalProperties"][no]['value'])

    for js in fx:
        for no in xrange(len(js["additionalProperties"])):
            if js["additionalProperties"][no]['key'] == 'WiFi':
                print 'wifi=', js["additionalProperties"][no]['value']
            if js["additionalProperties"][no]['key'] == 'Toilets':
                print 'toilets=',js["additionalProperties"][no]['value']
            if js["additionalProperties"][no]['key'] == 'Zone':
                print 'zone=',js["additionalProperties"][no]['value']
            if js["additionalProperties"][no]['key'] == 'Address':
                print 'address=',js["additionalProperties"][no]['value']




    for fx in fx:
        flines.writerow([fx["naptanId"],
                         fx["commonName"],
                         fx["stopType"],
                         fx['lat'],
                         fx['lon'],
                         lineId[9],
                         ])
    '''

    '''
    flines.writerow(["stationNaptan",
                "commonName",
                "stopType",
                "wifi_3",
                "toilets_5",
                "zone_6",
                "lifts_10",
                "carpark_12"])

    for fx in fx:
        flines.writerow([fx["naptanId"],
                    fx["commonName"],
                    fx["stopType"],
                    fx["additionalProperties"][3]['value'],
                    fx["additionalProperties"][5]['value'],
                    fx["additionalProperties"][6]['value'],
                    fx["additionalProperties"][10]['value'],
                    fx["additionalProperties"][12]['value']])
    '''

apiJsonCsv(inUrlLines)

subway = DataFrame(pd.read_csv("subwayModule/IN/tfl_subwayLines" + strftime("%Y%m%d") + ".csv"))
subwayWifi = DataFrame(pd.read_csv("subwayModule/IN/tfl_subwayLines_Wifi" + strftime("%Y%m%d") + ".csv"))
merged = merge(subway, subwayWifi, left_index=True, right_index=True, how= 'right')
print merged
#merged.to_csv("subwayModule/IN/tfl_subwayOutput.csv", index=False)




