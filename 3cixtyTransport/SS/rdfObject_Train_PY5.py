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


def ConvertProj(lat,lon): #+TICKED
    Bng = pyproj.Proj(init='epsg:27700')
    Wgs84 = pyproj.Proj(init='epsg:4326')
    wgsLon,wgsLat = pyproj.transform(Bng,Wgs84,lon, lat)
    return wgsLon,wgsLat

def getUid(r0):
    naptan = Namespace("http://transport.data.gov.uk/def/naptan/")
    #objectID  = r1
    idencode=r0.encode('utf-8')
    uid=uuid.uuid5(naptan, idencode)
    return uid

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
    #STATION GRAPH LIST

    stationId = row[0]
    stationGUID = getUid(row[0])
    stationLat=row[4]
    stationLong=row[5]
    stationGeometry = "POINT ("+str(stationLat) +" "+str(stationLong)+")"
    stationRoute = Literal(str(row[3]))#.replace('Nth','North').replace("Lon","London")
    stationTitle = Literal(str(row[1])).replace(" ", "-").lower()
    stationPublisher = URIRef('https://tfl.gov.uk/modes/trains/') ##??IS THIS CORRECT??
    stationBusinessType = URIRef('http://data.linkedevents.org/kos/3cixty/trainstation')

    #LINE GRAPH LIST
    trainRoute=row[3].replace(" ", "-").lower()
    trainId=row[1].replace(" ", "-").lower()
    trainWkt = row[6]
    trainLabel = row[3]

    lst = [stationId, stationLat, stationLong, stationGeometry, stationRoute, stationTitle,
           stationBusinessType, stationPublisher, trainId, trainWkt, trainRoute, trainLabel,stationGUID]
    return lst

#this creates a url of a single train station with the test id
def createTrainStation(stationTitle): #update to train
    singleStation = URIRef("http://data.linkedevents.org/transit/London/station/" + Literal(stationTitle))
    return singleStation

#this creates geometry url #CAUSING THE ERRORS
def createGeometry(stationTitle): #+TICKED
    singleGeometry = URIRef("http://data.linkedevents.org/location/" + stationTitle + "/geometry")
    return singleGeometry

#-------- Trainlines
#create line URL
def createLine(trainId):
    lineId = URIRef('http://data.linkedevents.org/transit/London/trainLine/' + trainId)
    return lineId


#create route
def createRoute(route):
    trainRoute = URIRef('http://data.linkedevents.org/transit/London/route/' + route)
    return trainRoute


#create train station and train line graphs
def createTrainGraph(arg,g): #+TICKED

    #STATIONS GRAPH
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

    singleStation = createTrainStation(arg[5]) #"http://data.linkedevents.org/transit/London/station/" + Literal(stationTitle)
    singleGeometry= URIRef("http://data.linkedevents.org/location/" + "%s" + "/geometry") % arg[5]
    #singleGeometry = createGeometry(arg[5]) #"http://data.linkedevents.org/location/" + Literal(stationId) + "/geometry"
    transitRouteValue = URIRef("http://data.linkedevents.org/transit/London/railwayRoute/%s") % arg[4].replace(" ", "-").lower()

    g.add((singleStation, rdf.type, naptan.RailwayStation))
    g.add((singleStation, rdf.type, dul.Place))
    g.add((singleStation, rdf.type, transit.Stop))
    g.add((singleStation, dc.identifier, Literal(arg[0])))
    g.add((singleStation, rdfs.label, Literal(arg[5])))  #g.add((singleStation, rdfs.label, arg[3]))

    g.add((singleGeometry, rdf.type, geo.Point))
    g.add((singleGeometry, geo.lat, Literal(arg[1], datatype=xsd.double)))
    g.add((singleGeometry, geo.long, Literal(arg[2], datatype=xsd.double)))
    g.add((singleGeometry, locn.geometry, Literal(arg[3], datatype=geosparql.wktLiteral)))
    g.add((singleStation, transit.route, transitRouteValue))
    g.add((singleStation, schema.name, Literal(arg[4]))) #NEW
    g.add((singleStation, geo.location, Literal(singleGeometry)))#g.add((singleStation, schema.location, singleAddress))
    g.add((singleStation, dc.publisher, Literal(arg[7])))
    g.add((singleStation, locationOnt.businessType, Literal((arg[6]))))

    #TRAIN LINES GRAPH
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    schema = Namespace("http://schema.org/")

    singleLine=createLine(arg[8])

    g.add((singleLine, rdf.type, transit.RailRoute)) #trainroute to trainroute
    g.add((singleLine, transit.route, createRoute(arg[10])))
    g.add((createRoute(arg[10]), schema.name, Literal(arg[11])))
    return g


def main():
    pathf="/Users/patrick/3cixty/IN/RM/151026/"
    inFileTS = pathf+"train_stations.csv"
    outFileTS=pathf+"train_stations.ttl"

    csvTS=readCsv(inFileTS)
    next(csvTS, None)  #FILE WITH HEADERS

    store = plugin.get('IOMemory', Store)()
    g = Graph(store)

    prefixes=definePrefixes()
    print('Binding Prefixes')
    bindingPrefixes(g,prefixes)

    print('Creating graph-Train...') #AMENDED
    for row in csvTS:
        lstData = getTrainData(row)
        createTrainGraph(lstData,g)
    createTrainGraph(lstData,g).serialize(outFileTS,format='turtle')


    print ('DONE!')

if __name__ == "__main__":
    main();