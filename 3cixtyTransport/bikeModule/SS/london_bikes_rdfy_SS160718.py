'''A python script converting raw bicycle data from the TFL api into RDF. Outputs as a turtle file.
Workfklow: API -> JSON -> CSV -> RDF -> TTL'''

import urllib, json, csv, uuid, re, imp
from datetime import datetime
from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import readCsv, getUid, ConvertProj, definePrefixes, bindingPrefixes


pathf = "/Users/patrick/3cixty/IN/tfl/"
#pathf = "z:/3cixty/3cxity_160627/in/TFL/"

def apiJsonCsv(inputURL):
    response = urllib.urlopen(inputURL)
    x = json.load(response)

    f = csv.writer(open(pathf + "tfl_bikes" + strftime("%Y%m%d") + ".csv", "wb+"))
    f.writerow(["id",
                "url",
                "commonName",
                "placeType",
                "bikePointsNo",
                "timeModified",
                "nFilledDocks",
                "nEmptyDocks",
                "nTotalDocks",
                "lat",
                "lon"])

    for x in x:
        f.writerow([x["id"],
                    x["url"],
                    x["commonName"],
                    x["placeType"],
                    x["additionalProperties"][0]['value'],
                    x["additionalProperties"][0]['modified'],
                    x["additionalProperties"][6]['value'],
                    x["additionalProperties"][7]['value'],
                    x["additionalProperties"][8]['value'],
                    x["lat"],
                    x["lon"]])

    return x


'''
def convertTime(timeValue):
    if (re.findall(".", timeValue)): { #perhaps use find instead of findall ?
        datetime.strptime(timeValue, "%Y-%m-%dT%H:%M:%S.%fZ")
    }
    else: {
        datetime.strptime(timeValue, "%Y-%m-%dT%H:%M:%SZ")
    }
'''

def getBikeData(row):
    id = row[0]
    url= row[1]
    commonName = row[2]
    placeType = row[3]
    bikePointsNo = row[4]

    #timeModified= convertTime(row[5])
    #timeModified = datetime.strptime(row[5],"%Y-%m-%dT%H:%M:%SZ")
    #timeModified = row[5]

    timeModified = datetime.strptime(row[5],"%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M:%S")
    nFilledDocks = row[6]
    nEmptyDocks = row[7]
    nTotalDocks = row[8]
    lat=row[9]
    lon=row[10]

    lst = [id, #0
           url, #1
           commonName, #2
           placeType, #3
           bikePointsNo, #4
           timeModified, #5
           nFilledDocks, #6
           nEmptyDocks, #7
           nTotalDocks, #8
           lat, #9
           lon] #10
    return lst


def definePrefixes():

#Vocabularies   -- THIS SHOULD BE A CONSTRUCTED BASED ON THE A DICTONARY DEFINITION
    prefixes = {'dc': 'http://purl.org/dc/elements/1.1/',
                'dcterms':'http://purl.org/dc/terms/',
                'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
                'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
                'geom': 'http://geovocab.org/geometry#',
                'geosparql': 'http://www.opengis.net/ont/geosparql#','locationOnt': 'http://data.linkedevents.org/def/location#',
                'locn': 'http://www.w3.org/ns/locn#',
                'owl':'http://www.w3.org/2002/07/owl#',
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                'naptan':'http://transport.data.gov.uk/def/naptan/',
                'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                'schema':'http://schema.org/',
                'vcard': 'http://www.w3.org/2006/vcard/ns#',
                'xsd': 'http://www.w3.org/2001/XMLSchema#'}
    return prefixes

def bindingPrefixes(graphs,prefixes):
    for key in prefixes:
        graphs.bind(key, prefixes[key])
    return graphs

