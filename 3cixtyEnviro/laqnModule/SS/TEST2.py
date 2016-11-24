__author__ = 'patrick'

from rdflib import ConjunctiveGraph, URIRef, plugin, Literal, Graph, BNode, Namespace, Dataset
from rdflib.store import Store
from rdflib import RDF, RDFS, OWL
from rdflib.namespace import VOID, RDF
from rdflib.collection import Collection
from pprint import pprint

sdmx_attribute=Namespace('http://purl.org/linked-data/sdmx/2009/attribute#')
qb= Namespace('http://purl.org/linked-data/cube#')
org =Namespace('http://www.w3.org/ns/org#')
sdmx = Namespace('http://purl.org/linked-data/sdmx#')
sdmx_dimension=Namespace('http://purl.org/linked-data/sdmx/2009/dimension#')
sdmx_subject=Namespace('http://purl.org/linked-data/sdmx/2009/subject#/')
sdmx_attribute=Namespace('http://purl.org/linked-data/sdmx/2009/attribute#')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
foaf=Namespace('http://xmlns.com/foaf/0.1/')

store = plugin.get('IOMemory', Store)()

gc=ConjunctiveGraph(store)
context=URIRef('http://source.data.gov.uk/dsd/coins')
context2=URIRef('http://source.data.gov.uk/dsd/coinsDATA2')


ds = Dataset()
ds.add((context, sdmx_dimension.refPeriod, Literal('graph1')))
ds.bind('sdmx_dimension', sdmx_dimension)
dsMother = ds.graph(URIRef('http://source.data.gov.uk/dsd/coinsCONTAINER_GRAPH'))
dsMother.add((context2, sdmx_dimension.whatever, Literal('graph2')))
dsMother.bind('sdmx_dimension', sdmx_dimension)

gc.add((context,RDF.type,qb.DataStructureDefinition))
gc.add((context,qb.componentProperty,sdmx_dimension.refPeriod, qb))
gc.bind('sdmx_dimension', sdmx_dimension)
gc.bind('qb', qb)

print (gc.serialize(format="turtle"))
print (ds.serialize(format="turtle"))
print (dsMother.serialize(format="turtle"))

g=Graph(store)
g.add((URIRef('http://example.org/x'), URIRef('http://example.org/y'),Literal('bar')))
ds.add((URIRef('http://example.org/x'),URIRef('http://example.org/z'),Literal('foo-bar'),g))
print (ds.serialize(format="turtle"))

c=Collection(dsMother, context)

len(c)

pprint([term.turtle() for term in c])


###############################
from rdflib import URIRef, BNode, Literal

bob = URIRef("http://example.org/people/Bob")
linda = BNode() # a GUID is generated

name = Literal('Bob') # passing a string
age = Literal(24) # passing a python int
height = Literal(76.5) # passing a python float
from rdflib import Namespace

n = Namespace("http://example.org/people/")

n.bob = URIRef(u'http://example.org/people/bob')
n.eve = URIRef(u'http://example.org/people/eve')

g.add((bob, RDF.type, foaf.person))
g.add((bob, foaf.name, name))
g.add((bob, foaf.knows, linda))
g.add((linda, RDF.type, foaf.Person))
g.add((linda, foaf.name, Literal('Linda')))

print (g.serialize(format="turtle"))