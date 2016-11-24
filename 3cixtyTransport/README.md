LONDON RDF DATA DOCUMENTATION
===============
<p>The dataset contained in the 3cixty Knowledgebase are:</p>

Bus TfL data
------------
<p>The ttl dataset for London bus stops was generated with data published by [Transport for London]: https://tfl.gov.uk (TfL). Unique [SHA-1](https://en.wikipedia.org/wiki/SHA-1) ID was generated for each bus stop which immediately linked the bus stop to its geometry and address.</p>
<P>Each bus stop node contains:</p>
<ul>
<li>Identifier</li>
<li>Label</li>
<li>Business type</li>
<li>Address and location</li>
<li>Bus stop geometry has both point coordinates and geoSPARQL literal value.</li>
</ul>
[London TfL Bus stop RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/busStop_rdfDiagram.svg)</br>
[Example of a London TfL Bus stop RDF ontology diagram: East Street bus stop](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/busStopExample_rdfDiagram.svg)
<p>London bus stop turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/London/stop/47001> a dul:Place,
        naptan:BusStop,
        transit:Stop ;
    rdfs:label "East Street" ;
    locationOnt:businessType "http://data.linkedevents.org/kos/3cixty/busstop" ;
    geom:geometry <http://data.linkedevents.org/location/dd8eef47-7f85-5fe9-8e48-58958c93e6e6/geometry> ;
    dc:identifier "47001" ;
    dc:publisher <https://tfl.gov.uk/modes/buses/> ;
    schema:location <http://data.linkedevents.org/location/dd8eef47-7f85-5fe9-8e48-58958c93e6e6/address> ;
    geo:location <http://data.linkedevents.org/location/dd8eef47-7f85-5fe9-8e48-58958c93e6e6/geometry> ;
    locn:address <http://data.linkedevents.org/location/dd8eef47-7f85-5fe9-8e48-58958c93e6e6/address> .
    
<http://data.linkedevents.org/location/dd8eef47-7f85-5fe9-8e48-58958c93e6e6/address> a dct:Location,
        schema:PostalAddress ;
    dct:title "East Street" ;
    schema:addressLocality "London" ;
    schema:streetAddress "East Street" ;
    locn:address "East Street" ;
    locn:adminUnit12 "London" .

<http://data.linkedevents.org/location/dd8eef47-7f85-5fe9-8e48-58958c93e6e6/geometry> a geo:Point ;
    geo:lat "51.48734305"^^xsd:double ;
    geo:long "-0.095244167"^^xsd:double ;
    locn:geometry "POINT(51.4873430490329 -0.0952441671769662)"^^geosparql:wktLiteral .
```
<p>Example SPARQL query: T.B.C.</p>
</br>

Underground, overground, tram and light rail TfL data
------------
<p>The ttl dataset for London Underground stations published by Transport for London contains:</p>
<ul>
<li>Unique URI for each tube station in the TfL network</li>
<li>Station name and extended description</li>
<li>Semantic links to tube lines which stop at given station</li>
<li>Geometry property represented both as coordinates and geoSPARQL literal value</li>
</ul>
[London underground station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/undergroundStation_rdfDiagram.svg)</br>
[Example of London underground RDF ontology diagram: Acton Town station](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/undergroundStationExample_rdfDiagram.svg)<br>
<p>Underground station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/London/subwayStop/ActonTownStation> a dul:Place,
        transit:Station ;
    rdfs:label "Acton Town Station" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/subway> ;
    dc:publisher <https://tfl.gov.uk> ;
    dct:description "Acton Town Station London Underground Ltd. Gunnersbury Lane London W3 8HN" ;
    transit:route <http://data.linkedevents.org/transit/London/subwayRoute/District>,
        <http://data.linkedevents.org/transit/London/subwayRoute/Piccadilly> ;
    geo:location <http://data.linkedevents.org/transit/London/subwayStop/ActonTownStation/geometry> .
    
<http://data.linkedevents.org/transit/London/subwayStop/ActonTownStation/geometry> a geo:Point ;
    geo:lat "51.5028"^^xsd:double ;
    geo:long "-0.280251"^^xsd:double ;
    locn:geometry "POINT(51.5027503967285 -0.280251204967499)"^^geosparql:wktLiteral .
    
<http://data.linkedevents.org/transit/London/subwayRoute/Piccadilly> a transit:SubwayRoute .
    
<http://data.linkedevents.org/transit/London/subwayRoute/District> a transit:SubwayRoute .
```
<p>Example SPARQL query: T.B.C.</p>
</br>


Time between undergound stations
-------
<p>This ttl dataset contains travel time between connected TfL tube stations. The structure links unique URIs for tube stations defined as origins to respective URIs for tube stations defined as destinations along with travel time interval between them.</p>
[London underground station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/undergroundStationTimeBetween_rdfDiagram.svg)</br>
[Example of London underground RDF ontology diagram: Acton Town station](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/undergroundStationTimeBetweenRxample_rdfDiagram.svg)</br>
<p>Time in between underground station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/travel/London/timeBetween#1176> a qb:Observation ;
    travel:destination <http://data.linkedevents.org/transit/London/subwayStop/ActonTownStation> ;
    travel:origin <http://data.linkedevents.org/transit/London/subwayStop/EalingCommonStation> ;
    travel:travelTime "3"^^xsd:int .
