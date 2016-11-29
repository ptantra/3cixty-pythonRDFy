#libraries
import rdflib
from rdflib import URIRef, Literal, Namespace, Graph
import csv

# This is an object that can bind its prefixes
class Tree:
    def __init__(self, g):
        self.g = g
        self.prefixes = {
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
            'xsd': 'http://www.w3.org/2001/XMLSchema#'
        }

    def bindingPrefixes(self, g):
        self.g = g
        for key in self.prefixes:
            self.g.bind(key, self.prefixes[key])
        return self.g

# This is an RDF superclass that knows all the namespaces
class RDF:
    def __init__(self):
        self.dc = Namespace('http://purl.org/dc/elements/1.1/')
        self.dct = Namespace('http://purl.org/dc/terms/')
        self.dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
        self.geo = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
        self.geom = Namespace('http://geovocab.org/geometry#')
        self.geosparql = Namespace('http://www.opengis.net/ont/geosparql#')
        self.rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        self.rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
        self.locationOnt = Namespace('http://data.linkedevents.org/def/location#')
        self.locn = Namespace('http://www.w3.org/ns/locn#')
        self.naptan = Namespace('http://transport.data.gov.uk/def/naptan/')
        self.owl = Namespace('http://www.w3.org/2002/07/owl#')
        self.schema = Namespace('http://schema.org/')
        self.transit = Namespace('http://vocab.org/transit/terms/')
        self.unknown = Namespace('http://data.linkedevents.org/def/unknown#')
        self.xsd = Namespace('http://www.w3.org/2001/XMLSchema#')

# ------ This is the Bus class

class Bus(RDF):
    def __init__(self, stopId):
        RDF.__init__(self)
        self.stopId = stopId.replace(" ", "")

    def createBusStop(self):
        busStop = URIRef("http://data.linkedevents.org/transit/stop/" + Literal(self.stopId))
        return busStop

    def createGeometry(self):
        busStopGeom = URIRef('http://data.linkedevents.org/London/location/' + Literal(self.stopId) + '/geometry')
        return busStopGeom

    def createAddress(self):
        stopAddress = URIRef('http://data.linkedevents.org/location/' + Literal(self.stopId) + '/address')
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

# ----- This is an RDF creator

class RDFCreator:
    def __init__(self):
        self.data = []
        self.g = Graph()

    def createBusStopRDF(self, path):
        index = 0
        with open(path, 'r') as f:
            f.next()
            for line in csv.reader(f, dialect='excel', delimiter=','):
                self.data.append(Bus(line[0]))
        for item in self.data:
            item.createBusGraph(self.g)
            print 'Graph extended ' + str(index) + ' entities.'
            index +=1
        return self.g

# -------- Main
def main(content, path):
    print "Generating file... Wait."
    tree = Tree(content)
    tree.bindingPrefixes(content)
    content.serialize(destination=path, format='turtle')
    print('The file in place.')

# -------- Execution
rdf = RDFCreator()
main(rdf.createBusStopRDF('/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopCodeOnly.csv'), '/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopCodeOnly.ttl')