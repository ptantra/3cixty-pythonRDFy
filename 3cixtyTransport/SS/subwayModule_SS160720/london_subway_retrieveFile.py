import imp, csv, urllib
from time import strftime
from bs4 import BeautifulSoup
#from common import urlRetrieve

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')

inUrl = "http://data.tfl.gov.uk/tfl/syndication/feeds/stations.kml?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0"
outXml = "/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/IN/subway-stations.xml"


inputfile = outXml
with open(inputfile, 'r') as f:
  soup = BeautifulSoup(f, "lxml")

f = csv.writer(open("./" + "IN/tfl_subway" + strftime("%Y%m%d") + ".csv", "wb+"))
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


lineId = 'central'

inUrlLines = 'https://api.tfl.gov.uk/Line/' + lineId +'/StopPoints?app_id=&app_key='
outXmlLines = "/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/IN/subway-lines.xml"

def apiJsonCsv(inUrlLines):
    response = urllib.urlopen(inUrlLines )
    x = json.load(response)

    flines = csv.writer(open(pathf + "IN/tfl_subwayLines" + strftime("%Y%m%d") + ".csv", "wb+"))
    flines.writerow(["id",
                "commonName",
                "placeType",
                "wifi",
                "toilets",
                "lifts",
                "carpark",
                "whatever",
                "line1",
                "line2"])

    for fx in fx:
        flines.writerow([fx["id"],
                    fx["commonName"],
                    fx["placeType"],
                    fx["additionalProperties"][0]['value'],
                    fx["additionalProperties"][1]['value'],
                    fx["additionalProperties"][6]['value'],
                    fx["additionalProperties"][7]['value'],
                    fx["additionalProperties"][8]['value'],
                    fx["lines"][1]['name'],
                    fx["lines"][2]['name']])

    print fx

    return fx



