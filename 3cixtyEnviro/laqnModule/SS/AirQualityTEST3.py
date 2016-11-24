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

RDF = Namespace("http://www.w3.org/2000/01/rdf-schema#")

store = plugin.get('IOMemory', Store)()
g1 = Graph(store)
g2 = Graph(store)
g3 = Graph(store)
stmt1 = BNode()
stmt2 = BNode()
stmt3 = BNode()
g1.add((stmt1, RDF.type, RDF.Statement))
g1.add((stmt1, RDF.subject,URIRef(u'http://rdflib.net/store/ConjunctiveGraph')))

g1.add((stmt1, RDF.predicate, RDFS.label))
g1.add((stmt1, RDF.object, Literal("Conjunctive Graph")))
g2.add((stmt2, RDF.type, RDF.Statement))
g2.add((stmt2, RDF.subject,URIRef(u'http://rdflib.net/store/ConjunctiveGraph')))

g2.add((stmt2, RDF.predicate, RDF.type))
g2.add((stmt2, RDF.object, RDFS.Class))
g3.add((stmt3, RDF.type, RDF.Statement))
g3.add((stmt3, RDF.subject,URIRef(u'http://rdflib.net/store/ConjunctiveGraph')))

g3.add((stmt3, RDF.predicate, RDFS.comment))
g3.add((stmt3, RDF.object, Literal("The top-level aggregate graph - The sum " + "of all named graphs within a Store")))
#len(list(ConjunctiveGraph(store).subjects(RDF.type, RDF.Statement)))

#len(list(ReadOnlyGraphAggregate([g1,g2]).subjects(RDF.type, RDF.Statement)))

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g3.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')


