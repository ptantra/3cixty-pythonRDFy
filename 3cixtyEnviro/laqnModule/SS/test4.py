__author__ = 'patrick'

from rdflib.graph import Graph
from pprint import pprint
from rdflib import URIRef, Literal, Namespace, plugin, Graph, BNode, Dataset
from rdflib.collection import Collection

RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

listName = BNode('A')
g = Graph('IOMemory')
listItem1 = BNode('B')
listItem2 = BNode('C')
g.add((listName, RDF.first, Literal(1)))
g.add((listName, RDF.rest, listItem1))
g.add((listItem1, RDF.first, Literal(2)))
g.add((listItem1, RDF.rest, listItem2))
g.add((listItem2, RDF.rest, RDF.nil))
g.add((listItem2, RDF.first, Literal(3)))
c = Collection(g,listName)
#pprint([term.rdf() for term in c])


c.serialize('x.ttl', format='turle')