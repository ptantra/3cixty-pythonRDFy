# ---- libraries

from rdflib import URIRef, Literal, Namespace, Graph
import csv
import uuid
import string
import random

# -------- This is an RDF superclass


class RDF:
    def __init__(self):  # common namespaces
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

    @staticmethod  # ------ UID Generator
    def getUID(value, namespace):
        idencode = value.encode('utf-8')
        uid = uuid.uuid5(namespace, idencode)
        return uid

# ------ This is the Bus class


class Bus(RDF):
    def __init__(self, stopId):
        RDF.__init__(self)
        self.geom = Namespace('http://geovocab.org/geometry#')  # specific namespaces
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

    def createLabel(self, label):
        title = Literal(str(label).title())
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

# ----- This is a Busline class


class Busline(RDF):
    def __init__(self, route, run, lat, long, label):
        RDF.__init__(self)
        self.sf = Namespace("http://www.opengis.net/ont/sf#")
        self.transit = Namespace('http://vocab.org/transit/terms/')

        self.route = route
        self.run = run
        self.lat = lat
        self.long = long
        self.wkt = "POINT (" + str(self.lat) + " " + str(self.long) + ")"
        self.label = Literal(str(label).title())

    @staticmethod
    def bindPrefixes(graph):
        prefixes = {
            'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
            'locn': 'http://www.w3.org/ns/locn#',
            'naptan': 'http://transport.data.gov.uk/def/naptan/',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'schema': 'http://schema.org/',
            'sf': 'http://www.opengis.net/ont/sf#',
            'transit': 'http://vocab.org/transit/terms/'
        }
        for key in prefixes:
            graph.bind(key, prefixes[key])
        return graph

    def createBusline(self):
        busline = URIRef('http://data.linkedevents.org/transit/London/busLine/' + Literal(self.route))
        return busline

    def createBuslineGeometry(self):
        buslineGeom = URIRef(self.createBusline() + '/geometry')
        return buslineGeom

    def createRoute(self):
        busRoute = URIRef('http://data.linkedevents.org/transit/London/route/' + Literal(self.route))
        return busRoute

    def createRouteService(self):
        routeService = URIRef('http://data.linkedevents.org/transit/London/service/' + Literal(self.route) + '_' + Literal(self.run))
        return routeService

    def createBuslineGraph(self, g):
        busline = self.createBusline()
        geom = self.createBuslineGeometry()
        route = self.createRoute()
        service = self.createRouteService()

        g.add((busline, self.rdf.type, self.transit.BusRoute))
        g.add((busline, self.geo.location, geom))
        g.add((busline, self.rdfs.label, self.label))
        g.add((busline, self.transit.RouteService, service))
        g.add((busline, self.transit.route, route))
        g.add((geom, self.rdf.type, self.sf.LineString))
        g.add((geom, self.locn.geometry, Literal(self.wkt, datatype=self.geosparql.wktLiteral)))

        return g

# ------ This is a Bus Correspondence class


class BusCorrespondence(Bus):
    def __init__(self, stopId, route, run, seq):
        RDF.__init__(self)
        self.transit = Namespace('http://vocab.org/transit/terms/')

        self.stopId = stopId
        self.route = route
        self.run = run
        self.seq = seq
        self.service = str(self.route) + '_' + str(self.run)

    @staticmethod
    def bindPrefixes(graph):
        prefixes = {
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'transit': 'http://vocab.org/transit/terms/',
            'xsd': 'http://www.w3.org/2001/XMLSchema#'
        }
        for key in prefixes:
            graph.bind(key, prefixes[key])
        return graph

    def createServiceStop(self):
        serviceStopId = URIRef('http://data.linkedevents.org/transit/London/serviceStop/' + Literal(self.service) + '/' + Literal(self.stopId))
        return serviceStopId

    def createService(self):
        service = URIRef('http://data.linkedevents.org/transit/London/service/' + Literal(self.service))
        return service

    def createBusCorrespondenceGraph(self, g):
        servStop = self.createServiceStop()
        stop = self.createBusStop()
        serv = self.createService()

        g.add((servStop, self.rdf.type, self.transit.ServiceStop))
        g.add((servStop, self.transit.service, serv))
        g.add((servStop, self.transit.sequence, Literal(self.seq, datatype=self.xsd.int)))
        g.add((servStop, self.transit.stop, stop))
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
        return locationResUID  # this returns a UUID starting with a letter!

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

    def createBuslineRDF(self, path):
        index = 0
        with open(path, 'r') as f:
            f.next()
            print 'Building the graph...'
            for line in csv.reader(f, dialect='excel', delimiter=','):
                self.data.append(Busline(line[0], line[1], line[2], line[3], line[4]))
        for item in self.data:
            item.createBuslineGraph(self.g)
            print 'Graph extended ' + str(index) + ' entities.'
            index += 1
        print 'Graph complete with ' + str(index) + ' Busline entities.'
        Busline.bindPrefixes(self.g)
        return self.g

    def createBusCorrespondenceRDF(self, path):
        index = 0
        with open(path, 'r') as f:
            f.next()
            print 'Building the graph...'
            for line in csv.reader(f, dialect='excel', delimiter=','):
                self.data.append(BusCorrespondence(line[0], line[1], line[2], line[3]))
        for item in self.data:
            item.createBuslineGraph(self.g)
            print 'Graph extended ' + str(index) + ' entities.'
            index += 1
        print 'Graph complete with ' + str(index) + ' Bus Correspondence entities.'
        BusCorrespondence.bindPrefixes(self.g)
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

# ---- Airbnb

airbnb_content = rdf.createAirbnbRDF('/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyHotel/airbnbModule/london/DATA/airbnbLondon_validated.csv')
airbnb_path = '/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyHotel/airbnbModule/london/DATA/airbnbSimple2.ttl'
#main(airbnb_content, airbnb_path)

#----- Bus

bus_content = rdf.createBusStopRDF('/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopCodeOnly.csv')
bus_path = '/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopSimple.ttl'
main(bus_content, bus_path)

