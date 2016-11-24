__author__ = 'casa'
# -*- coding: utf-8 -*-

import csv, zipfile, uuid, pyproj, re, imp, os
from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import readCsv, getUid, ConvertProj, definePrefixes, bindingPrefixes, readDict

#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists("OUT/"):
    os.makedirs(strftime("OUT/"))
'''
def readCsv(inputfile):
    try:
          f=open(inputfile,'rU');
          rf=csv.reader(f,delimiter=',');
          return rf;
    except IOError as e:
         print ("I/O error({0}): {1}".format(e.errno, e.strerror))
         raise

def getUid(r0):
    naptan = Namespace("http://transport.data.gov.uk/def/naptan/")
    #objectID  = r1
    idencode=r0.encode('utf-8')
    uid=uuid.uuid5(naptan, idencode)
    return uid

def ConvertProj(lat,lon):
    Bng = pyproj.Proj(init='epsg:27700')
    Wgs84 = pyproj.Proj(init='epsg:4326')
    #print (lat+'-'+lon)
    wgsLon,wgsLat = pyproj.transform(Bng,Wgs84,lon, lat)
    return wgsLon,wgsLat

def definePrefixes():

#Vocabularies   -- THIS SHOULD BE A CONSTRUCTED BASED ON THE A DICTONARY DEFINITION
    prefixes = {'schema':'http://schema.org/',
        'naptan':'http://transport.data.gov.uk/def/naptan/',
        'owl':'http://www.w3.org/2002/07/owl#',
        'xsd': 'http://www.w3.org/2001/XMLSchema#',
        'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
        'vcard': 'http://www.w3.org/2006/vcard/ns#',
        'locationOnt': 'http://data.linkedevents.org/def/location#',
        'geom': 'http://geovocab.org/geometry#',
        'unknown': 'http://data.linkedevents.org/def/unknown#',
        'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
        'geosparql': 'http://www.opengis.net/ont/geosparql#',
        'sf': 'http://www.opengis.net/ont/sf#',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'transit': 'http://vocab.org/transit/terms/',
        'dcterms': 'http://purl.org/dc/terms/',
        'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
        'locn': 'http://www.w3.org/ns/locn#',
        'foaf': 'http://xmlns.com/foaf/0.1/',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'qb': 'http://purl.org/linked-data/cube#',
        'travel': 'http://3cixty.com/ontology#',
        'trans': 'http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/Transporte#'}
    return prefixes

def bindingPrefixes(graphs,prefixes):
    for key in prefixes:
        graphs.bind(key, prefixes[key])
    return graphs
'''

'''
def transfer(station,pathf):
    csv=readCsv(pathf+ 'IN' +'station_line.csv')
    if csv is not None:
        # Skip the headers
        next(csv, None)
        for row in csv:
            row=validateCol(row)
            if row[0]==station:
                row=filter(None, row[1:len(row)])
                return row
        #print(station)
        return []
'''

#Get data Tube stations
def getTubeSData(row):
    stationNaptan = row[0]
    stationName = row[1]
    stopType = row[2].replace('Naptan', '')
    lat = row[3]
    lon = row[4]
    line = row[5]
    wifi = row[6]
    zone = row[7]
    address = row[8]
    wkt = ('POINT ' + '(' + lat + ',' + lon + ')').replace(',',' ')
    businessType = 'http://data.linkedevents.org/kos/3cixty/subway'
    publisher = 'https://tfl.gov.uk'
    stopGUID = getUid(row[0])


    lst = [stationNaptan,#0
           stationName,#1
           stopType,#2
           lat,#3
           lon,#4
           line,#5
           wifi,#6
           zone,#7
           address,#8
           wkt,#9
           businessType,#10
           publisher,#11
           stopGUID]#12

    return lst

def createStation(stationName): #createTubeGraph
    stationName = URIRef('http://data.linkedevents.org/transit/london/subwayStop/' + Literal(stationName).replace(" ", "").replace("(","").replace(")","").replace("-","_").replace('&', "And").replace("&amp;","And"))
    #stationName = URIRef('http://data.linkedevents.org/transit/london/subwayStop/' + Literal(stationName).replace([" (-"], "").replace('&', "And").replace("&amp;", "And"))
    return stationName

def createStationGeom(stationName): #createTubeSGraph
    stationGeom = URIRef(createStation(stationName) + '/geometry')
    return stationGeom

def createLine(line):#
    singleLine = URIRef('http://data.linkedevents.org/transit/london/subwayRoute/' + Literal(line).replace(" ", ""))
    return singleLine

def createAddress(addressGUID):
    singleAddress = URIRef(('http://data.linkedevents.org/location/%s/address') % addressGUID)
    return singleAddress


