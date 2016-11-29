#libraries
import rdflib
from rdflib import URIRef, Literal, Namespace, plugin, Graph
import csv

# This is an object that can bind its prefixes
class Tree:
    def __init__(self, g):
        self.g = g
        self.prefixes = {'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#',
            'foaf': 'http://xmlns.com/foaf/0.1/',
            'geom': 'http://geovocab.org/geometry#',
            'transit': 'http://vocab.org/transit/terms/',
            'locn': 'http://www.w3.org/ns/locn#',
            'vcard': 'http://www.w3.org/2006/vcard/ns#',
            'dcterms': 'http://purl.org/dc/terms/',
            'schema': 'http://schema.org/',
            'geosparql': 'http://www.opengis.net/ont/geosparql#',
            'unknown': 'http://data.linkedevents.org/def/unknown#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'dul': 'http://ontologydesignpatterns.org/ont/dul/DUL.owl#',
            'naptan': 'http://transport.data.gov.uk/def/naptan/',
            'xsd': 'http://www.w3.org/2001/XMLSchema#',
            'owl': 'http://www.w3.org/2002/07/owl#',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'locationOnt': 'http://data.linkedevents.org/def/location#',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'travel': 'http://3cixty.com/ontology#',
            'qb': 'http://purl.org/linked-data/cube#',
            'dct': 'http://purl.org/dc/terms/',
            'sf': 'http://www.opengis.net/ont/sf#'}

    def bindingPrefixes(self, g):
        self.g = g
        for key in self.prefixes:
            self.g.bind(key, self.prefixes[key])
        return self.g

# This is an RDF superclass that knows all the namespaces
class RDF:
    def __init__(self):
        self.geo = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
        self.foaf = Namespace("http://xmlns.com/foaf/0.1/")
        self.geom = Namespace("http://geovocab.org/geometry#")
        self.unknown = Namespace("http://data.linkedevents.org/def/unknown#")
        self.transit = Namespace("http://vocab.org/transit/terms/")
        self.locn = Namespace("http://www.w3.org/ns/locn#")
        self.vcard = Namespace('http://www.w3.org/2006/vcard/ns#')
        self.dcterms = Namespace("http://purl.org/dc/terms/")
        self.schema = Namespace('http://schema.org/')
        self.geosparql = Namespace("http://www.opengis.net/ont/geosparql#")
        self.rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
        self.naptan = Namespace('http://transport.data.gov.uk/def/naptan/')
        self.xsd = Namespace('http://www.w3.org/2001/XMLSchema#')
        self.owl = Namespace('http://www.w3.org/2002/07/owl#')
        self.rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        self.locationOnt = Namespace("http://data.linkedevents.org/def/location#")
        self.dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
        self.dc = Namespace('http://purl.org/dc/elements/1.1/')
        self.travel = Namespace('http://3cixty.com/ontology#')
        self.qb = Namespace('http://purl.org/linked-data/cube#')
        self.dct = Namespace('http://purl.org/dc/terms/')
        self.sf = Namespace("http://www.opengis.net/ont/sf#")

# ------ This is the Bus class

class Bus(RDF):
    def __init__(self, stopId):
        RDF.__init__(self)
        self.stopId = stopId

    def createBusStop(self):
        busStop = URIRef("http://data.linkedevents.org/transit/London/stop/" + Literal(self.stopId).replace(" ", ""))
        return busStop

    def createBusGraph(self, g):
        busStop = self.createBusStop()
        g.add((busStop, self.rdf.type, self.naptan.BusStop))
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
            print 'Graph extended ' + str(index)
            index +=1
        return self.g

# -------- Main
def main(content, path):
    tree = Tree(content)
    tree.bindingPrefixes(content)
    content.serialize(destination=path, format='turtle')
    print('The file in place.')

# -------- Execution
rdf = RDFCreator()
main(rdf.createBusStopRDF('/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopCodeOnly.csv'), '/Users/Agata/Desktop/3cixty-pythonRDFy/3cixtyTransport/busModule/DATA/busStopCodeOnly.ttl')