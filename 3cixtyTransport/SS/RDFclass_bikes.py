__author__ = '3cixty team'

import os
import csv
import uuid
import requests
import json
import time
#import pyproj

from rdflib import URIRef, Literal, Namespace, plugin, Graph, ConjunctiveGraph
from rdflib.store import Store
from collections import defaultdict
#from json2csv import Json2Csv

class RDFclass_bikes:

    # initialise graph variable, read dictionary and bing prefixes
    def __init__(self):
        store = plugin.get('IOMemory', Store)()
        self.g=Graph(store)
        prefixes=self.readDict()
        self.bindingPrefixes(prefixes)

    def readCsv(self,inputfile):
        try:
            f=open(inputfile);
            rf=csv.reader(f,delimiter=',');
            return rf;
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            raise

    def writeCsv(self,output,row):
        if os.path.exists(output):
            f = open(output, 'a')
            f.write(row)
        else:
            f = open(output, 'w+')
            f.write(row)
        f.close()

    def readDict(self):
        dict = defaultdict(list)
        with open('dictionary_bikes.csv','rb') as f:
            r = csv.DictReader(f)
            for row in r:
                for (k,v) in row.items():
                    dict[k]=v
        f.close()
        return dict


    def getUid(self,s,n):
        idencode=s.encode('utf-8')
        uid=uuid.uuid5(n, idencode)
        return uid

    '''
    def convertProj(self,lon,lat):
        Bng = pyproj.Proj(init='epsg:27700')
        Wgs84 = pyproj.Proj(init='epsg:4326')
        wgsLon,wgsLat = pyproj.transform(Bng,Wgs84,lon, lat)
        return wgsLon,wgsLat

    '''

    def executeRequest(self,command,params ):
        print "Reading Bikes Endpoint: https://api.tfl.gov.uk/BikePoint"
        response = requests.get(command , params = params )
        content = json.loads(response.content)

        if( 200 != response.status_code):
            print "StatusCode : " , response.status_code

        return content

    def getBikeData(self):
        command="https://api.tfl.gov.uk/BikePoint?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0"
        return self.executeRequest(command, params = None)


    def saveJsonData(self,data):
        f = open("London_cyclehire_"+time.strftime("%Y_%m_%d_%H_%M")+".json", "w")
        f.write(json.dumps( data , indent = 4 ))
        print f
        f.close()


    def json2csv(self,jsoncontent):
        parser = init_parser()
        args = parser.parse_args()
        key_map = json.load(args.key_map)
        loader = None
        if args.each_line:
            loader = MultiLineJson2Csv(key_map)
        else:
            loader = Json2Csv(key_map)

        loader.load(args.json_file)

        outfile = args.output_csv
        if outfile is None:
            fileName, fileExtension = os.path.splitext(args.json_file.name)
            outfile = fileName + '.csv'

        loader.write_csv(filename=outfile, make_strings=args.strings)


    def bindingPrefixes(self,prefixes):
        for key in prefixes:
            self.g.bind(key, prefixes[key])

    def createBikeParkID(self,bikeGUID):
        singlePark = URIRef("http://data.linkedevents.org/location/%s" % bikeGUID)
        return singlePark

    def createGeometry(self, bikeGUID):
        singleGeometry = URIRef(('http://data.linkedevents.org/location/%s/geometry') % bikeGUID)
        return singleGeometry

    def createAddress(self, bikeGUID):
        singleAddress = URIRef(('http://data.linkedevents.org/london/%s/address') % bikeGUID)
        return singleAddress

    def writeRDF(self,outputfile):
         self.g.serialize(outputfile,format='turtle')

    def createRDF(self,row):

        nspaces=self.readDict()

        schema = Namespace(nspaces.get('schema'))
        unknow = Namespace(nspaces.get('unknow'))
        naptan = Namespace(nspaces.get('naptan'))
        owl = Namespace(nspaces.get('owl'))
        xsd = Namespace(nspaces.get('xsd'))
        rdfs = Namespace(nspaces.get('rdfs'))
        vcard = Namespace(nspaces.get('vcard'))
        locationOnt = Namespace(nspaces.get('locationOnt'))
        geom = Namespace(nspaces.get('geom'))
        geo = Namespace(nspaces.get('geo'))
        geosparql = Namespace(nspaces.get('geosparql'))
        rdf = Namespace(nspaces.get('rdf'))
        dcterms = Namespace(nspaces.get('dcterms'))
        dul = Namespace(nspaces.get('dul'))
        locn = Namespace(nspaces.get('locn'))
        foaf = Namespace(nspaces.get('foaf'))
        dc = Namespace(nspaces.get('dc'))

        bikeid  = row["url"].split('_')[1].encode('utf-8')
        uid=self.getUid(bikeid,naptan)
        bikeGUID = uid

        bikeLat,bikeLong=float(row["lat"]),float(row["lon"])
        bikeLats=str('{:f}'.format(bikeLat))
        bikeLongs=str('{:f}'.format(bikeLong))
        numBikes=str(row["additionalProperties"][6]["value"].encode('utf-8'))

        Address=row["commonName"].split(',')
        bikeLabel=Address[len(Address)-1].lstrip()+' '+str(bikeid)

        bikeGeometry = "POINT ("+str(bikeLat) +" "+str(bikeLong)+")"
        bikeAddress = Literal(row["commonName"])
        bikeCreatedDate=time.strftime("%Y")

        singleBike = self.createBikeParkID(bikeGUID)
        singleAddress = self.createAddress(bikeGUID)
        singleGeometry = self.createGeometry(bikeGUID)
        bikePublisher=URIRef('https://api.tfl.gov.uk/#BikePoint')
        bikeBusinessType = URIRef('http://data.linkedevents.org/kos/3cixty/bikestation')


        self.g.add((singleBike, rdf.type, dul.Place))
        self.g.add((singleBike, dc.identifier, Literal(bikeid)))
        self.g.add((singleBike, rdfs.label, Literal(bikeLabel)))
        self.g.add((singleBike, geom.geometry, singleGeometry))
        self.g.add((singleBike, schema.geo, singleGeometry))
        self.g.add((singleBike, geo.location, singleGeometry))
        self.g.add((singleBike, schema.location, singleGeometry))
        self.g.add((singleBike, vcard.hasAddress, singleAddress))
        self.g.add((singleBike, locn.addresss, singleAddress))
        self.g.add((singleBike, schema.dateCreated, Literal(bikeCreatedDate, datatype=xsd.int)))
        self.g.add((singleBike, locationOnt.numBikes, Literal(numBikes, datatype=xsd.int)))
        self.g.add((singleBike, dc.publisher, bikePublisher))
        self.g.add((singleBike, locationOnt.businessType, bikeBusinessType))

        self.g.add((singleGeometry, rdf.type, geo.Point))
        self.g.add((singleGeometry, geo.lat, Literal(bikeLats)))
        self.g.add((singleGeometry, geo.long, Literal(bikeLongs)))
        self.g.add((singleGeometry, locn.geometry, Literal(bikeGeometry, datatype=geosparql.wktLiteral)))

        self.g.add((singleAddress, rdf.type, locn.address))
        self.g.add((singleAddress, rdf.type, schema.PostalAddress))
        self.g.add((singleAddress, rdf.type, dcterms.Location))
        self.g.add((singleAddress, dcterms.title, bikeAddress))
        self.g.add((singleAddress, schema.streetAddress, bikeAddress))
        self.g.add((singleAddress, locn.address, bikeAddress))

        return self.g

    def main():

        pathf = "/Users/Roberto/Documents/"
        inFileTube = pathf + "stationsTube.csv"
        outFileTube = pathf + "stationsTube.ttl"

        csvTubeS = readCsv(inFileTube)

        next(csvTubeS, None)

        tubeS_store = plugin.get('IOMemory', Store)()
        tubeS_g = Graph(tubeS_store)

        prefixes = definePrefixes()

        print('Binding Prefixes')

        bindingPrefixes(tubeS_graph, prefixes)


        print('Creating graph-TubeS...')
        flag = 1
        for row in csvTubeS:
            lstData = getTubeSData(row)
            createRDF(lstData, tubeS_g, flag)
            flag = 0
        createRDF(lstData, tubeS_g, flag).serialize(outFileTube, format='turtle')

        print ('DONE!')

    if __name__ == "__main__":
        main();
