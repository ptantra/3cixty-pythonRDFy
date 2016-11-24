import csv, zipfile, uuid, pyproj, re, fileinput, urllib
from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict

r0 = '1234' + 'xxY'

naptan = Namespace("http://a.a.com")
idencode=r0.encode('utf-8')
uid=uuid.uuid5(naptan, idencode)

print uid