def createTubeSGraph(arg,g):
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    locationOnt = Namespace("http://data.linkedevents.org/def/location#")
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    transit = Namespace("http://vocab.org/transit/terms/")
    dul = Namespace("http://ontologydesignpatterns.org/ont/dul/DUL.owl#")
    locn = Namespace("http://www.w3.org/ns/locn#")
    dc = Namespace("http://purl.org/dc/elements/1.1/")
    geosparql = Namespace("http://www.opengis.net/ont/geosparql#")
    dct = Namespace('http://purl.org/dc/terms/')
    transit = Namespace("http://vocab.org/transit/terms/")
    schema = Namespace('http://schema.org/')
    
    #singleStation = createStation(str(arg[1]).strip())##
    singleStation = createStation(getUid(arg[0]))
    # singleGeometry = createStationGeom(str(arg[1]).strip())##
    singleGeometry = createStationGeom(getUid(arg[0]))  ##
    singleLine= createLine(str(arg[5]).strip())
    singleAddress= createAddress(str(getUid(arg[0])))

    
    g.add((singleStation, rdf.type, transit.Station))
    g.add((singleStation, rdf.type, dul.Place))
    g.add((singleStation, rdfs.label, Literal(str(arg[1]).strip())))
    g.add((singleStation, dct.description, Literal(str(arg[2]).strip())))
    g.add((singleStation, geo.location, createStationGeom(arg[0]))) 
    g.add((singleStation, locationOnt.businessType, URIRef(arg[10])))
    g.add((singleStation, dc.publisher, URIRef(arg[11])))
    g.add((singleStation, transit.route, singleLine))
    #g.add((singleStation, locn.address, singleAddress))

    #g.add((singleAddress, rdf.type, schema.PostalAddress))
    #g.add((singleAddress, rdf.type, dct.Location))
    #g.add((singleAddress, dct.title, Literal(arg[1])))
    #g.add((singleAddress, schema.streetAddress, Literal(arg[8])))

    g.add((singleLine, rdf.type, transit.RailRoute))
    g.add((singleLine, schema.name, Literal(str(arg[5]))))
    g.add((singleLine, transit.Station, singleStation))


    g.add((singleGeometry, rdf.type, geo.Point))
    g.add((singleGeometry, geo.lat, Literal(arg[3], datatype=xsd.placeholder)))
    g.add((singleGeometry, geo.long, Literal(arg[4], datatype=xsd.placeholder)))
    g.add((singleGeometry, locn.geometry, Literal(arg[9], datatype=geosparql.wktLiteral)))

    return g   

'''
def createTubeTGraph(arg,g):
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    qb = Namespace('http://purl.org/linked-data/cube#')
    travel = Namespace('http://3cixty.com/ontology#')
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

    singleTime = createTimeBetween(arg[0])#
    g.add((singleTime, rdf.type, qb.Observation))
    g.add((singleTime, travel.origin, createStation(arg[1])))#
    g.add((singleTime, travel.destination, createStation(arg[2])))#
    g.add((singleTime, travel.travelTime, Literal(arg[3], datatype=xsd.int)))
    return g
    
def createAreasGraph(arg,g):
    schema = Namespace("http://schema.org/")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    dct = Namespace('http://purl.org/dc/terms/')
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#") 
    locn = Namespace("http://www.w3.org/ns/locn#")
    
    singleArea = createArea(arg[1])#
    singleAreaGeom = createAreaGeom(arg[1])#
    g.add((singleArea, rdf.type, schema.AdministrativeArea))
    g.add((singleArea, rdfs.label, Literal(str(arg[0]).title())))
    g.add((singleArea, dct.identifier, Literal(arg[1])))
    g.add((singleArea, geo.location, singleAreaGeom))
    g.add((singleAreaGeom, locn.geometry, Literal(arg[2])))
    return g
'''

def main():

    inFileTube = 'IN/validation/tram_validated.csv'
    outFileTube = "OUT/tram_dirty" +".ttl"

    csvTubeS=readCsv(inFileTube)

    next(csvTubeS, None)

    tubeS_store = plugin.get('IOMemory', Store)()
    tubeS_g= Graph(tubeS_store)

    prefixes=definePrefixes()
    
    print('Binding Prefixes')
    bindingPrefixes(tubeS_g,prefixes)
    #bindingPrefixes(tubeT_graph,prefixes)

    print('Creating graph-TubeS...')
    flag=1
    for row in csvTubeS:
        lstData = getTubeSData(row)
        createTubeSGraph(lstData,tubeS_g)

    createTubeSGraph(lstData,tubeS_g).serialize(outFileTube,format='turtle')


    print ('DONE!')
    
if __name__ == "__main__":
    main();
