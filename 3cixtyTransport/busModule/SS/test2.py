import csv, zipfile, uuid, pyproj, re
from time import strftime
from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict



busPathf = "./"
inFile= "/Users/patrick/3cixty/codes/3cixtyTransport/busModule/IN/cleaned.csv"
outFile = busPathf + "OUT/" + "bus.ttl"

f = open(inFile, 'rU');
csvB = csv.reader(f, delimiter=',');

next(csvB) #skips the header

for row in csvB:
    #print type(row[0])


    naptan = Namespace("http://transport.data.gov.uk/def/naptan/")
    #print naptan
    idencode = row[0].encode('utf-8')
    #print idencode
    uid = uuid.uuid5(naptan, idencode)


    '''
    if isinstance(lon, str) == False:
        print lat
    #print isinstance(lon, str)
    '''

    for index in range(0, len(row)):
        #cleaned = re.sub('[<>#]', '', row[index])
        #row[index] = re.sub('[/]', '-', cleaned)

        Bng = pyproj.Proj(init='epsg:27700')
        Wgs84 = pyproj.Proj(init='epsg:4326')

        lat = row[4]
        lon = row[5]

        print busData[index][0]

        #print tuple(row[4])

        wgsLon, wgsLat = pyproj.transform(Bng, Wgs84, lon, lat)

        print  wgsLon, wgsLat


#busline_store = plugin.get('IOMemory', Store)()
#busline_g = Graph(busline_store)
#busline_graph = ConjunctiveGraph(busline_store)


