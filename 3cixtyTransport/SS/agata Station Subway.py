class Tube(RDF):
   def __init__(self, x, y, station, description, wkt, businessType, publisher, lines):
       RDF.__init__(self)
       self.tubes = ['Bakerloo',
                         'Central',
                         'Circle',
                         'District',
                         'Hammersmith & City',
                         'Jubilee',
                         'Metropolitan',
                         'Northern',
                         'Piccadilly',
                         'Victoria',
                         'Waterloo & City']
       self.x = x
       self.y = y
       self.station = station
       self.description = description
       self.wkt = wkt
       self.businessType = businessType
       self.publisher = publisher
       self.lines = lines

   def createStation(self):
       stationName = URIRef('http://data.linkedevents.org/transit/London/subwayStop/' + Literal(self.station).replace(" ", ""))
       return stationName

   def createStationGeom(self):
       stationGeom = URIRef(self.createStation() + '/geometry')
       return stationGeom

   def createSubwayRoute(self):
       for i in self.tubes:
           tubeline = URIRef('http://data.linkedevents.org/transit/London/subwayRoute/' + Literal(i).replace(" ", ""))
           self.g.add((tubeline, self.rdf.type, self.transit.SubwayRoute))
       return self.g

   def addStationLine(self):
       for i in self.lines[1:]:
           singleLine = URIRef('http://data.linkedevents.org/transit/London/subwayRoute/' + Literal(i).replace(" ", ""))
           self.g.add((self.createStation(), self.transit.route, singleLine))
       return self.g

   def createTubeGraph(self):
       self.g.add((self.createStation(), self.rdf.type, self.transit.Station))
       self.g.add((self.createStation(), self.rdf.type, self.dul.Place))
       self.g.add((self.createStation(), self.rdfs.label, Literal(self.station)))
       self.g.add((self.createStation(), self.dct.description, Literal(self.description)))
       self.g.add((self.createStation(), self.geo.location, self.createStationGeom()))
       self.g.add((self.createStation(), self.locationOnt.businessType, URIRef(Literal(self.businessType))))
       self.g.add((self.createStation(), self.dc.publisher, URIRef(Literal(self.publisher))))
       self.g.add((self.createStationGeom(), self.rdf.type, self.geo.Point))
       self.g.add((self.createStationGeom(), self.geo.lat, Literal(self.y, datatype=self.xsd.double)))
       self.g.add((self.createStationGeom(), self.geo.long, Literal(self.x, datatype=self.xsd.double)))
       self.g.add((self.createStationGeom(), self.locn.geometry, Literal(self.wkt, datatype=self.geosparql.wktLiteral)))

       self.bindingPrefixes()
       self.createSubwayRoute()
       self.addStationLine()
       return self.g

agata [11:45 AM]
sample data

agata [11:46 AM]
tube = Tube(10000, 5000, 'Great station', 'a very long description', 'just some wkt',
           'http://data.linkedevents.org/kos/3cixty/subway',
           'https://tfl.gov.uk',
           ['Great station', 'Central', 'Metropolitan', 'Piccadilly'])

print(tube.createTubeGraph().serialize(format='turtle')) (edited)