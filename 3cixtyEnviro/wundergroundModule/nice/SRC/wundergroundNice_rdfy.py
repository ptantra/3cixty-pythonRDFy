__author__ = 'patrick'

import csv, uuid, pyproj, random, string, time, sys, fileinput, os

from rdflib import URIRef, Literal, Namespace, plugin, Graph, BNode, collection, ConjunctiveGraph
from rdflib.store import Store
from datetime import datetime, date, time
from time import time

from time import strftime

#os.chdir('Z:/3cixty/3cixty_160822/3cixtyEnviro/wundergroundModule/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/nice/') # @patrick CASA Mac setup
print os.getcwd()

def readCsv(inputfile):
    try:
        f = open(inputfile, 'rU')
        rf = csv.reader(f, delimiter=';')
        return rf
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        raise

def getUid(deviceId, weatherComponent, weatherTimestamp, weatherPublisher):
    publisher= Namespace(weatherPublisher)
    idencode = deviceId.encode('UTF-8') + str(weatherComponent) + str(weatherTimestamp)#str(datetime.strftime(recordedAt, '%d/%m/%Y %H:%M'))
    uid = uuid.uuid5(publisher, idencode)
    return uid

def definePrefixes():
    prefixes = {'dc': 'http://purl.org/dc/elements/1.1/',
                'dct': 'http://purl.org/dc/terms/',
                'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
                'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
                'geosparql': 'http://www.opengis.net/ont/geosparql#',
                'locn': 'http://www.w3.org/ns/locn#',
                'owl': 'http://www.w3.org/2002/07/owl#',
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                'schema': 'http://schema.org/',
                'ssn':'http://www.w3.org/ns/ssn/',
                'xsd':'http://www.w3.org/2001/XMLSchema#'}
    return prefixes

def bindingPrefixes(g, prefixes):
    for key in prefixes:
        g.bind(key, prefixes[key])
    return g

def createWeatherDeviceId(getUid):
    weatherId = URIRef("http://data.linkedevents.org/environment/nice/wunderground/observation/" + Literal(getUid))
    return weatherId

def createArea(weatherDeviceCode):
    area = URIRef('http://data.linkedevents.org/environment/nice/wunderground/deviceId/' + Literal(weatherDeviceCode))
    return area

def createGeom(weatherDeviceCode):
    geom = createArea(weatherDeviceCode) + '/geometry'
    return geom

def createSensor(weatherDeviceCode):
    geom = createArea(weatherDeviceCode) + '/sensor'
    return geom

def createAddress(weatherDeviceCode):
    address = createArea(weatherDeviceCode) + '/address'
    return address


def weatherUid(deviceId, weatherUrl):
    publisher = Namespace(weatherUrl)
    idencode = deviceId.encode('UTF-8')
    uid = uuid.uuid5(publisher, idencode)
    return uid

def getWeatherData(row):

    publisher = URIRef("https://www.wunderground.com")
    pwsId = Literal(str(row[0]))
    deviceAddress = Literal(str(row[2]))
    deviceLocality = Literal(str(row[1]))
    lat = row[3]
    lon = row[4]
    deviceGeom= "POINT (" + str(lat) + " " + str(lon) + ")"
    deviceForecast = URIRef(("http://api.wunderground.com/api/[API-KEY]/forecast/q/pws:%s.json?bestfct=1") % row[0])
    deviceHourly = URIRef(("http://api.wunderground.com/api/[API-KEY]/hourly/q/pws:%s.json?bestfct=1") % row[0])

    forecastUid = weatherUid(row[0], deviceForecast)
    hourlyUid = weatherUid(row[0], deviceHourly)

    lst = [pwsId,#0
           deviceAddress,#1
           deviceLocality,#2
           lat,#3
           lon,#4
           deviceGeom,#5
           deviceForecast,#6
           deviceHourly,#7
           publisher,#8
           forecastUid,#9
           hourlyUid]#10

    return lst

def createWeatherGraph(arg, g):
    dc = Namespace('http://purl.org/dc/elements/1.1/')
    dct = Namespace('http://purl.org/dc/terms/')
    dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
    geo = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
    geosparql = Namespace("http://www.opengis.net/ont/geosparql#")
    locn = Namespace("http://www.w3.org/ns/locn#")
    rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
    schema = Namespace("http://schema.org/")
    ssn = Namespace('http://www.w3.org/ns/ssn/')
    xsd = Namespace('http://www.w3.org/2001/XMLSchema#')

    area = createArea(arg[0])
    geom = createGeom(arg[0])
    address = createAddress(arg[0])
    forecast = createWeatherDeviceId(arg[9])
    hourly = createWeatherDeviceId(arg[10])


    g.add((area, rdf.type, ssn.sensingDevice))
    g.add((area, rdfs.label, Literal(arg[0])))
    g.add((area, dc.publisher, URIRef(arg[8])))
    g.add((area, ssn.hasLocation, address))
    #g.add((area, schema.location, address))
    g.add((area, ssn.observationResult, forecast))#linksToRealtimedata
    g.add((area, ssn.hasRegion, geom))


    g.add((geom, rdf.type, geo.Point))
    g.add((geom, rdf.type, dul.spaceRegion))##QUESTION USE BOTH geo.point and dul.spaceRegion in triplet ?
    g.add((geom, geo.lat, Literal(arg[3], datatype=xsd.placeholder)))
    g.add((geom, geo.long, Literal(arg[4], datatype=xsd.placeholder)))
    g.add((geom, locn.geometry, Literal(arg[5], datatype=geosparql.wktLiteral)))


    g.add((address, ssn.isLocationOf, area))
    g.add((address, rdf.type, schema.PostalAddress ))
    g.add((address, schema.streetAddress, Literal(arg[1])))
    g.add((address, locn.address, Literal(arg[1] + ", " + arg[2])))
    g.add((address, schema.addressLocality, Literal(arg[2])))

    prefixes=definePrefixes()
    bindingPrefixes(g, prefixes)

    return g

def main():

    inFile = 'DATA/FEEDS/pws_nice.csv'
    outFile = 'DATA/pws_nice_dirty.ttl'

    csv = readCsv(inFile)
    next(csv, None)  # FILE WITH HEADERS

    store = plugin.get('IOMemory', Store)()
    g = Graph(store)

    prefixes = definePrefixes()
    print('Binding Prefixes')
    bindingPrefixes(g, prefixes)

    print('Creating graph-environment...')  # AMENDED

    for row in csv:
        lstData = getWeatherData(row)
        createWeatherGraph(lstData, g).serialize(outFile, format='turtle')

    print 'DONE creating wunderground graph'

if __name__ == "__main__":
    main()
