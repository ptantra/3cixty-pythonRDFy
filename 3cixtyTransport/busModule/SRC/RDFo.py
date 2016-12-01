# ---- libraries
import rdflib
from rdflib import URIRef, Literal, Namespace, Graph
import csv, uuid
import string, random


# -------- This is an RDF superclass

class RDF:
    def __init__(self): # common namespaces
        self.dc = Namespace('http://purl.org/dc/elements/1.1/')
        self.dct = Namespace('http://purl.org/dc/terms/')
        self.dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
        self.geo = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
        self.geosparql = Namespace('http://www.opengis.net/ont/geosparql#')
        self.locationOnt = Namespace('http://data.linkedevents.org/def/location#')
        self.locn = Namespace('http://www.w3.org/ns/locn#')
        self.rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        self.rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
        self.schema = Namespace('http://schema.org/')
        self.unknown = Namespace('http://data.linkedevents.org/def/unknown#')
        self.xsd = Namespace('http://www.w3.org/2001/XMLSchema#')

    @staticmethod # ------ UID Generator
    def getUID(value, namespace):
        idencode = value.encode('utf-8')
        uid = uuid.uuid5(namespace, idencode)
        return uid


# ------ This is the Bus class

class Bus(RDF):
    def __init__(self, stopId):
        RDF.__init__(self)
        self.geom = Namespace('http://geovocab.org/geometry#') # specific namespaces
        self.naptan = Namespace('http://transport.data.gov.uk/def/naptan/')
        self.transit = Namespace('http://vocab.org/transit/terms/')

        self.stopId = stopId
        self.stopUID = RDF.getUID(self.stopId, self.naptan)

    @staticmethod
    def bindPrefixes(graph):
        prefixes = {
            'dc': 'http://purl.org/dc/elements/1.1/',
            'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
            'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
            'geom': 'http://geovocab.org/geometry#',
            'naptan': 'http://transport.data.gov.uk/def/naptan/',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'schema': 'http://schema.org/',
            'transit': 'http://vocab.org/transit/terms/'
        }
        for key in prefixes:
            graph.bind(key, prefixes[key])
        return graph

    def createBusStop(self):
        busStop = URIRef("http://data.linkedevents.org/transit/stop/" + Literal(self.stopUID))
        return busStop

    def createGeometry(self):
        busStopGeom = URIRef('http://data.linkedevents.org/London/location/' + Literal(self.stopUID) + '/geometry')
        return busStopGeom

    def createAddress(self):
        stopAddress = URIRef('http://data.linkedevents.org/location/' + Literal(self.stopUID) + '/address')
        return stopAddress

    def createLabel(self):
        title = Literal(str(self.label).title())
        return title

    def createBusGraph(self, g):
        busStop = self.createBusStop()
        address = self.createAddress()
        geom = self.createGeometry()
        #label = Literal(self.createLabel())

        g.add((busStop, self.rdf.type, self.naptan.BusStop))
        g.add((busStop, self.rdf.type, self.dul.Place))
        g.add((busStop, self.rdf.type, self.transit.Stop))
        g.add((busStop, self.dc.identifier, Literal(self.stopId)))
        g.add((busStop, self.geom.geometry, geom))

        g.add((busStop, self.geo.location, geom))
        g.add((busStop, self.schema.location, address))

        return g

# ----- This is the Airbnb class

