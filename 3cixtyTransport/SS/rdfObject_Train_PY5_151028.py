# coding=utf-8
__author__ = 'patrick'

__author__ = 'Wick 1'
__author__ = 'casa'
# -*- coding: utf-8 -*-
#libraries
#import tkinter as tk
#from tkinter import filedialog
import csv
import uuid
import pyproj
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store

def readCsv(inputfile): #+TICKED
    try:
          f=open(inputfile,'rU');
          rf=csv.reader(f,delimiter=',');
          return rf;
    except IOError as e:
         print ("I/O error({0}): {1}".format(e.errno, e.strerror))
         raise


def getUid(r0): #+TICKED
    naptan = Namespace("http://transport.data.gov.uk/def/naptan/") ##MAYBE CHANGE??##
    idencode=r0.encode('UTF-8')
    uid=uuid.uuid5(naptan, idencode)
    return uid

def ConvertProj(lat,lon): #+TICKED
    Bng = pyproj.Proj(init='epsg:27700')
    Wgs84 = pyproj.Proj(init='epsg:4326')
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
        'trans': 'http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/Transporte#'}
    return prefixes

def bindingPrefixes(graphs,prefixes): #+TICKED
    for key in prefixes:
        graphs.bind(key, prefixes[key])
    return graphs

def getTrainData(row): #amended #+TICKED
    objectID  = row[0]
    uid=getUid(row[0])
    stationLat=row[4]
    stationLong=row[5]
    stationid = objectID
    stationGeometry = "POINT ("+str(stationLat) +" "+str(stationLong)+")"
    stationRoute = Literal(str(row[3]))#.replace('Nth','North').replace("Lon","London")
    stationGUID = uid
    stationTitle = Literal(str(row[1]))
    stationPublisher = URIRef('https://tfl.gov.uk/modes/trains/') ##??IS THIS CORRECT??
    stationBusinessType = URIRef('http://data.linkedevents.org/kos/3cixty/trainstation')

    lst = [stationid, stationLat, stationLong, stationGeometry, stationRoute, stationGUID, stationTitle, stationBusinessType, stationPublisher]
    return lst



#this creates a url of a single train station with the test id
def createTrainStation(stationId): #update to train
    singleStation = URIRef("http://data.linkedevents.org/transit/London/station/" + stationId)
    return singleStation

#this creates geometry url
def createGeometry(stationId, stationGUID): #+TICKED
    singleGeometry = URIRef(('http://data.linkedevents.org/location/%s/geometry') % stationGUID)
    return singleGeometry

#this creates single address
def createAddress(stationId, stationGUID):
    singleAddress = URIRef(('http://data.linkedevents.org/location/%s/address') % stationGUID)
    return singleAddress

