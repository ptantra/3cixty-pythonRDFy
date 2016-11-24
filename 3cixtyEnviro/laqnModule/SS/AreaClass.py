from rdflib import URIRef, Namespace, Graph
from rdflib import Literal
import uuid
import csv
from rdflib import XSD
import random
import string

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
            #'xsd': 'http://www.w3.org/2001/XMLSchema#',
            'owl': 'http://www.w3.org/2002/07/owl#',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'locationOnt': 'http://data.linkedevents.org/def/location#',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'travel': 'http://3cixty.com/ontology#',
            'qb': 'http://purl.org/linked-data/cube#',
            'dct': 'http://purl.org/dc/terms/',
            'sf': 'http://www.opengis.net/ont/sf#',
            'acco': 'http://purl.org/acco/ns#',
            'gr': 'http://purl.org/goodrelations/v1#',
            'locationRes': 'http://data.linkedevents.org/location/',
            'rev': 'http://purl.org/stuff/rev#',
            'sioc': 'http://rdfs.org/sioc/ns#',
            'seegrid': 'http://def.seegrid.csiro.au/isotc211/iso19115/2003/code/MaintenanceFrequency/'
            }

    def namespaces(self):
        for prefix, namespace in self.namespace_manager.namespaces():
            yield prefix, namespace

    def bindingPrefixes(self, g):
        for key in self.prefixes:
            self.g.bind(key, URIRef(self.prefixes[key]))
        return self.g

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
        #self.xsd = Namespace('http://www.w3.org/2001/XMLSchema#')
        self.owl = Namespace('http://www.w3.org/2002/07/owl#')
        self.rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        self.locationOnt = Namespace("http://data.linkedevents.org/def/location#")
        self.dul = Namespace('http://ontologydesignpatterns.org/ont/dul/DUL.owl#')
        self.dc = Namespace('http://purl.org/dc/elements/1.1/')
        self.travel = Namespace('http://3cixty.com/ontology#')
        self.qb = Namespace('http://purl.org/linked-data/cube#')
        self.dct = Namespace('http://purl.org/dc/terms/')
        self.sf = Namespace("http://www.opengis.net/ont/sf#")
        self.locationRes = Namespace('http://data.linkedevents.org/location/')
        self.acco = Namespace("http://purl.org/acco/ns#")
        self.gr = Namespace('http://purl.org/goodrelations/v1#')
        self.rev = Namespace('http://purl.org/stuff/rev#')
        self.sioc = Namespace('http://rdfs.org/sioc/ns#')
        self.seegrid = Namespace('http://def.seegrid.csiro.au/isotc211/iso19115/2003/code/MaintenanceFrequency/')


class Area(RDF):
    def __init__(self, name, code, geom):
        RDF.__init__(self)
        self.name = str(name).strip()
        self.code = str(code).strip()
        self.geom = geom

    def createArea(self):
        area = URIRef('http://data.linkedevents.org/transit/London/area/' + Literal(self.code))
        return area

    def createAreaGeom(self):
        areaGeom = URIRef(self.createArea() + '/geometry')
        return areaGeom


    def createAreaGraph(self, g):
        area = self.createArea()
        geom = self.createAreaGeom()
        g.add((area, self.rdf.type, self.schema.AdministrativeArea))
        g.add((area, self.rdfs.label, Literal(self.name.title())))
        g.add((area, self.dct.identifier, Literal(self.code)))
        g.add((area, self.geo.location, geom))
        g.add((geom, self.locn.geometry, Literal(self.geom)))
        return g

class RDFCreator:
    def __init__(self):
        self.data = []
        self.g = Graph()
        tree = Tree(self.g)
        tree.bindingPrefixes(self.g)

    def createHotelObj(self, path):
        with open(path, 'rU') as f:
            f.next()
            for line in csv.reader(f, dialect='excel'):
                self.data.append(Hotel(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))
            return self.data

    def createArea(self, path):
        with open(path, 'rU') as f:
            f.next()
            for line in csv.reader(f, dialect='excel'):
                self.data.append(Area(line[0], line[1], line[2]))
            return self.data

    #def createNt(self):
        #for i in self.data:
            #i.createNtGraph(self.g)
        #return self.g

    def createRDF(self):
        for i in self.data:
            i.createGraph(self.g)
        return self.g

def mainArea(source, ntpath, ttlpath):
    rdf = RDFCreator()
    rdf.createArea(source)
    #rdf.createNt().serialize(format='nt', destination=ntpath)
    rdf.createRDF().serialize(format='turtle', destination=ttlpath)
    #next(reader, None)
    print('The files in place.')

source = '/Users/patrick/3cixty/IN/London DataStore/151124/carbon-emissions-boroughTOTAL.csv'
ntpath = '/Users/patrick/3cixty/IN/London DataStore/151124/carbon-emissions-boroughTOTAL.ttl'
ttlpath = '/Users/patrick/3cixty/IN/London DataStore/151124/carbon-emissions-boroughTOTAL2.ttl'

mainArea(source, ntpath, ttlpath) #uncomment to run