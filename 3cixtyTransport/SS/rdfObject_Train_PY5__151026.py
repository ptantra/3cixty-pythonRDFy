# coding=utf-8
__author__ = 'patrick'

__author__ = 'Wick 1'
__author__ = 'casa'
# -*- coding: utf-8 -*-
#libraries
#import tkinter as tk
#from tkinter import filedialog
import csv
import zipfile
import uuid
import pyproj
#import time
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

'''
def createZip(nzip,outFile):
    zf = zipfile.ZipFile(nzip, mode='w')
    try:
        print ('Creating zip file...')
        zf.write(outFile)
    finally:
        print ('Zip created')
        zf.close()
'''

def getUid(r0): #+TICKED
    naptan = Namespace("http://transport.data.gov.uk/def/naptan/") ##MAYBE CHANGE??##
    #objectID  = r1
    idencode=r0.encode('utf-8')
    uid=uuid.uuid5(naptan, idencode)
    return uid

def ConvertProj(lat,lon): #+TICKED
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
        'trans': 'http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/Transporte#'}
    return prefixes

def bindingPrefixes(graphs,prefixes): #+TICKED
    for key in prefixes:
        graphs.bind(key, prefixes[key])
    return graphs

def getTrainData(row): #amended #+TICKED

    #naptan = Namespace("http://transport.data.gov.uk/def/naptan/")
    #uid=uuid.uuid5(naptan, idencode)
    #idencode=row[0].encode('utf-8')
    objectID  = row[1]
    uid=getUid(row[0])

    stopLat=''
    stopLong=''
    try:
        stopLat,stopLong=ConvertProj(row[7],row[6])
    except TypeError as e:
        print ("wrong lat, long -".format(e))

    #noAddress=""
    stopid = objectID
    stopGeometry = "POINT ("+str(stopLat) +" "+str(stopLong)+")"
    stopRoute = URIRef('http://data.linkedevents.org/transit/London/route/')
    stopGUID = uid
    #stopTitle = Literal(str(row[3]))
    #stopAddress = Literal(noAddress)
    #stopLocnAddress = Literal(noAddress)
    #stopAddressLocality = Literal('London')
    #stopAdminUnitL2 = Literal('London')
    #stopPublisher = URIRef('https://tfl.gov.uk/modes/buses/')
    #stopBusinessType = URIRef('http://data.linkedevents.org/kos/3cixty/busstop')
    #stopLabel = Literal('Bus Stop - '+str(row[3]))

    #lst = [stopid, stopLat, stopLong, stopGeometry, stopRoute, stopGUID, stopTitle, stopAddress, stopLocnAddress,\
    #       stopAddressLocality, stopAdminUnitL2, stopPublisher, stopBusinessType, stopLabel]
    lst = [stopid, stopLat, stopLong, stopGeometry, stopRoute, stopGUID]
    return lst

'''
def getBusLineData(row):

    busRoute=row[0]
    busRun  = row[1]
    busId=getUid(busRoute)
    busWkt = row[3]
    busLabel = row[2]
    lst = [busId, busWkt, busRoute, busRun, busLabel]
    return lst
'''
'''
def getBusCData(row):

    stop=row[0]
    stopID  = row[1]
    stopN=getUid(row[2])
    route = row[3]
    srun = row[4]
    seq =  row[5]
    service =  row[6]
    lst = [stop, stopID, stopN, route, srun, seq, service]
    return lst
'''
#this creates a url of a single train stop with the test id
def createTrainStop(stopId): #update to train
    singleStop = URIRef("http://data.linkedevents.org/transit/London/stop/" + stopId)
    return singleStop

#this creates geometry url
def createGeometry(stopId, stopsGUID): #+TICKED
    singleGeometry = URIRef(('http://data.linkedevents.org/location/%s/geometry') % stopsGUID)
    return singleGeometry

#this creates single address
def createAddress(stopId, stopsGUID):
    singleAddress = URIRef(('http://data.linkedevents.org/location/%s/address') % stopsGUID)
    return singleAddress

