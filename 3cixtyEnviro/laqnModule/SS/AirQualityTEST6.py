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
import rdflib

rdflib = Namespace('http://rdflib.net/')
g = rdflib.Graph()
g.add((rdflib.URIRef('http://rdflib.net/bob'), rdflib.RDFS.label, rdflib.Literal('Bob')))

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')


