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
from rdflib.namespace import RDF, RDFS

g = Graph()
a = BNode('foo')
b = BNode('bar')
c = BNode('baz')

g.add((a, RDF.first, RDF.type))
g.add((a, RDF.rest,b))
g.add((b, RDF.first, RDFS.label))
g.add((b, RDF.rest,c))
g.add((c,RDF.first,RDFS.comment))
g.add((c,RDF.rest,RDF.nil))
def topList(node,g):
    for s in g.subjects(RDF.rest,node):
      yield s
def reverseList(node,g):
   for f in g.objects(node,RDF.first):
      print(f)
   for s in g.subjects(RDF.rest,node):
       yield s

store = plugin.get('IOMemory', Store)()
g = Graph(store)

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')