#-------- Buslines
'''
#create line URL
def createLine(busId):
    lineId = URIRef('http://data.linkedevents.org/transit/London/busLine/' + busId)
    return lineId


#create line geometry url
def createGeometryURL(busId):
    geometryURL = URIRef('http://data.linkedevents.org/transit/London/busLine/' + busId + '/geometry')
    return geometryURL

#create geometry
#def createGeometry(busWkt):
 #   routeGeometry = Literal(busWkt)
  #  return routeGeometry


#create routeService or serviceId
def createRouteService(route, run):
    routeService = URIRef('http://data.linkedevents.org/transit/London/service/' + route + '_' + Literal(run))
    return routeService

#create route
def createRoute(route):
    busRoute = URIRef('http://data.linkedevents.org/transit/London/route/' + route)
    return busRoute


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


def createTrainCGraph(arg,trainline_g): ##?
    transit = Namespace("http://vocab.org/transit/terms/")
    xsd = Namespace('http://www.w3.org/2001/XMLSchema#')
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

    singleServiceStop=createServiceStop(arg[6], arg[1])
    singleService=createService(arg[6])
    singleStop=createStop(arg[1])

    trainline_g.add((singleServiceStop, rdf.type, transit.ServiceStop))
    trainline_g.add((singleServiceStop, transit.service, singleService))
    trainline_g.add((singleServiceStop, transit.sequence, Literal(arg[5], datatype=xsd.int)))
    trainline_g.add((singleServiceStop, transit.stop, singleStop))
    return trainline_g

def createTrainGraph(arg,trainline_g): #??

    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    sf = Namespace("http://www.opengis.net/ont/sf#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    transit = Namespace("http://vocab.org/transit/terms/")
    locn = Namespace("hƒttp://www.w3.org/ns/locn#")
    #geosparql = Namespace("http://www.opengis.net/ont/geosparql#")

    idb=arg[0].urn
    idb=idb[9:]
    singleLine=createLine(idb)
    singleGeometryURL=createGeometryURL(idb)
    singleService=createRouteService(arg[2], arg[3])

    trainline_g.add((singleLine, rdf.type, transit.trainRoute)) #busroute to trainroute
    trainline_g.add((singleLine, geo.location, singleGeometryURL))
    trainline_g.add((singleLine, rdfs.label, Literal(arg[4])))
    trainline_g.add((singleLine, transit.routeService, singleService))
    trainline_g.add((singleLine, transit.route, createRoute(arg[2])))
    trainline_g.add((singleGeometryURL, rdf.type, sf.LineString))
    trainline_g.add((singleGeometryURL, locn.geometry, Literal(arg[1], datatype=geosparql.wktLiteral)))
    return trainline_g
'''

#creates graph of one train stop
def createTrainGraph(arg,g): #+TICKED
    schema = Namespace("http://schema.org/")
    naptan = Namespace("http://transport.data.gov.uk/def/naptan/london")
  # owl = Namespace("http://www.w3.org/2002/07/owl#")
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
  # vcard = Namespace("http://www.w3.org/2006/vcard/ns#")
  # locationOnt = Namespace("http://data.linkedevents.org/def/location#")
  # geom = Namespace("http://geovocab.org/geometry#")
  # unknown = Namespace("http://data.linkedevents.org/def/unknown#")
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
  # geosparql = Namespace("http://www.opengis.net/ont/geosparql#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    transit = Namespace("http://vocab.org/transit/terms/")
  # dcterms = Namespace("http://purl.org/dc/terms/")
    dul = Namespace("http://ontologydesignpatterns.org/ont/dul/DUL.owl#")
    locn = Namespace("http://www.w3.org/ns/locn#")
    stopRouteService = URIRef('http://data.linkedevents.org/transit/London/routeService/') ##NEW OBJECT##
  # foaf = Namespace("http://xmlns.com/foaf/0.1/")
  # dc = Namespace("http://purl.org/dc/elements/1.1/")
  # trans = Namespace("http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/Transporte#")

    singleStop = createTrainStop(arg[0])
    singleAddress = createAddress(arg[0], arg[5]) ##check arg[5]#singleStop = self.createTrainStop(stopid)
    singleGeometry = createGeometry(arg[0], arg[5]) #check arg[5]#singleAddress = self.createAddress(stopGUID)

    g.add((singleStop, rdf.type, naptan.TrainStop))
    g.add((singleStop, rdf.type, dul.Place))
    g.add((singleStop, rdf.type, transit.Stop))
    #g.add((singleStop, dc.identifier, Literal(arg[0])))
    #g.add((singleStop, geom.geometry, singleGeometry))
    #g.add((singleStop, schema.geo, singleGeometry))
    #g.add((singleAddress, rdf.type, schema.PostalAddress))
    #g.add((singleAddress, rdf.type, dcterms.Location))
    #g.add((singleAddress, dcterms.title, arg[6]))
    #g.add((singleAddress, schema.streetAddress, arg[7]))
    #g.add((singleAddress, locn.address, arg[8]))
    #g.add((singleAddress, schema.addressLocality, arg[9]))
    #g.add((singleAddress, locn.adminUnitL12, arg[10]))
    g.add((singleGeometry, rdf.type, geo.Point))
    g.add((singleGeometry, geo.lat, Literal(arg[6], datatype=xsd.double)))
    g.add((singleGeometry, geo.long, Literal(arg[7], datatype=xsd.double)))
    #######g.add((singleGeometry, locn.geometry, Literal(arg[3], datatype=geosparql.wktLiteral))) REVISIT
    g.add((singleStop, geo.location, singleGeometry))
    g.add((singleStop, transit.route, arg[4]))
    g.add((singleStop, transit.routeService, stopRouteService)) ##NEW PREDICATE##
    g.add((singleStop, schema.name, singleAddress)) #NEW
    #g.add((singleStop, schema.location, singleAddress))
    #g.add((singleStop, locn.address, singleAddress))
    #g.add((singleStop, dc.publisher, arg[11]))
    #g.add((singleStop, locationOnt.businessType, arg[12]))
    #g.add((singleStop, rdfs.label, arg[3]))
    return g