def createBikeGraph(arg, g):

    nspaces = readDict()

    schema = Namespace(nspaces.get('schema'))
    naptan = Namespace(nspaces.get('naptan'))
    owl = Namespace(nspaces.get('owl'))
    xsd = Namespace(nspaces.get('xsd'))
    rdfs = Namespace(nspaces.get('rdfs'))
    locationOnt = Namespace(nspaces.get('locationOnt'))
    geom = Namespace(nspaces.get('geom'))
    geo = Namespace(nspaces.get('geo'))
    geosparql = Namespace(nspaces.get('geosparql'))
    rdf = Namespace(nspaces.get('rdf'))
    dcterms = Namespace(nspaces.get('dcterms'))
    dul = Namespace(nspaces.get('dul'))
    locn = Namespace(nspaces.get('locn'))
    dc = Namespace(nspaces.get('dc'))

    bikeid = arg[4].encode('utf-8')
    bikeGUID = getUid(arg[4], arg[1], naptan)

    bikeLat, bikeLong = float(arg[9]), float(arg[10])
    bikeLats = str('{:f}'.format(bikeLat))
    bikeLongs = str('{:f}'.format(bikeLong))
    nTotalDocks = str(arg[8].encode('utf-8'))

    address = arg[2].split(',')
    bikeLabel = address[len(address) - 1].lstrip() + ' ' + str(bikeid)


    bikeGeometry = "POINT (" + str(bikeLat) + " " + str(bikeLong) + ")"
    #bikeAddress = Literal(re.sub(r'&(?![A-Za-z]+[0-9]*;|#[0-9]+;|#x[0-9a-fA-F]+;)', r'and',arg[2]))
    bikeAddress = Literal(arg[2])
    #a, b = bikeAddress.strip("\n ' '").split(',')
    bikeAddressStreet = Literal(bikeAddress.strip("\n ' '").split(',')[0])
    #bikeAddressLocality = Literal(bikeAddress.split(',')[1].replace(" ", "", 1))
    #bikeAddressLocality = Literal(bikeAddress.strip("\n ' '").split(','))


    bikeCreatedDate = arg[5]


    singleBike = createBikeParkID(bikeGUID)
    singleAddress = createAddress(bikeGUID)
    singleGeometry = createGeometry(bikeGUID)
    bikePublisher = URIRef('http://www.api.tfl.org.uk')
    bikeBusinessType = URIRef('http://data.linkedevents.org/kos/3cixty/bikestation')



    g.add((singleBike, rdf.type, dul.Place))
    g.add((singleBike, dcterms.identifier, Literal(arg[0])))
    g.add((singleBike, dcterms.description, Literal("London TFL Bike hire docks")))


    g.add((singleBike, rdfs.label, Literal(arg[2])))
    g.add((singleBike, locn.geometry, singleGeometry))
    g.add((singleBike, schema.location, singleAddress))




    g.add((singleBike, schema.dateCreated, Literal(bikeCreatedDate, datatype=xsd.dateTime)))
    g.add((singleBike, schema.url, URIRef("https://api-argon.tfl.gov.uk/Place/%s" % arg[0])))
    g.add((singleBike, locationOnt.nTotalDocks, Literal(nTotalDocks, datatype=xsd.int)))
    g.add((singleBike, dc.publisher, bikePublisher))
    g.add((singleBike, locationOnt.businessType, bikeBusinessType))



    g.add((singleGeometry, rdf.type, geo.Point))
    g.add((singleGeometry, locn.geometry, Literal(bikeGeometry, datatype=geosparql.wktLiteral)))
    g.add((singleGeometry, geo.lat, Literal(bikeLats, datatype=xsd.placeholder)))
    g.add((singleGeometry, geo.long, Literal(bikeLongs, datatype=xsd.placeholder)))



    g.add((singleAddress, rdf.type, schema.PostalAddress))
    g.add((singleAddress, dcterms.title, bikeAddress))
    g.add((singleAddress, schema.streetAddress, bikeAddressStreet))
    g.add((singleAddress, locn.address, bikeAddress))
    #g.add((singleAddress, schema.addressLocality, bikeAddressLocality))

    return g


def getUid(s, i, n):
    idencode = s.encode('utf-8') + str(i)
    uid = uuid.uuid5(n, idencode)
    return uid

def readDict(): #needed?
    dict = defaultdict(list)
    with open(pathf + 'dictionary_bikes.csv','rb') as f:
        r = csv.DictReader(f)
        for row in r:
            for (k,v) in row.items():
                dict[k]=v
    f.close()
    return dict

#import uuid


def createBikeParkID(bikeGUID):
    singlePark = URIRef("http://data.linkedevents.org/location/%s" % bikeGUID)
    return singlePark


def createGeometry(bikeGUID):
    singleGeometry = URIRef(('http://data.linkedevents.org/location/%s/geometry') % bikeGUID)
    return singleGeometry


def createAddress(bikeGUID):
    singleAddress = URIRef(('http://data.linkedevents.org/location/%s/address') % bikeGUID)
    return singleAddress


def main():

    url="https://api.tfl.gov.uk/BikePoint?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0" #url for bike api
    #apiJsonCsv(url) #json to csv conversion

    #inputCsv = pathf + "tfl_bikes" + strftime("%Y%m%d") + ".csv"
    inputCsv = pathf + "tfl_bikes" + strftime("%Y%m%d") + ".csv"
    outFile = pathf + "tfl_bikes" + strftime("%Y%m%d") + ".ttl"

    csvBike = readCsv(inputCsv) #create object from the resulting csv file

    next(csvBike) #skips the header

    bike_store = plugin.get('IOMemory', Store)()
    bike_g = Graph(bike_store)
    prefixes = definePrefixes()

    print('Binding Prefixes')
    bindingPrefixes(bike_g, prefixes)

    print('Creating graph-bike...')

    for row in csvBike: #loop through individual rows in the csv file **KEY**
        lstData= getBikeData(row)#activates the getBikeData() function **KEY**
        createBikeGraph(lstData, bike_g).serialize(outFile, format='turtle')


    print ('Done!!')

if __name__ == "__main__":
    main();