#creates graph of one train station
def createTrainGraph(arg,g): #+TICKED
    schema = Namespace("http://schema.org/")
    naptan = Namespace("http://transport.data.gov.uk/def/naptan/")
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    locationOnt = Namespace("http://data.linkedevents.org/def/location#")
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    geosparql = Namespace("http://www.opengis.net/ont/geosparql#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    transit = Namespace("http://vocab.org/transit/terms/")
    dul = Namespace("http://ontologydesignpatterns.org/ont/dul/DUL.owl#")
    locn = Namespace("http://www.w3.org/ns/locn#")
    dc = Namespace("http://purl.org/dc/elements/1.1/")

    singleStation = createTrainStation(arg[0])
    singleStation2 = createTrainStation(arg[6].replace(" ", "-").lower())
    singleAddress = createAddress(arg[0], arg[5]) ##check arg[5]#singleStation = self.createTrainStation(stationid)
    singleGeometry = createGeometry(arg[6]) #station names without spaces
    transitRouteValue = URIRef("http://data.linkedevents.org/transit/London/railwayRoute/%s") % arg[4].replace(" ", "-").lower()

    g.add((singleStation2, rdf.type, naptan.RailwayStation))
    g.add((singleStation2, rdf.type, dul.Place))
    g.add((singleStation2, rdf.type, transit.Stop))
    g.add((singleStation2, dc.identifier, Literal(arg[0])))
    g.add((singleGeometry, rdf.type, geo.Point))
    g.add((singleGeometry, geo.lat, Literal(arg[1], datatype=xsd.double)))
    g.add((singleGeometry, geo.long, Literal(arg[2], datatype=xsd.double)))
    g.add((singleGeometry, locn.geometry, Literal(arg[3], datatype=geosparql.wktLiteral)))
    g.add((singleStation2, transit.route, transitRouteValue))
    g.add((singleStation2, schema.name, Literal(arg[4]))) #NEW
    g.add((singleStation2, geo.location, singleGeometry)) #g.add((singleStation, schema.location, singleAddress))
    g.add((singleStation2, dc.publisher, arg[8]))
    g.add((singleStation2, locationOnt.businessType, (arg[7])))
    g.add((singleStation2, rdfs.label, Literal(arg[6])))  #g.add((singleStation, rdfs.label, arg[3]))
    return g

#-------- Trainlines

def getTrainLineData(row):

    trainRoute=row[3].replace(" ", "-").lower()
    trainId=row[1].replace(" ", "-").lower()
    trainWkt = row[6]
    trainLabel = row[3]
    lst = [trainId, trainWkt, trainRoute, trainLabel]

    return lst


#create line URL
def createLine(trainId):
    lineId = URIRef('http://data.linkedevents.org/transit/London/trainLine/' + trainId)
    return lineId


#create line geometry url
def createGeometryURL(trainId):
    geometryURL = URIRef('http://data.linkedevents.org/transit/London/trainLine/' + trainId + '/geometry')
    return geometryURL

#create geometry
def createGeometry(trainWkt):
    routeGeometry = Literal(trainWkt)
    return routeGeometry


#create routeService or serviceId
def createRouteService(route, run):
    routeService = URIRef('http://data.linkedevents.org/transit/London/service/' + route + '_' + Literal(run))
    return routeService

#create route
def createRoute(route):
    trainRoute = URIRef('http://data.linkedevents.org/transit/London/route/' + route)
    return trainRoute


def createServiceStop(service, stopCode):
    serviceStopId = URIRef('http://data.linkedevents.org/transit/London/serviceStop/' + service + '/' + Literal(stopCode))
    return serviceStopId


#create service URL
def createService(service):
    serviceURL = URIRef('http://data.linkedevents.org/transit/London/service/' + service)
    return serviceURL


#create stop URL
def createStop(stopCode): #+TICKED
    stopURL = URIRef('http://data.linkedevents.org/transit/London/station/' + Literal(stopCode)) #amended
    return stopURL


def createTrainLineGraph(arg,trainline_g): #??

    #rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    #geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    #sf = Namespace("http://www.opengis.net/ont/sf#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    transit = Namespace("http://vocab.org/transit/terms/")
    schema = Namespace("http://schema.org/")
    #locn = Namespace("hƒttp://www.w3.org/ns/locn#")
    #geosparql = Namespace("http://www.opengis.net/ont/geosparql#")

    idb=arg[0]
    #idb=idb[9:]
    singleLine=createLine(idb)
    singleStation2 = createTrainStation(arg[3].replace(" ", "-").lower())
    #singleGeometryURL=createGeometryURL(idb)
    #singleService=createRouteService(arg[2], arg[3])


    trainline_g.add((singleLine, rdf.type, transit.RailRoute)) #trainroute to trainroute
    trainline_g.add((singleLine, transit.route, createRoute(arg[2])))
    #trainline_g.add((singleLine, schema.name, Literal(arg[3])))

    trainline_g.add((createRoute(arg[2]), schema.name, Literal(arg[3]))) #??????
    return trainline_g


def main(): #+TICKED
    pathf="/Users/patrick/3cixty/IN/RM/151026/"
    inFileB = pathf+"train_stations.csv"
    outFileB=pathf+"train_stations.ttl"
    inFileBR = pathf+"train_stations.csv"
    outFileBR=pathf+"trainR.ttl"

    csvB=readCsv(inFileB)
    csvBR=readCsv(inFileBR)

    next(csvB, None)  #FILE WITH HEADERS
    next(csvBR, None)  #FILE WITH HEADERS


    store = plugin.get('IOMemory', Store)()
    g = Graph(store)
    graph = ConjunctiveGraph(store)

    trainline_store = plugin.get('IOMemory', Store)()
    trainline_g= Graph(trainline_store)
    trainline_graph = ConjunctiveGraph(trainline_store)
    prefixes=definePrefixes()
    print('Binding Prefixes')
    bindingPrefixes(graph,prefixes)
    bindingPrefixes(trainline_graph,prefixes)

    print('Creating graph-Train...') #AMENDED
    for row in csvB:
        lstData = getTrainData(row)
        createTrainGraph(lstData,g)
    createTrainGraph(lstData,g).serialize(outFileB,format='turtle')

    print('Creating graph-trainR...')
    for row in csvBR:
        lstData = getTrainLineData(row)
        createTrainLineGraph(lstData,trainline_g)
    createTrainLineGraph(lstData,trainline_g).serialize(outFileBR,format='turtle')

    print ('DONE!')

if __name__ == "__main__":
    main();