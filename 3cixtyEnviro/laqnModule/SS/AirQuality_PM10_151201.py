import csv
import uuid
import pyproj
import random
from random import seed
import string
from rdflib import URIRef, Literal, Namespace, plugin, Graph, BNode
from rdflib.store import Store
import time

start_time = time.time()

def readCsv(inputfile):
    try:
        f = open(inputfile, 'rU')
        rf = csv.reader(f, delimiter=',')
        return rf
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        raise

def getUid(r0):#use this script to create NON-COMPLIANT uuid
    hotelUri = Namespace("http://data.linkedevents.org/places/London/hotels")
    idencode = r0.encode('utf-8')
    uid = uuid.uuid5(hotelUri, idencode)
    return uid

def definePrefixes():
    prefixes = {'schema': 'http://schema.org/',
                'owl': 'http://www.w3.org/2002/07/owl#',
                'xsd': 'http://www.w3.org/2001/XMLSchema#',
                'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                'locationOnt': 'http://data.linkedevents.org/def/location#',
                'locationRes': 'http://data.linkedevents.org/location/',
                'geom': 'http://geovocab.org/geometry#',
                'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
                'gsp': 'http://www.opengis.net/ont/geosparql#',
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                'dcterms': 'http://purl.org/dc/terms/',
                'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
                'locn': 'http://www.w3.org/ns/locn#',
                'foaf': 'http://xmlns.com/foaf/0.1/',
                'dc': 'http://purl.org/dc/elements/1.1/',
                #'time': 'http://www.w3.org/2006/time#',
                'acco': 'http://purl.org/acco/ns#',
                'gr': 'http://purl.org/goodrelations/v1#',
                'envo': 'http://purl.obolibrary.org/obo/#',
                'time':'http://www.w3.org/TR/owl-time#',
                'gn':'http://www.geonames.org/ontology/#',
                'qb':'http://purl.org/linked-data/cube#',
                'org':'http://www.w3.org/ns/org#',
                'sdmx_dimension':'http://purl.org/linked-data/sdmx/2009/dimension#',
                'sdmx': 'http://purl.org/linked-data/sdmx#'}
    return prefixes

def bindingPrefixes(g, prefixes):
    for key in prefixes:
        g.bind(key, prefixes[key])
    return g

def createAirQualityId(airQualId):
    airQualId = URIRef('http://data.linkedevents.org/places/London/environment/' + airQualId)
    return airQualId

def createArea():
    area = URIRef('http://data.linkedevents.org/environment/London/area/' + Literal())
    return area

def createAreaGeom():
    areaGeom = URIRef(createArea() + '/geometry')
    return areaGeom

def getAirQualData(row):
    airQualId = row[0]
    airQualGUID = getUid(row[0])
    airQualTitle = Literal(str(row[0]))
    #airQualSpatial= row[2]
    airQualDateTime = row[2]
    airQualPM10 = row[3]
    airQualRatified=row[5]
    airQualPublisher = URIRef('http://www.londonair.org.uk/london/asp/')

    lst = [airQualId, airQualGUID, airQualTitle,
           airQualDateTime, airQualPM10,airQualRatified,
           airQualPublisher]
    return lst

def createAirQualGraph(arg, g):
    schema = Namespace("http://schema.org/")
    xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    locationOnt = Namespace("http://data.linkedevents.org/def/location#")
    geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    gs = Namespace("http://www.opengis.net/ont/geosparql#")
    locn = Namespace("http://www.w3.org/ns/locn#")
    dc = Namespace("http://purl.org/dc/elements/1.1/")
    rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    acco = Namespace("http://purl.org/acco/ns#")
    gr = Namespace('http://purl.org/goodrelations/v1#')
    foaf = Namespace('http://xmlns.com/foaf/0.1/')
    dcterms = Namespace('http://purl.org/dc/terms/')
    dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
    envo = Namespace('http://purl.obolibrary.org/obo/#')
    time = Namespace('http://www.w3.org/TR/owl-time#')
    gn= Namespace('http://www.geonames.org/ontology/#')
    qb=Namespace('http://purl.org/linked-data/cube#')
    org =Namespace('http://www.w3.org/ns/org#')
    sdmx = Namespace('http://purl.org/linked-data/sdmx#')
    sdmx_dimension=Namespace('http://purl.org/linked-data/sdmx/2009/dimension#')

    #area = createArea()
    area = URIRef('http://data.linkedevents.org/places/London/area/' + Literal(arg[0]))
    #geom = createAreaGeom()
    geom = URIRef('http://data.linkedevents.org/places/London/area/' + Literal(arg[0])) +'/geometry'
    measurePM10 = URIRef("http://data.linkedevents.org/location/airquality/" + "%s" + "/PM10") % arg[0]


    g.add((area, rdf.type, qb.DataStructureDefinition))
    g.add((area, rdf.type, dul.Place))
    g.add((area, rdf.type, schema.Place))
    g.add((area, rdfs.label, Literal(arg[2])))
    g.add((area, rdfs.subPropertyOf, sdmx_dimension.refArea))
    g.add((area, dcterms.identifier, Literal(arg[0])))
    g.add((area, dcterms.publisher, Literal(arg[6])))
    g.add((area, geo.location, geom))
    g.add((area, envo.EnvironmentalMaterial, measurePM10))
    g.add((area, org.organisation, Literal('Kings College')))

    g.add((geom, rdf.type, geo.Multipolygon))
    g.add((geom, locn.geometry, Literal(arg[3])))

    g.add((measurePM10, rdf.type, envo.EnvironmentalMaterial))
    g.add((measurePM10, rdfs.comment, Literal('PM10 particulates measured in ug m-3 reference equiv by VCM')))
    g.add((measurePM10, dcterms.description, Literal('PM10 particulates measured in ug m-3 reference equiv by VCM')))
    g.add((measurePM10, dcterms.issued, Literal(arg[3], datatype=xsd.dateTime)))
    g.add((measurePM10, dcterms.subject, Literal('PM10 particulates')))
    g.add((measurePM10, envo.PM10, Literal(arg[4], datatype=xsd.floating)))

    prefixes=definePrefixes()
    bindingPrefixes(g, prefixes)

    return g

def main():
    pathf = "/Users/patrick/3cixty/IN/Kings/151201/"
    inFile = pathf + "LaqnDataSAMPLE.csv"
    outFile = pathf + "LaqnDataSAMPLE.ttl"

    csv = readCsv(inFile)
    next(csv, None)  # FILE WITH HEADERS

    store = plugin.get('IOMemory', Store)()
    g = Graph(store)

    prefixes = definePrefixes()
    print('Binding Prefixes')
    bindingPrefixes(g, prefixes)

    print('Creating graph-air quality...')

    for row in csv:
        lstData = getAirQualData(row)
        createAirQualGraph(lstData, g).serialize(outFile, format='turtle')

    print ('DONE! Time elapsed ' + str((time.time() - start_time)))

if __name__ == "__main__":
    main()
