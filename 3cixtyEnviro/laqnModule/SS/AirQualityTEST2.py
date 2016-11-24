import csv
import uuid
import pyproj
import random
from random import seed
import string
from rdflib import URIRef, Literal, Namespace, plugin, Graph, BNode
from rdflib.store import Store
import time
from rdflib.collection import Collection

from rdflib import ConjunctiveGraph, URIRef, RDFS, Literal
from rdflib.namespace import SKOS
from pprint import pprint

g = ConjunctiveGraph()
u = URIRef(u'http://example.com/foo')
g.add([u, RDFS.label, Literal('foo')])
g.add([u, RDFS.label, Literal('bar')])

pprint(sorted(g.preferredLabel(u)))

g.add([u, SKOS.prefLabel, Literal('bla')])
pprint(g.preferredLabel(u))
g.add([u, SKOS.prefLabel, Literal('blubb', lang='en')])
sorted(g.preferredLabel(u))
g.preferredLabel(u, lang='')
pprint(g.preferredLabel(u, lang='en'))

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')


