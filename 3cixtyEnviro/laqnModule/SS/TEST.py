__author__ = 'patrick'

from rdflib import ConjunctiveGraph, URIRef, plugin, Literal, Graph, BNode, Namespace
from rdflib.store import Store
from rdflib import RDF, RDFS, OWL
from rdflib.namespace import VOID, RDF



FOAF = Namespace('http://xmlns.com/foaf/0.1/')
sdmx_attribute=Namespace('http://purl.org/linked-data/sdmx/2009/attribute#')

store = plugin.get('IOMemory', Store)()

g=ConjunctiveGraph(store)
g

c1 = URIRef("http://example.org/mygraph1")
c2 = Literal('mygraph2')

bob = URIRef(u'urn:unitMeasure')
likes = URIRef(u'urn:likesGANTI')
pizza = URIRef(u'urn:pizzaGANTI')
#g.get_context(c1).add((bob, likes, pizza))
g.get_context(c2).add((bob, likes, pizza))

list(g.contexts())

gc1 = g.get_context(c2)
#print (gc1.serialize(format="turtle"))

g=Graph(store)
s=BNode(Literal('someone'))
g.add((s, RDF.type, FOAF.person))
g.bind('sdmx_attribute', FOAF)
print  g.serialize(format="turtle")

gc1.bind("rdfs", RDFS.uri)
graham = URIRef(u'urn:graham')
gc1.add((graham, likes, pizza))
gc1.add((graham, RDFS.label, Literal('Graham')))
print (gc1.serialize(format="turtle"))

uri = URIRef("http://example.com")
uri

graham = Literal(u'Graham', lang="en")
str(graham)

file = open("/Users/patrick/3cixty/IN/Kings/151201/TEST.ttl", "w")
g.serialize(destination='/Users/patrick/3cixty/IN/Kings/151201/TEST.ttl', format='turtle')
