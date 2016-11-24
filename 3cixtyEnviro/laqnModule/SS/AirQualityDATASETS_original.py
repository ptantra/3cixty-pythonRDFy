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


from rdflib.namespace import RDF, RDFS, SKOS

from rdflib import plugin, exceptions, query

from rdflib.term import Node, URIRef, Genid
from rdflib.term import BNode
from rdflib.term import Literal

from rdflib.paths import Path

assert Literal
from rdflib.namespace import Namespace
assert Namespace
from rdflib.store import Store
from rdflib.serializer import Serializer
from rdflib.parser import Parser
from rdflib.parser import create_input_source
from rdflib.namespace import NamespaceManager
from rdflib.resource import Resource
from rdflib import py3compat
b = py3compat.b

import os
import shutil
import tempfile
from urlparse import urlparse

RDF = Namespace("http://www.w3.org/2000/01/rdf-schema#")

from rdflib.graph import Graph, Dataset, ConjunctiveGraph
from pprint import pprint

ds = Dataset()
ds.add((URIRef('http://example.org/a'),URIRef('http://www.example.org/b'),Literal('foo')))
g = ds.graph(URIRef('http://www.example.com/gr'))
g.add((URIRef('http://purl.org/linked-data/sdmx/2009/subject#/3.1'),URIRef('http://purl.org/linked-data/sdmx/2009/subject#/3.2'),Literal('bar')))
ds.add((URIRef('http://example.org/x'),URIRef('http://example.org/z'),Literal('foo-bar'),g))

for t in ds.triples((None,None,None)):
     print(t)

for q in ds.quads((None, None, None, None)):
     print(q)

for c in ds.graphs():
     print(c)

file = open("/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/outputTEST.ttl', format='turtle')


