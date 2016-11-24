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

g = Graph()
result = g.parse("http://www.w3.org/2000/10/swap/test/meet/blue.rdf")
print("graph has %s statements." % len(g))

for s, p, o in g:
     if (s, p, o) not in g:
         raise Exception("It better be!")
s = g.serialize(format='nt')

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')


