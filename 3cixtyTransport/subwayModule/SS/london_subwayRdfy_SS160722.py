__author__ = 'casa'
# -*- coding: utf-8 -*-

import csv, zipfile, uuid, pyproj, re, imp
from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import readCsv, getUid, ConvertProj, definePrefixes, bindingPrefixes, readDict

pathf = "./"

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


#Get data Tube stations
def getTubeSData(row):#

    x = row[1]
    y = row[2]
    station = row[0]
    description = row[4]
    wkt = row[3]
    businessType = 'http://data.linkedevents.org/kos/3cixty/subway'
    publisher = 'https://tfl.gov.uk'
    
    path = pathf + 'IN/'
    stationLine = transfer(station,path)

    lines = ['Bakerloo',
              'Central',
              'Circle',
              'District',
              'Hammersmith & City',
              'Jubilee',
              'Metropolitan',
              'Northern',
              'Piccadilly',
              'Victoria',
              'Waterloo & City']
    lst = [x, y, station, description, wkt,businessType,publisher,lines,stationLine]
    return lst

#Get Tube Time
'''
def getTubeTData(row,count):#
    origin = row[0]
    dest   = row[1]
    time   = row[2]
    lst = [count, origin, dest, time]
    return lst 


#GetAreasData
def getAreasData(row):#
    name = row[0]
    code = row[1]
    geom = row[2]
    lst = [name, code, geom]
    return lst

def createSubwayRoute(tubelines):#
    tubes = []
    for i in tubelines:
        tubeline = URIRef('http://data.linkedevents.org/transit/London/subwayRoute/' + Literal(i).replace(" ", ""))
        tubes.append(tubeline)
    return tubes

'''

def createStation(station): #createTubeGraph
    stationName = URIRef('http://data.linkedevents.org/transit/London/subwayStop/' + Literal(station).replace(" ", ""))
    return stationName

def createStationGeom(station): #createTubeSGraph
    stationGeom = URIRef(createStation(station) + '/geometry')
    return stationGeom

def addStationLine(g,lines,station):#
    transit = Namespace("http://vocab.org/transit/terms/")
    for i in lines[1:]:
        singleLine = URIRef('http://data.linkedevents.org/transit/London/subwayRoute/' + Literal(i).replace(" ", ""))
        g.add((createStation(station), transit.route, singleLine))
    return g

def createArea(code): #createAreasGraph
    area = URIRef('http://data.linkedevents.org/transit/London/area/' + Literal(code))
    return area

def createAreaGeom(code):#
    areaGeom = URIRef(createArea(code) + '/geometry')
    return areaGeom
    
def createTimeBetween(id):##
    timeBetween = URIRef('http://data.linkedevents.org/travel/London/timeBetween#' + Literal(id))
    return timeBetween    

def createTubeSGraph(arg,g,flag):
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
    
    singleStation = createStation(str(arg[2]).strip())##
    singleGeometry = createStationGeom(str(arg[2]).strip())##
    
    g.add((singleStation, rdf.type, transit.Station))
    g.add((singleStation, rdf.type, dul.Place))
    g.add((singleStation, rdfs.label, Literal(str(arg[2]).strip())))
    g.add((singleStation, dct.description, Literal(str(arg[3]).strip())))
    g.add((singleStation, geo.location, createStationGeom(arg[2]))) ##
    g.add((singleStation, locationOnt.businessType, URIRef("http://data.linkedevents.org/kos/3cixty/subway")))
    g.add((singleStation, dc.publisher, URIRef("https://tfl.gov.uk")))
    g.add((singleGeometry, rdf.type, geo.Point))    
    g.add((singleGeometry, geo.lat, Literal(arg[0], datatype=xsd.double)))
    g.add((singleGeometry, geo.long, Literal(arg[1], datatype=xsd.double)))
    g.add((singleGeometry, locn.geometry, Literal(arg[4], datatype=geosparql.wktLiteral)))  
    
    addStationLine(g,arg[8],arg[2])#
    
    if flag:
        for i in arg[7]:
            #g.add((i, rdf.type, transit.SubwayRoute))
            createSubwayRoute(arg[7])#
    bindingPrefixes()
    return g   

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

def main():

    #url='http://data.tfl.gov.uk/tfl/syndication/feeds/stations.kml?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'

    pathf = "./"
    inFileTube = pathf + "IN/" +"tfl_subway" + strftime("%Y%m%d") +".csv"
    outFileTube = pathf + "OUT/" +"tfl_subway" + strftime("%Y%m%d") +".ttl"
    #inFileTube = pathf + "/IN/" +"boroughs_coma.csv"
    #outFileTube = pathf + "/OUT/" + "boroughs_coma.ttl"
    #inFileTube = pathf + "/IN/" + "time_between.csv"
    #outFileTube= pathf+ "/OUT/" + "TubeSegmentedTime.ttl"
 
    csvTubeS=readCsv(inFileTube)
    #csvAreas=readCsv(inFileTube)
    #csvTubeT=readCsv(inFileTube)

    next(csvTubeS, None)
    #next(csvAreas, None)
    #next(csvTubeT, None)
    store = plugin.get('IOMemory', Store)()
    g = Graph(store)
    #graph = ConjunctiveGraph(store)


    tubeS_store = plugin.get('IOMemory', Store)()
    tubeS_g= Graph(tubeS_store)
    #tubeS_graph = ConjunctiveGraph(tubeS_store)
    
    #Areas_store = plugin.get('IOMemory', Store)()
    #Areas_g= Graph(Areas_store)
    #Areas_graph = ConjunctiveGraph(Areas_store)

    #tubeT_store = plugin.get('IOMemory', Store)()
    #tubeT_g= Graph(tubeT_store)
    #tubeT_graph = ConjunctiveGraph(tubeT_store)

    prefixes=definePrefixes()
    
    print('Binding Prefixes')
    bindingPrefixes(tubeS_g,prefixes)
    #bindingPrefixes(tubeT_graph,prefixes)

    print('Creating graph-TubeS...')
    flag=1
    for row in csvTubeS:
        lstData = getTubeSData(row)
        createTubeSGraph(lstData,tubeS_g,flag)
        flag=0
    createTubeSGraph(lstData,tubeS_g,flag).serialize(outFileTube,format='turtle')    

    '''
    print('Creating graph-Areas...')
        lstData = getAreasData(row)#
    for row in csvAreas:
        createAreasGraph(lstData,Areas_g)
    createAreasGraph(lstData,Areas_g).serialize(outFileTube,format='turtle')
 
    print('Creating graph-TubeT...')
    
    count=1
    for row in csvTubeT:
        lstData = getTubeTData(row,count)#
        count=count+1
        createTubeTGraph(lstData,tubeT_g)
    createTubeTGraph(lstData,tubeT_g).serialize(outFileTube,format='turtle')
    '''
    
    print ('DONE!')
    
if __name__ == "__main__":
    main();