```
<p>Example SPARQL query: T.B.C.</p>
</br>

Train station data
-----
<p>The train line dataset, which was obtained from the National Rail, contains information about London train stations (and nationwide) which may not necessarily be operated by TFL.</p>
<p>The rdf output includes:</p>
<ul>
<li>Unique station ID’s that are generated with SHA-1 algorithms</li>
<li>Semantic descriptions of each train stations; name, identifier</li>
<li>Semantic descriptions of the train lines</li>
<li>Geometry represented both as coordinates and geoSPARQL literal value</li>
</ul>
[London Train Station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/trainStation_rdfDiagram.svg)</br>
[Example of London Train Station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/trainStationExample_rdfDiagram.svg)</br>
<p>Train station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/London/station/abbey-wood> a dul:Place,
        naptan:RailwayStation,
        transit:Stop ;
    rdfs:label "abbey-wood" ;
    locationOnt:businessType "http://data.linkedevents.org/kos/3cixty/trainstation" ;
    dc:identifier "5131" ;
    dc:publisher "https://tfl.gov.uk/modes/trains/" ;
    schema:name "National Rail" ;
    transit:route <http://data.linkedevents.org/transit/London/railwayRoute/national-rail> ;
    geo:location "http://data.linkedevents.org/location/abbey-wood/geometry" .

<http://data.linkedevents.org/location/abbey-wood/geometry> a geo:Point ;
    geo:lat 51.49102^^xsd:double ;
    geo:long 12.0363^^xsd:double ;
    locn:geometry "POINT (51.491019 0.120363)"^^geosparql:wktLiteral .
 
<http://data.linkedevents.org/transit/London/route/national-rail> schema:name "National Rail" .   
```
<p>Example SPARQL query: T.B.C.</p>
</br>


Bicycle TfL data
-----------
<p>Data on bike hire stations were published by Transport for London.</p>
<p>The generated ttl has the following structure:</p>
<ul>
<li>A unique URI for each bike hire station along with its identifier and label</li>
<li>A geometry URI with geometry properties represented both by point coordinates and geoSPARQL literal value</li>
<li>Address URI along with address properties</li>
<li>A number of bikes available at each station</li>
</ul>
[London TfL Bicycle Hire RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/bicycleHire_rdfDiagram.svg)</br>
[Example of London TfL Bicycle Hire RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/busStopExample_rdfDiagram.svg)</br>
<p>London TfL cycle hire station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15> a dul:Place ;
    rdfs:label "Clarence Walk, Stockwell" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/bikestation> ;
    locationOnt:nTotalDocks "28"^^xsd:int ;
    dc:publisher <http://www.api.tfl.org.uk> ;
    dcterms:description "London TFL Bike hire docks" ;
    dcterms:identifier "BikePoints_630" ;
    schema:dateCreated "2016-07-18T09:42:06"^^xsd:dateTime ;
    schema:location <http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/address> ;
    schema:url <https://api-argon.tfl.gov.uk/Place/BikePoints_630> ;
    locn:geometry <http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/geometry> .
    
<http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/geometry> a geo:Point ;
    geo:lat "51.470732"^^xsd:placeholder ;
    geo:long "-0.126994"^^xsd:placeholder ;
    locn:geometry "POINT (51.470732 -0.126994)"^^geosparql:wktLiteral .
    
<http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/address> a schema:PostalAddress ;
    dcterms:title "Clarence Walk, Stockwell" ;
    schema:streetAddress "Clarence Walk" ;
    locn:address "Clarence Walk, Stockwell" .
```
<p>Example SPARQL query: T.B.C.</p>
</br>


AirBnB
-------
<p>The AirBnB ttl dataset was generated with AirBnB booking system API.</p>
<p>The semantic dataset contains:<p>
<ul>
<li>Unique URI for each accommodation offering</li>
<li>Host name and id along with the description of each offering</li>
<li>Price, minimum nights stay</li>
<li>Number of reviews and reviewing frequency</li>
<li>Number of listings from given host</li>
<li>Business type and yearly availability</li>
<li>Geometry and address URIs</li>
<li>Location as both point coordinates and geoSPARQL literal values</li>
<li>Locality and neighbourhood</li>
</ul>

[London AirBnB RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/airBnB_rdfDiagram.svg)</br>
[Example of London AirBnB RDF ontology diagram: Jonas in Hackney](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/airBnbExample_rdfDiagram.svg)
<p>AirBnB turtle file example:</p>
```Turtle
<http://data.linkedevents.org/location/00091040-d8fe-5765-a326-7e1e58c228a3>  a  locationOnt:Accommodation ,
                dul:Place ,
                acco:Accommodation ,
                gr:Offering  ;
        locationOnt:businessType  "Entire  home/apt"  ;
        seegrid:annually  "19"^^xsd:days  ;
        seegrid:monthly  ""^^xsd:reviewsMonthly  ;
        dc:publisher  <http://www.airbnb.com>  ;
        gr:description  "Modern  East  London  Apartment"  ;
        gr:hasCurrencyValue  "80"^^xsd:GBP  ;
        gr:hasUnitOfMeasurement  "4"^^xsd:minimumNights  ;
        sioc:has_host  "Jonas"  ;
        sioc:host_of  "1"^^xsd:listings  ;
        sioc:last_reply_date  "1970-01-01"^^xsd:date  ;
        sioc:num_replies  "0"^^xsd:reviews  ;
        schema:name  "Accommodation"  ;
        geo:location  <http://data.linkedevents.org/location/00091040-d8fe-5765-a326-7e1e58c228a3/geometry>  ;
        locn:address  <http://data.linkedevents.org/location/00091040-d8fe-5765-a326-7e1e58c228a3/address>  .

