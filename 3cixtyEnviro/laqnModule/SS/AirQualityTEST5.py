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
from rdflib.namespace import SKOS, RDF, RDFS
from pprint import pprint



from rdflib.graph import Graph
from pprint import pprint
listName = BNode()
g = Graph('IOMemory')
listItem1 = BNode()
listItem2 = BNode()
g.add((listName, RDF.first, Literal(1)))
g.add((listName, RDF.rest, listItem1))
g.add((listItem1, RDF.first, Literal(2)))
g.add((listItem1, RDF.rest, listItem2))
g.add((listItem2, RDF.rest, RDF.nil))
g.add((listItem2, RDF.first, Literal(3)))
c = Collection(g,listName)

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')


