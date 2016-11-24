import csv
import uuid
import pyproj
import random
from random import seed
import string
from rdflib import URIRef, Literal, Namespace, plugin, Graph, BNode, Dataset, ConjunctiveGraph
from rdflib.store import Store
from rdflib.term import bind
import time
from rdflib.collection import Collection

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
                'time':'http://www.w3.org/TR/owl-time#',
                'gn':'http://www.geonames.org/ontology/#',
                'qb':'http://purl.org/linked-data/cube#',
                'org':'http://www.w3.org/ns/org#',
                'sdmx_dimension':'http://purl.org/linked-data/sdmx/2009/dimension#',
                'sdmx_subject': 'http://purl.org/linked-data/sdmx/2009/subject#',
                'sdmx_attribute':'http://purl.org/linked-data/sdmx/2009/attribute#',
                'skos' : 'http://www.w3.org/2004/02/skos/core#',
                'sdmx': 'http://purl.org/linked-data/sdmx#',
                'ex_geo' : 'http://example.org/geo#'}
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
    gr = Namespace('http://purl.org/goodrelations/v1#')
    foaf = Namespace('http://xmlns.com/foaf/0.1/')
    dcterms = Namespace('http://purl.org/dc/terms/')
    dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
    time = Namespace('http://www.w3.org/TR/owl-time#')
    gn= Namespace('http://www.geonames.org/ontology/#')
    qb=Namespace('http://purl.org/linked-data/cube#')
    org =Namespace('http://www.w3.org/ns/org#')
    sdmx = Namespace('http://purl.org/linked-data/sdmx#')
    sdmx_dimension=Namespace('http://purl.org/linked-data/sdmx/2009/dimension#')
    sdmx_subject=Namespace('http://purl.org/linked-data/sdmx/2009/subject#/')
    sdmx_attribute=Namespace('http://purl.org/linked-data/sdmx/2009/attribute#')
    skos = Namespace('http://www.w3.org/2004/02/skos/core#')

    #area = createArea()

    ds = URIRef('http://data.linkedevents.org/places/London/area/' + Literal(arg[0]))


    ds_pm10 = Dataset()
    ds_pm10.add=((URIRef('http://data.linkedevents.org/places/London/environment/'),
                  URIRef('http://data.linkedevents.org/places/London/environment/CO2'),
                  Literal('Dataset 1')))
    g2 = ds_pm10.graph(URIRef('http://data.linkedevents.org/places/London/environment/CO2/dataset1'))

    g=ConjunctiveGraph()
    #ds2 = URIRef('http://data.linkedevents.org/places/London/area2/' + Literal(arg[0]))
    #geom = createAreaGeom()
    #geom = URIRef('http://data.linkedevents.org/places/London/area/' + Literal(arg[0])) +'/geometry'
    #measurePM10 = URIRef("http://data.linkedevents.org/location/airquality/" + "%s" + "/PM10") % arg[0]
    #sdmxText= sdmx_subject.Literal('3.1')

    #####using structure copied from http://publishing-statistical-data.googlecode.com/svn/trunk/specs/src/main/html/cube.html
    g.add((ds, rdf.type, qb.DataStructureDefinition))
    g.add((ds, qb.ComponentProperty, Literal('unknown')))
    g.add((ds, qb.MeasureProperty, Literal('PM 10')))
    g.add((ds, qb.CodeList, skos.Concept))
    g.add((ds, rdfs.comment, Literal('London air pollutant (PM10) measures', lang= 'en')))
    g.add((ds, qb.Component, qb.dimension))
    g.add((ds, dcterms.publisher, Literal(arg[6])))
    #g.quads((ds, qb.dimension, sdmx_dimension.refArea, qb['order 2']))
    #g.quads((ds, qb.dimension, sdmx_dimension.refPeriod, qb['order 1']))

    g.add((skos.Concept, rdf.type, dcterms.subject))
    g.add((skos.Concept, skos.broadest, sdmx_subject[2]))
    g.add((skos.Concept, skos.notation, Literal('2')))
    g.bind('sdmx_subject', sdmx_subject)

    g.add((ds_pm10, rdf.type, qb.DataSet))
    g.add((ds_pm10, dcterms.title, Literal('London air pollutant (PM10) measures', lang= 'en')))
    g.add((ds_pm10, rdfs.label, Literal('London air pollutant (PM10) measures', lang= 'en')))
    g.add((ds_pm10, rdfs.comment, Literal('Yearly London air pollutant (PM10) measures', lang= 'en')))
    g.add((ds_pm10, dcterms.description, Literal('Yearly London air pollutant (PM10) measures', lang= 'en')))
    g.add((ds_pm10, dcterms.identifier, Literal(arg[0])))
    g.add((ds_pm10, qb.structure, Literal('dsd1')))
    g.add((ds_pm10, dcterms.issued, Literal('2013', datatype=xsd.gYear)))
    g.add((ds_pm10, dcterms.subject, sdmx_subject["3.1"]))
    g.add((sdmx_subject["3.4"], dcterms.subject,ds_pm10 ))
    g.add((ds_pm10, dcterms.subject, geo.UK))
    #g.add((ds_pm10, sdmx_attribute.unitMeasure, URIRef('http://dbpedia.org/resource/Year')))
    #g.add((ds_pm10, qb.slice, Literal('slice 1')))
    #g.add((ds_pm10, qb.slice, Literal('slice 2')))
    #g.add((ds_pm10, qb.slice, Literal('slice 3')))
    #g.add((ds_pm10, qb.slice, Literal('slice 4')))
    #g.add((ds_pm10, qb.slice, Literal('slice 5')))
    #g.add((ds_pm10, qb.slice, Literal('slice 6')))


    #g.add((ds_pm10,rdf.type, qb.DataStructureDefinition))
    #g.add((ds_pm10, qb.component, qb.dimension))
    #g.add((ds_pm10, qb.dimension, Literal('refArea')))
    #g.add((ds_pm10, qb.order, Literal('1')))
    #g.add((ds_pm10, qb.dimension, Literal('refPeriod')))
    #g.add((ds_pm10, qb.order, Literal('2')))
    #g.add((ds_pm10, qb.componentAttachment, qb.Slice))

    #g.add((dataset, envo.EnvironmentalMaterial, measurePM10))
    #g.add((dataset, org.organisation, Literal('Kings College')))

    #g.add((geom, rdf.type, geo.Multipolygon))
    #g.add((geom, locn.geometry, Literal(arg[3])))

    #g.add((measurePM10, rdf.type, envo.EnvironmentalMaterial))
    ##g.add((measurePM10, rdfs.comment, Literal('PM10 particulates measured in ug m-3 reference equiv by VCM')))
   # g.add((measurePM10, dcterms.description, Literal('PM10 particulates measured in ug m-3 reference equiv by VCM')))
    #g.add((measurePM10, dcterms.issued, Literal(arg[3], datatype=xsd.dateTime)))
    #g.add((measurePM10, dcterms.subject, Literal('PM10 particulates')))
    #g.add((measurePM10, envo.PM10, Literal(arg[4], datatype=xsd.floating)))

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
