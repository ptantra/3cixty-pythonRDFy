__author__ = 'patrick'

import csv, uuid, pyproj, random, string, time, sys, fileinput, os

from rdflib import URIRef, Literal, Namespace, plugin, Graph, BNode, collection, ConjunctiveGraph
from rdflib.store import Store
from datetime import datetime, date, time
from time import time

from time import strftime

#os.chdir('Z:/3cixty/3cixty_160822/3cixtyEnviro/wundergroundModule/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/') # @patrick CASA Mac setup
print os.getcwd()


def readCsv(inputfile):
    try:
        f = open(inputfile, 'rU')
        rf = csv.reader(f, delimiter=',')
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
                'envo': 'http://purl.obolibrary.org/obo/#',
                'foaf': 'http://xmlns.com/foaf/0.1/',
                'geonames': 'http://www.geonames.org/ontology',
                'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
                'geom': 'http://geovocab.org/geometry#',
                'gn':'http://www.geonames.org/ontology/#',
                'gr': 'http://purl.org/goodrelations/v1#',
                'geosparql': 'http://www.opengis.net/ont/geosparql#',
                'locationOnt': 'http://data.linkedevents.org/def/location#',
                'locationRes': 'http://data.linkedevents.org/location/',
                'locn': 'http://www.w3.org/ns/locn#',
                'owl': 'http://www.w3.org/2002/07/owl#',
                'qb':'http://purl.org/linked-data/cube#',
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                'schema': 'http://schema.org/',
                'sdmx_attribute':'http://purl.org/linked-data/sdmx/2009/attribute#',
                'ssn':'http://purl.oclc.org/NET/ssnx/ssn#',
                'time':'http://www.w3.org/2006/time#',
                'time':'http://www.w3.org/TR/owl-time#',
                'xsd':'http://www.w3.org/2001/XMLSchema#'}
    return prefixes

def bindingPrefixes(g, prefixes):
    for key in prefixes:
        g.bind(key, prefixes[key])
    return g

def createWeatherDeviceId(getUid):
    weatherId = URIRef("http://data.linkedevents.org/environment/London/wunderground/observation/" + Literal(getUid))
    return weatherId

def createArea(weatherDeviceCode):
    area = URIRef('http://data.linkedevents.org/environment/London/wunderground/deviceId/' + Literal(weatherDeviceCode))
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
    deviceGeom= "POINT(" + str(lat) + " " + str(lon) + ")"
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
    dct = Namespace('http://purl.org/dc/terms/')
    dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    geosparql = Namespace("http://www.opengis.net/ont/geosparql#")
    locationOnt = Namespace("http://data.linkedevents.org/def/location#")
    locn = Namespace("http://www.w3.org/ns/locn#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    schema = Namespace("http://schema.org/")
    ssn = Namespace('http://purl.oclc.org/NET/ssnx/ssn#')
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

    area = createArea(arg[0])
    geom = createGeom(arg[0])
    address = createAddress(arg[0])
    forecast = createWeatherDeviceId(arg[9])
    hourly = createWeatherDeviceId(arg[10])

    deviceBusinessType = URIRef('http://data.linkedevents.org/kos/wunderground/weatherstation')

    g.add((area, rdf.type, ssn.sensingDevice))
    g.add((area, rdf.type, dul.Place))
    g.add((area, rdfs.label, Literal(arg[0])))
    g.add((area, locationOnt.businessType, deviceBusinessType))
    g.add((area, dct.publisher, URIRef(arg[8])))
    g.add((area, geo.location, geom))
    g.add((area, schema.location, address))
    g.add((area, ssn.hasPropery, forecast))
    #g.add((area, ssn.hasPropery, hourly))

    g.add((geom, rdf.type, geo.Point))
    g.add((geom, geo.lat, Literal(arg[3], datatype=xsd.placeholder)))
    g.add((geom, geo.lon, Literal(arg[4], datatype=xsd.placeholder)))
    g.add((geom, locn.geometry, Literal(arg[5], datatype=geosparql.wktLiteral)))

    g.add((address, rdf.type, schema.PostalAddress ))
    g.add((address, schema.streetAddress, Literal(arg[1])))
    g.add((address, locn.address, Literal(arg[1] + ", " + arg[2])))
    g.add((address, schema.addressLocality, Literal(arg[2])))

    #g.add((forecast, rdf.type, ssn.observation))
    #g.add((forecast, dct.description, Literal('weather forecast', lang='en')))
    #g.add((forecast, rdfs.comment, Literal('Returns a summary of the weather for the next 3 days.', lang='en')))
    #g.add((forecast, schema.url, URIRef(arg[6])))

    #g.add((hourly, rdf.type, ssn.observation))
    #g.add((hourly, dct.description, Literal('hourly', lang='en')))
    #g.add((hourly, rdfs.comment, Literal('Returns an hourly forecast for the next 36 hours immediately following the API request.',lang='en')))
    #g.add((hourly, schema.url, URIRef(arg[7])))

    prefixes=definePrefixes()
    bindingPrefixes(g, prefixes)

    return g

def main():

    inFile = "IN/"+ strftime("%Y%m%d") +"/validation/wunderground_validated.csv"
    outFile = "IN/"+ strftime("%Y%m%d") +"/wunderground_dirty.ttl"
    #inFile = "Z:/3cixty/3cixty_160816/IN/intel/icriQEOPsensors/merged_deviceData.csv"
    #outFile = "Z:/3cixty/3cixty_160816/IN/intel/icriQEOPsensors/icriQEOPsensorData" + "_" + strftime("%Y%m%d") + ".ttl"

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
