import csv
import sys
import pyproj
import numpy
import hashlib
import uuid
import pandas as pd
#from osgeo import ogr
import uuid
from rdflib import URIRef, BNode, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store

#f=open('/Users/patrick/3cixty/IN/SG/bus-stops-10-06-15.csv')
#busData = csv.reader(f,delimiter=',')
#next(busData,None)

nspaces=dict([('schema',  "http://schema.org/"), ('naptan',"http://transport.data.gov.uk/def/naptan/"), ('foaf', "http://xmlns.com/foaf/0.1/"), \
                    ('xsd', "http://www.w3.org/2001/XMLSchema#"), ('rdfs', "http://www.w3.org/2000/01/rdf-schema#"), ('vcard', "http://www.w3.org/2006/vcard/ns#"),  \
                    ('locationOnt', "http://data.linkedevents.org/def/location#"), ('geom', "http://geovocab.org/geometry#"), ('unknown', "http://data.linkedevents.org/def/unknown#"), \
                    ('geo', "http://www.w3.org/2003/01/geo/wgs84_pos#"), ('geosparql', "http://www.opengis.net/ont/geosparql#"), ('rdf', "http://www.w3.org/2000/01/rdf-schema#"), \
                    ('transit', "http://vocab.org/transit/terms/"), ('dcterms', "http://purl.org/dc/terms/"), ('dul', "http://ontologydesignpatterns.org/ont/dul/DUL.owl#"), \
                    ('locn', "http://www.w3.org/ns/locn#"),  ('trans', "http://vocab.linkeddata.es/datosabiertos/def/urbanismo-infraestructuras/Transporte#")]);
   # print (nspaces.values())
   
busData = pd.DataFrame(pd.read_csv('/Users/patrick/3cixty/IN/SG/bus-stops-10-06-15.csv'))
#busData.dtypes()
print(busData.head())
#print(busData[[0]][100:1000].duplicated())

#busData.fillna[[2]](50)

#print "Null Values\n", pd.isnull(busData[[2]]).sum()
#print "Duplicates\n", busData[[2]].duplicated().sum()

idencode='B334'.decode()

naptan = Namespace(nspaces.get('naptan')) #nspaces - need dictionary to be defined first otherwise the code above applies
naptan = Namespace('http://transport.data.gov.uk/def/naptan/')

print(uuid.uuid5(naptan, idencode))

#for row in busData:
    #idencode=row[0].encode('utf-8')
    #print(uuid.uuid5(naptan, idencode))
    
    
    
