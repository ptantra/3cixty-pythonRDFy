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

RDF = Namespace("http://www.w3.org/2000/01/rdf-schema#")

from rdflib.graph import Graph
from pprint import pprint
'''listName = BNode()
listItem1 = BNode()
listItem2 = BNode()'''

listName = URIRef("http://www.abc.org/listName")
listItem1 = BNode()
listItem2 = BNode()

g = Graph('IOMemory')

g.add((listName, RDF.first, Literal(1)))
g.add((listName, RDF.rest, listItem1))
g.add((listItem1, RDF.first, Literal(2)))
g.add((listItem1, RDF.rest, listItem2))
g.add((listItem1, RDF.rest, RDF.nil))
g.add((listItem1, RDF.first, Literal(3)))
c = Collection(g,listName)

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')

#pathf = "/Users/patrick/3cixty/IN/Kings/151201/"
    #inFile = pathf + "LaqnDataSAMPLE.csv"
    #outFile = pathf + "LaqnDataSAMPLE.ttl"


#source: http://rdflib.readthedocs.org/en/latest/apidocs/rdflib.html#rdflib.term.bind - collection module


