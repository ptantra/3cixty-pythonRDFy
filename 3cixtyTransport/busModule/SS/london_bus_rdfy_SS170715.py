__author__ = 'casa'
# -*- coding: utf-8 -*-

import csv, zipfile, uuid, pyproj, re
from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict

#import _3cixty_transportCommon as common
#from common import readCsv, getUid, convertProj, definePrefixes, bindingPrefixes


def readCsv(inputfile):
    try:
          f=open(inputfile,'rU');
          rf=csv.reader(f,delimiter=',');
          return rf;
    except IOError as e:
         print ("I/O error({0}): {1}".format(e.errno, e.strerror))
         raise

def readDict():  # needed?
    dict = defaultdict(list)
    with open( '/Users/patrick/3cixty/codes/3cixtyTransport/busModule/IN/dictionary.csv', 'r') as f:
        r = csv.DictReader(f)
        for row in r:
            for (k, v) in row.items():
                dict[k] = v
    f.close()
    return dict

def getUid(r0):##BUS
    #naptan = Namespace("http://transport.data.gov.uk/def/naptan/")
    nspaces = readDict()
    naptan = Namespace(nspaces.get('naptan'))
    #objectID  = r1
    idencode=r0.encode('utf-8')
    uid=uuid.uuid5(naptan, idencode)
    return uid

def ConvertProj(lat,lon):##BUS
    Bng = pyproj.Proj(init='epsg:27700')
    Wgs84 = pyproj.Proj(init='epsg:4326')
    #print (lat+'-'+lon)
    wgsLon,wgsLat = pyproj.transform(Bng,Wgs84,lon, lat)
    return wgsLon,wgsLat

def definePrefixes():
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


def getBusData(row):

    objectID  = row[1]
    uid=getUid(row[0]) ##COMMON FILE

    stopLat=''
    stopLong=''
    try:
        stopLat,stopLong=ConvertProj(row[4],row[5]) ##COMMON FILE
    except TypeError as e:
        print ("wrong lat, long -".format(e))

    noAddress=""
    stopid = objectID
    stopGeometry = "POINT ("+str(stopLat) +" "+str(stopLong)+")"
    stopRoute = URIRef('http://data.linkedevents.org/transit/London/route/')
    stopGUID = uid
    stopTitle = Literal(str(row[3]))
    stopAddress = Literal(noAddress)
    stopLocnAddress = Literal(noAddress)
    stopAddressLocality = Literal('London')
    stopAdminUnitL2 = Literal('London')
    stopPublisher = URIRef('https://tfl.gov.uk/modes/buses/')
    stopBusinessType = URIRef('http://data.linkedevents.org/kos/3cixty/busstop')
    stopLabel = Literal('Bus Stop - '+str(row[3]))

    lst = [stopid, stopLat, stopLong, stopGeometry, stopRoute, stopGUID, stopTitle, stopAddress, stopLocnAddress, stopAddressLocality, stopAdminUnitL2, stopPublisher, stopBusinessType, stopLabel]

    return lst

#get station line
def validateCol(row):
    if row is not None:
        for index in range(0,len(row)):
            row[index]=re.sub('\r\t\t\t','',row[index])
    return row
    
#this creates a url of a single bus stop with the test id
def createBusStop(stopId):
    singleStop = URIRef("http://data.linkedevents.org/transit/London/stop/" + stopId)
    return singleStop

#this creates geometry url
def createGeometry(stopId, stopsGUID):
    singleGeometry = URIRef(('http://data.linkedevents.org/location/%s/geometry') % stopsGUID)
    return singleGeometry

#this creates single address
def createAddress(stopId, stopsGUID):
    singleAddress = URIRef(('http://data.linkedevents.org/location/%s/address') % stopsGUID)
    return singleAddress

#-------- Buslines    
#create line URL
def createLine(busId):
    lineId = URIRef('http://data.linkedevents.org/transit/London/busLine/' + busId)
    return lineId

#create line geometry url
def createGeometryURL(busId):
    geometryURL = URIRef('http://data.linkedevents.org/transit/London/busLine/' + Literal(busId) + '/geometry')
    return geometryURL


#creates graph of one bus stop
def createBusGraph(arg,g):
    schema = Namespace("http://schema.org/")
    naptan = Namespace("http://transport.data.gov.uk/def/naptan/london")
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    locationOnt = Namespace("http://data.linkedevents.org/def/location#")
    geom = Namespace("http://geovocab.org/geometry#")
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    transit = Namespace("http://vocab.org/transit/terms/")
    dcterms = Namespace("http://purl.org/dc/terms/")
    dul = Namespace("http://ontologydesignpatterns.org/ont/dul/DUL.owl#")
    locn = Namespace("http://www.w3.org/ns/locn#")
    dc = Namespace("http://purl.org/dc/elements/1.1/")

    singleStop = createBusStop(arg[0])
    singleAddress = createAddress(arg[0], arg[5])
    singleGeometry = createGeometry(arg[0], arg[5])
    
    g.add((singleStop, rdf.type, naptan.BusStop))
    g.add((singleStop, rdf.type, dul.Place))
    g.add((singleStop, rdf.type, transit.Stop))
    g.add((singleStop, dc.identifier, Literal(arg[0])))
    g.add((singleStop, geom.geometry, singleGeometry))
    g.add((singleStop, schema.geo, singleGeometry))
    g.add((singleAddress, rdf.type, schema.PostalAddress))
    g.add((singleAddress, rdf.type, dcterms.Location))
    g.add((singleAddress, dcterms.title, arg[6]))
    g.add((singleAddress, schema.streetAddress, arg[7]))
    g.add((singleAddress, locn.address, arg[8]))
    g.add((singleAddress, schema.addressLocality, arg[9]))
    g.add((singleAddress, locn.adminUnitL12, arg[10]))
    g.add((singleGeometry, rdf.type, geo.Point))
    g.add((singleGeometry, geo.lat, Literal(arg[1], datatype=xsd.placeholder)))
    g.add((singleGeometry, geo.long, Literal(arg[2], datatype=xsd.placeholder)))
    #g.add((singleGeometry, locn.geometry, Literal(arg[3], datatype=geosparql.wktLiteral)))
    g.add((singleStop, geo.location, singleGeometry))
    g.add((singleStop, transit.route, arg[4]))
    g.add((singleStop, schema.location, singleAddress))
    g.add((singleStop, locn.address, singleAddress))
    g.add((singleStop, dc.publisher, arg[11]))
    g.add((singleStop, locationOnt.businessType, arg[12]))
    g.add((singleStop, rdfs.label, arg[13]))
    return g

def main():

    busPathf ="./"
    inFileB = busPathf + "IN/validation/bus_validated.csv"
    outFileB= busPathf + "OUT/"+"bus_" + strftime("%Y%m%d") +".ttl"


    csvB=readCsv(inFileB)
    busline_store = plugin.get('IOMemory', Store)()
    bus_g= Graph(busline_store)
    #busline_graph = ConjunctiveGraph(busline_store)

    prefixes=definePrefixes()
    
    print('Binding Prefixes')
    bindingPrefixes(bus_g, prefixes)


    print('Creating graph-Bus...')
    for row in csvB:
        lstData = getBusData(row)
        #createBusGraph(lstData,g)
        createBusGraph(lstData,bus_g).serialize(outFileB,format='turtle')


    print ('DONE!')
    
if __name__ == "__main__":
    main();