class Airbnb(RDF):
    def __init__(self, objectId, label, area, lat, long):
        RDF.__init__(self)
        self.acco = Namespace('http://purl.org/acco/ns#')
        self.gr =  Namespace('http://purl.org/goodrelations/v1#')
        self.owl = Namespace('http://www.w3.org/2002/07/owl#')
        self.threecixtyKOS = Namespace('http://data.linkedevents.org/kos/3cixty/')
        self.locationRes = Namespace('http://data.linkedevents.org/location/')

        self.objectId = objectId
        self.placeUID = self.createLocationResUID()
        self.label = label
        self.area = area
        self.lat = lat
        self.long = long
        self.wkt = "POINT (" + str(self.lat) + " " + str(self.long) + ")"
        self.publisher = URIRef('https://www.airbnb.co.uk')
        self.country = Literal('UK')

    @staticmethod
    def bindPrefixes(graph):
        prefixes = {
            'acco': 'http://purl.org/acco/ns#',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
            'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
            'geosparql': 'http://www.opengis.net/ont/geosparql#',
            'locationOnt': 'http://data.linkedevents.org/def/location#',
            'locationRes': 'http://data.linkedevents.org/location/',
            'locn': 'http://www.w3.org/ns/locn#',
            'owl': 'http://www.w3.org/2002/07/owl#',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'schema': 'http://schema.org/',
            'threecixtyKOS': 'http://data.linkedevents.org/kos/3cixty/',
            'xsd': 'http://www.w3.org/2001/XMLSchema#'
        }
        for key in prefixes:
            graph.bind(key, prefixes[key])
        return graph

    def createLocationResUID(self):
        hotelUri = Namespace("http://data.linkedevents.org/places/london/hotels")
        idencode = str(self.objectId)
        uid = RDF.getUID(idencode, hotelUri)
        puid = URIRef("http://data.linkedevents.org/location/" + Literal(uid))
        uuidList = list(puid)
        chars = string.ascii_letters
        random.seed(101)  # set seed so the random number generated is replicable in the next iteration
        newId = ''.join(random.choice(chars))
        uuidList[38] = newId
        locationResUID = ''.join(uuidList).lower()
        return locationResUID # this returns a UUID starting with a letter!

    def createPlace(self):
        placeURI = URIRef(self.placeUID)
        return placeURI

    def createGeometry(self):
        placeGeom = URIRef(self.placeUID + '/geometry')
        return placeGeom

    def createAddress(self):
        placeAddress = URIRef(self.placeUID + '/address')
        return placeAddress

    def createSameAsLink(self):
        sameAsLink = URIRef("http://www.airbnb.co.uk/rooms/" + str(self.objectId))
        return sameAsLink

    def createPlaceGraph(self, g):
        place = self.createPlace()
        geom = self.createGeometry()
        address = self.createAddress()
        sameAsLink = self.createSameAsLink()

        g.add((place, self.rdf.type, self.dul.Place))
        g.add((place, self.rdf.type, self.acco.Hotel))
        g.add((place, self.rdfs.label, Literal(self.label)))
        g.add((place, self.locationOnt.businessType, self.threecixtyKOS.residence))
        g.add((place, self.dc.identifier, Literal(self.objectId)))
        g.add((place, self.dc.publisher, self.publisher))
        g.add((place, self.owl.sameAs, sameAsLink))
        g.add((place, self.schema.location, address))
        g.add((place, self.geo.location, geom))

        g.add((geom, self.rdf.type, self.geo.Point))
        g.add((geom, self.geo.lat, Literal(self.lat, datatype=self.xsd.placeholder)))
        g.add((geom, self.geo.long, Literal(self.long, datatype=self.xsd.placeholder)))
        g.add((geom, self.locn.geometry, Literal(self.wkt, datatype=self.geosparql.wktLiteral)))

        g.add((address, self.rdf.type, self.schema.postalAddress))
        g.add((address, self.schema.addressCountry, self.country))
        g.add((address, self.schema.addressLocality, Literal(self.area)))

        return g

# ----- This is an RDF creator

class RDFCreator:
    def __init__(self):
        self.data = []
        self.g = Graph()

    def createBusStopRDF(self, path):
        index = 0
        with open(path, 'r') as f:
            f.next()
            print 'Building the graph...'
            for line in csv.reader(f, dialect='excel', delimiter=','):
                self.data.append(Bus(line[0]))
        for item in self.data:
            item.createBusGraph(self.g)
            print 'Graph extended ' + str(index) + ' entities.'
            index +=1
        print 'Graph complete with ' + str(index) + ' Bus entities.'
        Bus.bindPrefixes(self.g)
        return self.g

    def createAirbnbRDF(self, path):
        index = 0
        with open(path, 'r') as f:
            f.next()
            print 'Building the graph...'
            for line in csv.reader(f, dialect='excel', delimiter=','):
                self.data.append(Airbnb(line[0], line[13], line[2], line[3], line[4]))
        for item in self.data:
            item.createPlaceGraph(self.g)
            print 'Graph extended ' + str(index) + ' entities.'
            index += 1
        print 'Graph complete with ' + str(index) + ' Airbnb entities.'
        Airbnb.bindPrefixes(self.g)
        return self.g


# -------- Main
def main(content, path):
    print "Generating file... Wait."
    content.serialize(destination=path, format='turtle')
    print('The file in place.')

# -------- Execution
rdf = RDFCreator()
#main(rdf.createBusStopRDF('/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopCodeOnly.csv'), '/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopSimple.ttl')
main(rdf.createAirbnbRDF('/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyHotel/airbnbModule/london/DATA/airbnbLondon_validated.csv'), '/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyHotel/airbnbModule/london/DATA/airbnbSimple2.ttl')

