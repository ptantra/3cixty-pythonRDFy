__author__ = 'casa'
# -*- coding: utf-8 -*-

from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph
from rdflib.store import Store
import imp, os, pyproj

imp.load_source('common','/Users/patrick/3cixty/codes/3cixtyTransport/commonModule/transportCommon.py')
from common import readCsv, getUid, ConvertProj, definePrefixes, bindingPrefixes, readDict


#os.chdir('Z:/3cixty/3cixty_160718/3cixtyTransport/busModule/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/busModule/') # @patrick CASA Mac setup
print os.getcwd()

pathf = './'

def getBusData(row):

    if not os.path.exists('DATA/'):
        os.makedirs(strftime('DATA/'))

    objectID  = row[1]
    Lat = row[4]
    Lon = row[5]
    stopLon, stopLat = convertProj(Lon, Lat)

    noAddress=''
    stopid = objectID
    stopGeometry = 'POINT ('+str(stopLat) +' '+str(stopLon)+')'
    stopRoute = URIRef('http://data.linkedevents.org/transit/London/route/')
    stopGUID = getUid(str(row[2]))
    stopTitle = Literal(str(row[3]))
    stopAddress = Literal(noAddress)
    stopLocnAddress = Literal(noAddress)
    stopAddressLocality = Literal('London')
    stopAdminUnitL2 = Literal('London')
    stopPublisher = URIRef('https://tfl.gov.uk/modes/buses/')
    stopBusinessType = URIRef('http://data.linkedevents.org/kos/tfl/busstop')
    stopLabel = Literal('Bus Stop - '+str(row[3]))

    lst = [stopid,#0
           stopLon,#1
           stopLat,#2
           stopGeometry,#3
           stopRoute, #4
           stopTitle, #5
           stopAddress,
           stopLocnAddress,
           stopAddressLocality,
           stopAdminUnitL2,
           stopPublisher,
           stopBusinessType,
           stopLabel,
           stopGUID]

    return lst

#this creates a url of a single bus stop with the test id
def createBusStop(stopId):
    singleStop = URIRef('http://data.linkedevents.org/transit/london/stop/' + stopId)
    return singleStop

#this creates geometry url
def createGeometry(stopGUID):
    singleGeometry = URIRef(('http://data.linkedevents.org/location/%s/geometry') % stopGUID)
    return singleGeometry

#this creates single address
def createAddress(stopGUID):
    singleAddress = URIRef(('http://data.linkedevents.org/location/%s/address') % stopGUID)
    return singleAddress


def convertProj(lon,lat):##BUS
    Bng = pyproj.Proj(init='epsg:27700')
    Wgs84 = pyproj.Proj(init='epsg:4326')
    #print (lat+'-'+lon)
    wgsLon,wgsLat = pyproj.transform(Bng,Wgs84,lon, lat)
    return wgsLon,wgsLat


#-------- Buslines    
#create line URL
def createLine(busId):
    lineId = URIRef('http://data.linkedevents.org/transit/london/busLine/' + busId)
    return lineId

#create line geometry url
def createGeometryURL(busId):
    geometryURL = URIRef('http://data.linkedevents.org/transit/london/busLine/' + Literal(busId) + '/geometry')
    return geometryURL

def definePrefixes():

#Vocabularies   -- THIS SHOULD BE A CONSTRUCTED BASED ON THE A DICTONARY DEFINITION
    prefixes = {
        'dc': 'http://purl.org/dc/elements/1.1/',
        'dct': 'http://purl.org/dc/terms/',
        'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
        'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
        'geom': 'http://geovocab.org/geometry#',
        'geosparql': 'http://www.opengis.net/ont/geosparql#',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
        'locationOnt': 'http://data.linkedevents.org/def/location#',
        'locn': 'http://www.w3.org/ns/locn#',
        'naptan': 'http://transport.data.gov.uk/def/naptan/',
        'owl':'http://www.w3.org/2002/07/owl#',
        'schema':'http://schema.org/',
        'transit': 'http://vocab.org/transit/terms/',
        'unknown': 'http://data.linkedevents.org/def/unknown#',
        'xsd': 'http://www.w3.org/2001/XMLSchema#'}
    return prefixes

def bindingPrefixes(graphs,prefixes):
    for key in prefixes:
        graphs.bind(key, prefixes[key])
    return graphs

#creates graph of one bus stop
def createBusGraph(arg,g):
    dc = Namespace('http://purl.org/dc/elements/1.1/')
    dct = Namespace('http://purl.org/dc/terms/')
    dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
    geo = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
    geosparql = Namespace('http://www.opengis.net/ont/geosparql#')
    geom = Namespace('http://geovocab.org/geometry#')
    locn = Namespace('http://www.w3.org/ns/locn#')
    locationOnt = Namespace('http://data.linkedevents.org/def/location#')
    naptan = Namespace('http://transport.data.gov.uk/def/naptan/')
    rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
    schema = Namespace('http://schema.org/')
    transit = Namespace('http://vocab.org/transit/terms/')
    xsd = Namespace('http://www.w3.org/2001/XMLSchema#')

    singleStop = createBusStop(arg[0])
    singleAddress = createAddress(arg[13])
    singleGeometry = createGeometry(arg[13])
    busRoute = createBusStop(arg[0])

    g.add((singleStop, rdf.type, transit.Stop))
    g.add((singleStop, rdf.type, naptan.BusStop))
    g.add((singleStop, rdf.type, dul.Place))
    g.add((singleStop, dc.identifier, Literal(arg[0])))
    g.add((singleStop, rdfs.label, Literal(arg[5])))
    g.add((singleStop, geom.geometry, singleGeometry))
    g.add((singleStop, schema.geo, singleGeometry))
    g.add((singleStop, locn.address, singleAddress))
    g.add((singleStop, schema.location, singleAddress))
    #g.add((singleStop, transit.route, busRoute))

    g.add((singleStop,locationOnt.businesstype, URIRef('http://data.linkedevents.org/kos/3cixty/busstop') ))


    g.add((singleGeometry, rdf.type, geo.Point))
    g.add((singleGeometry, geo.lat, Literal(arg[2], datatype=xsd.placeholder)))
    g.add((singleGeometry, geo.long, Literal(arg[1], datatype=xsd.placeholder)))
    g.add((singleGeometry, locn.geometry, Literal(arg[3], datatype=geosparql.wktLiteral)))


    g.add((singleAddress, rdf.type, schema.PostalAddress))
    g.add((singleAddress, rdf.type, dct.Location))
    #g.add((singleAddress, dct.title, arg[5]))
    #g.add((singleAddress, schema.streetAddress, arg[7]))
    g.add((singleAddress, locn.address, arg[5]))
    #g.add((singleAddress, schema.addressLocality, arg[9]))
    #g.add((singleAddress, locn.adminUnitL12, arg[10]))#not returning anything interesting- is this necessary
    return g

def main():

    busPathf ='./'
    inFileB = busPathf + 'DATA/bus_validatedSMALL.csv'
    outFileB= busPathf + 'DATA/bus_dirtySMALL.ttl'

    csvB=readCsv(inFileB)
    busline_store = plugin.get('IOMemory', Store)()
    bus_g= Graph(busline_store)

    prefixes=definePrefixes()
    
    print('Binding Prefixes')
    bindingPrefixes(bus_g, prefixes)

    print('Creating graph-Bus...')
    for row in csvB:
        lstData = getBusData(row)
        createBusGraph(lstData,bus_g).serialize(outFileB,format='turtle')

    print ('DONE - Bus rdfy')
    
if __name__ == '__main__':
    main();


#def runGraph():
