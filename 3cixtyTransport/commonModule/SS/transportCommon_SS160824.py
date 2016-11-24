__author__ = 'casa'
# -*- coding: utf-8 -*-
import csv, zipfile, uuid, pyproj, re, fileinput, urllib
from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict

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
    idencode=r0.encode('utf-8')
    uid=uuid.uuid5(naptan, idencode)
    return uid

def ConvertProj(lon,lat):
    Bng = pyproj.Proj(init='epsg:27700')
    Wgs84 = pyproj.Proj(init='epsg:4326')
    #print (lat+'-'+lon)
    wgsLon,wgsLat = pyproj.transform(Bng,Wgs84,lon, lat)
    return wgsLon,wgsLat

def readDict():
    dict = defaultdict(list)
    with open('/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/nspaceDict.csv','rb') as f:
        r = csv.DictReader(f)
        for row in r:
            for (k,v) in row.items():
                dict[k]=v
    f.close()
    return dict

def definePrefixes():
    prefixes = {
        'dc': 'http://purl.org/dc/elements/1.1/',
        'dcterms': 'http://purl.org/dc/terms/',
        'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
        'foaf': 'http://xmlns.com/foaf/0.1/',
        'geom': 'http://geovocab.org/geometry#',
        'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
        'geosparql': 'http://www.opengis.net/ont/geosparql#',
        'locn': 'http://www.w3.org/ns/locn#',
        'locationOnt': 'http://data.linkedevents.org/def/location#',
        'naptan': 'http://transport.data.gov.uk/def/naptan/',
        'owl': 'http://www.w3.org/2002/07/owl#',
        'qb': 'http://purl.org/linked-data/cube#',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
        'schema':'http://schema.org/',
        'sf': 'http://www.opengis.net/ont/sf#',
        'trans': 'http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/Transporte#',
        'transit': 'http://vocab.org/transit/terms/',
        'travel': 'http://3cixty.com/ontology#',
        'unknown': 'http://data.linkedevents.org/def/unknown#',
        'vcard': 'http://www.w3.org/2006/vcard/ns#',
        'xsd': 'http://www.w3.org/2001/XMLSchema#'
        }
    return prefixes

def bindingPrefixes(graphs,prefixes): #Modules: Bus, Bike
    for key in prefixes:
        graphs.bind(key, prefixes[key])
    return graphs

def convertXsdDouble(inFile, outFile):
    s = open(inFile).read()
    s = s.replace("^^xsd:placeholder", "^^xsd:double")
    f = open(outFile, 'w')
    f.write(s)
    f.close()

def urlRetrieve(inUrl, outFile):
    urllib.urlretrieve(inUrl, outFile)




#getBusData(row)
#getBusLineData(row)
#getBusCData(row
#validateCol(row)#get station line
#transfer(station,path)

#getTubeSData(row)#Get data Tube stations
#getTubeTData(row,count)#Get Tube Time
#getAreasData(row)#GetAreasData
#---------------

#createBusStop(stopId)#this creates a url of a single bus stop with the test id

#createGeometry(stopId, stopsGUID) #this creates geometry url
#createAddress(stopId, stopsGUID)#this creates single address

#-------- Buslines

#createLine(busId)#create line URL
#createGeometryURL(busId)#create line geometry url

#create geometry
#def createGeometry(busWkt):
 #   routeGeometry = Literal(busWkt)
  #  return routeGeometry

#createRouteService(route, run)#create routeService or serviceId

#createRoute(route)#create route
#createServiceStop(service, stopCode)

#SUBWAY?
#createService(service)#create service URL
#createStop(stopCode)#create stop URL
#createSubwayRoute(tubelines)

###TRAIN
#createStation(station)
#createStationGeom(station)
#addStationLine(g,lines,station)

#createArea(code)
#createAreaGeom(code)
#createTimeBetween(id)

#-----Graphs
#createBusCGraph(arg,busline_g)
#createBuslineGraph(arg,busline_g)
#createBusGraph(arg,g)#creates graph of one bus stop

#createTubeSGraph(arg,g,flag)
#createTubeTGraph(arg,g)
#createAreasGraph(arg,g)

#main()
