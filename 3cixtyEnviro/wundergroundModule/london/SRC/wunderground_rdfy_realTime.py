__author__ = 'patrick'

import csv, uuid, pyproj, random, string, time, sys, fileinput, os

from rdflib import URIRef, Literal, Namespace, plugin, Graph, BNode, collection, ConjunctiveGraph
from rdflib.store import Store
from datetime import datetime, date, time
from time import time

from time import strftime

#os.chdir('Z:/3cixty/3cixty_160822/3cixtyEnviro/wundergroundModule/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/london/') # @patrick CASA Mac setup
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
    idencode = deviceId.encode('UTF-8') + str(weatherComponent) + str(weatherTimestamp)#str(datet§ime.strftime(recordedAt, '%d/%m/%Y %H:%M'))
    uid = uuid.uuid5(publisher, idencode)
    return uid

def definePrefixes():
    prefixes = {'dct': 'http://purl.org/dc/terms/',
                'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
                'owl': 'http://www.w3.org/2002/07/owl#',
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                'ssn': 'http://www.w3.org/ns/ssn/',
                'xsd':'http://www.w3.org/2001/XMLSchema#'}

    return prefixes

def bindingPrefixes(g, prefixes):
    for key in prefixes:
        g.bind(key, prefixes[key])
    return g

def createWeatherDeviceId(getUid):
    weatherId = URIRef("http://data.linkedevents.org/environment/London/wunderground/observation/" + Literal(getUid))
    return weatherId

def weatherUid(deviceId, weatherUrl):
    publisher = Namespace(weatherUrl)
    idencode = deviceId.encode('UTF-8')
    uid = uuid.uuid5(publisher, idencode)
    return uid

def getWeatherData(row):

    pwsId = Literal(str(row[0]))
    deviceForecast = URIRef(("http://api.wunderground.com/api/[API-KEY]/forecast/q/pws:%s.json?bestfct=1") % row[0])

    timestamp = Literal(datetime.fromtimestamp(float(row[2])).strftime("%Y-%m-%dT%H:%M:%S"))
    condition = Literal(str(row[1]))

    forecastUid = weatherUid(row[0], deviceForecast)

    lst = [pwsId,#0
           deviceForecast,#1
           timestamp,#2
           condition,#3
           forecastUid]#4

    return lst

def createWeatherGraph(arg, g):
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    ssn = Namespace('http://www.w3.org/ns/ssn/')
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

    forecast = createWeatherDeviceId(arg[4])

    g.add((forecast, rdf.type, ssn.observation))
    g.add((forecast, ssn.property, Literal('weather condition', lang='en')))
    g.add((forecast, ssn.observationResultTime, Literal(arg[2], datatype=xsd.dateTime)))
    g.add((forecast, ssn.observationValue, Literal(arg[3], lang='en')))

    prefixes=definePrefixes()
    bindingPrefixes(g, prefixes)

    return g

def main():

    inFile = "DATA/forecast.csv"
    outFile = "DATA/forecast.ttl"
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