def main(): #+TICKED
    #root = tk.Tk()
    #root.withdraw()
    #inFile = filedialog.askopenfilename()
    pathf="/Users/patrick/3cixty/IN/openDataSources/"
    inFileB = pathf+"RailReferences_Naptan_151022.csv"
    outFileB=pathf+"train_stations.ttl"
    #inFileBR = pathf+"busline_content.csv"
    #outFileBR=pathf+"busR.ttl"
    #inFileBC = pathf+"buscorrespondence.csv"
    #outFileBC=pathf+"busC.ttl"

    csvB=readCsv(inFileB)
    #csvBR=readCsv(inFileBR)
    #csvBC=readCsv(inFileBC)


    next(csvB, None)  #FILE WITH HEADERS
    #next(csvBR, None)  #FILE WITH HEADERS
    #next(csvBC, None)  #FILE WITH HEADERS

    store = plugin.get('IOMemory', Store)()
    g = Graph(store)
    graph = ConjunctiveGraph(store)
    #busline_store = plugin.get('IOMemory', Store)()
    #busline_g= Graph(busline_store)
    #busline_graph = ConjunctiveGraph(busline_store)
    #busC_store = plugin.get('IOMemory', Store)()
    #busC_g= Graph(busC_store)
    #busC_graph = ConjunctiveGraph(busC_store)


    prefixes=definePrefixes()
    print('Binding Prefixes')
    bindingPrefixes(graph,prefixes)
    #bindingPrefixes(busline_graph,prefixes)
    #bindingPrefixes(busC_graph,prefixes)

    print('Creating graph-Train...') #AMENDED
    for row in csvB:
        lstData = getTrainData(row)
        createTrainGraph(lstData,g)
    createTrainGraph(lstData,g).serialize(outFileB,format='turtle')

    #print('Creating graph-BusR...')
    #for row in csvBR:
    #    lstData = getBusLineData(row)
    #    createBuslineGraph(lstData,busline_g)
    #createBuslineGraph(lstData,busline_g).serialize(outFileBR,format='turtle')

    #print('Creating graph-BusC...')
    #for row in csvBR:
    #    lstData = getBusCData(row)
    #    createBusCGraph(lstData,busC_g)
    #createBusCGraph(lstData,busC_g).serialize(outFileBC,format='turtle')
    #nzip = pathf+time.strftime("%Y-%m-%d")+'.zip'
   # nzipB = pathf+outFileB+'.zip'
   # nzipBR = pathf+outFileBR+'.zip'
   # createZip(nzipB,outFileB)
   # createZip(nzipBR,outFileBR)

    print ('DONE!')

if __name__ == "__main__":
    main();