<http://data.linkedevents.org/location/00091040-d8fe-5765-a326-7e1e58c228a3/address>  a  acco:Hotel  ;
        dct:addressLocality  "Hackney"  ;
        geo:location  <http://data.linkedevents.org/location/00091040-d8fe-5765-a326-7e1e58c228a3/geometry>  .
        
<http://data.linkedevents.org/location/00091040-d8fe-5765-a326-7e1e58c228a3/geometry>  a  geo:Point  ;
        geo:lat  51.5401^^xsd:double  ;
        geo:long  -5.385104^^xsd:double  ;
        locn:geometry  "POINT(51.5401000976562 -0.0538510382175446)"^^geo:wktLiteral  .
```
<p>Example SPARQL query: T.B.C.</p>
</br>

Wunderground stations
------------
<p>The rdf graph for the London wunderground weather stations is generated with data collected from Wunderground forecast api, as published by [Wunderground]: https://www.wunderground.com/. The weather stations emits various weather readings. Included in the rdf graph is the weather condition reading and its corresponding timestamps. Each weather station can be identified by its given station id number and is immediately linked with its geometry and address information. A uri observation link is also listed. Because the observations are to be updated periodically, the observations are graphed in a separate 'real-time' ttl file.</p>
<P>Each weather station node contains:</p>
<ul>
<li>Identifier</li>
<li>Label</li>
<li>Business type</li>
<li>Publisher</li>
<li>Link to weather station observation properties</li>
<li>Link to weather address properties</li>
<li>Link to weather geometric properties</li>
<li>Weather station geometry has both point coordinates and geoSPARQL literal value.</li>
</ul>
[Wunderground weather station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStations.svg)</br>
[Example of a Wunderground weather station RDF ontology diagram: East Street bus stop](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStationsExample.svg)
[Real time observation from a Wunderground weather station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStations.svg)</br>
[Example of a real time observation from a Wunderground weather station RDF ontology diagram: East Street bus stop](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStationsExample.svg)
<p>London Wunderground weather station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/environment/London/wunderground/deviceId/I90579897> a dul:Place,
        ssn:sensingDevice ;
    rdfs:label "I90579897" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/wunderground/weatherstation> ;
    ssn:hasPropery <http://data.linkedevents.org/environment/London/wunderground/observation/59ed2715-f5aa-53ac-bc01-1eb72c028e7d> ;
    dct:publisher <https://www.wunderground.com> ;
    schema:location <http://data.linkedevents.org/environment/London/wunderground/deviceId/I90579897/address> ;
    geo:location <http://data.linkedevents.org/environment/London/wunderground/deviceId/I90579897/geometry> .
    
<http://data.linkedevents.org/environment/London/wunderground/deviceId/I90579897/address> a schema:PostalAddress ;
    schema:addressLocality "North Finchley" ;
    schema:streetAddress "North Finchley" ;
    locn:address "North Finchley, North Finchley" .

<http://data.linkedevents.org/environment/London/wunderground/deviceId/I90579897/geometry> a geo:Point ;
    geo:lat "51.613396"^^xsd:double ;
    geo:lon "-0.17326"^^xsd:double ;
    locn:geometry "POINT(51.613396 -0.17326)"^^geosparql:wktLiteral .
```
<P>Each real time weather station observation node contains:</p>
<ul>
<li>Observation identifier</li>
<li>Observation time</li>
<li>Observation value</li>
<li>Description</li>

</ul>

<p>London Wunderground weather station real-time turtle file example:</p>
```Turtle
<http://data.linkedevents.org/environment/London/wunderground/observation/59ed2715-f5aa-53ac-bc01-1eb72c028e7d> a ssn:observation ;
    ssn:observationResultTime "2016-08-31T19:00:00"^^xsd:dateTime ;
    ssn:observationValue "partlycloudy"@en ;
    dct:description "weather condition"@en .
```

<p>Example SPARQL query: T.B.C.</p>
</br>




