LONDON TRANSPORT RDF DATA DOCUMENTATION
===============
<p>The dataset contained in the 3cixty Knowledgebase are:</p>

Bus TfL data: Bus Stops
------------
<p>The ttl dataset for London bus stops was generated with data published by [Transport for London]: https://tfl.gov.uk (TfL). Unique [SHA-1](https://en.wikipedia.org/wiki/SHA-1) ID was generated for each bus stop which immediately linked the bus stop to its geometry and address.</p>
<p>Each bus stop node contains:</p>
<ul>
<li>Identifier</li>
<li>Label</li>
<li>Business type</li>
<li>Address and location</li>
<li>Bus stop geometry has both point coordinates and geoSPARQL literal value.</li>
</ul>
[London TfL Bus stop RDF ontology diagram](https://github.com/3cixty/knowledgebase/master/documentation/London/busStop_rdfDiagram.svg)</br>
[Example of a London TfL Bus stop RDF ontology diagram: East Street bus stop](https://github.com/3cixty/knowledgebase/master/documentation/London/busStopExample_rdfDiagram.svg)

![London Bus stop RDF graph diagram](busStop RDF diagrams_1605034.jpg?raw=true)

<p>London bus stop turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/london/stop/10001> a dul:Place,
        naptan:BusStop,
        transit:Stop ;
    rdfs:label "Trevor Close" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/busstop> ;
    geom:geometry <http://data.linkedevents.org/location/d0bd682a-d99a-52b4-9dfa-bd747d5e85ec/geometry> ;
    dc:identifier "10001" ;
    dc:publisher <https://tfl.gov.uk> ;
    schema:location <http://data.linkedevents.org/location/d0bd682a-d99a-52b4-9dfa-bd747d5e85ec/address> ;
    geo:location <http://data.linkedevents.org/location/d0bd682a-d99a-52b4-9dfa-bd747d5e85ec/geometry> .
    
<http://data.linkedevents.org/location/d0bd682a-d99a-52b4-9dfa-bd747d5e85ec/address> a schema:postalAddress ;
    locn:address "Trevor Close" .

<http://data.linkedevents.org/location/d0bd682a-d99a-52b4-9dfa-bd747d5e85ec/geometry> a geo:Point ;
    geo:lat "51.460191021304176"^^xsd:double ;
    geo:lon "-0.3348309612429955"^^xsd:double ;
    locn:geometry "POINT (51.460191021304176 -0.3348309612429955)"^^geosparql:wktLiteral .
```
<p>Example SPARQL query:</p>
```SPARQL
prefix dct: <http://purl.org/dc/terms/> 

SELECT ?label ?lon ?lat ?identifier
WHERE {
{ 
?node rdfs:label ?label .
?node a transit:Stop . 
?node dc:identifier ?identifier . 
?node geo:location ?location . }
{?location geo:lon ?lon ; geo:lat ?lat . }
}limit 20
```

Bus TfL data: Bus Lines
------------
<p>The ttl dataset for London bus stops was generated with data published by [Transport for London]: https://tfl.gov.uk (TfL). Unique [SHA-1](https://en.wikipedia.org/wiki/SHA-1) ID was generated for each bus stop which immediately linked the bus stop to its geometry and address.</p>
<p>Each bus-line entity contains:</p>
<ul>
<li>Identifier</li>
<li>Label</li>
<li>Route</li>
<li>Route service number</li>
<li>A list of geolocated points representing the sequence of stops that is listed in the route.</li>
</ul>

<p>London bus-line turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/london/busLine/0001e385-bbeb-5cf9-9664-a34a1624ae4a> a transit:BusRoute ;
    rdfs:label "Woodbine Place- Rensburg Road" ;
    transit:RouteService <http://data.linkedevents.org/transit/london/service/W12_2> ;
    transit:route <http://data.linkedevents.org/transit/london/route/W12> ;
    geo:location <http://data.linkedevents.org/transit/london/busLine/0001e385-bbeb-5cf9-9664-a34a1624ae4a/geometry> .
    
<http://data.linkedevents.org/transit/london/busLine/0001e385-bbeb-5cf9-9664-a34a1624ae4a/geometry> a sf:LineString ;
    locn:geometry "LINESTRING (51.5769506448 0.0267878469017, 51.5783271618 0.025708888584, 51.5819507288 0.0283382746549, 51.5882544375 0.0283447625645, 51.590186877 0.0299611365795, 51.5916320484 0.0280332371672, 51.5941019888 0.0245626474983, 51.5944460584 0.0223400490948, 51.5913767086 0.0225068961583, 51.589252562 0.0220949467414, 51.5866049637 0.0212700400457, 51.5839942937 0.0203891330705, 51.5832330381 0.0160250161139, 51.5833830267 0.00937733816316, 51.5829022682 0.00436183844349, 51.5797671978 0.00416615083856, 51.5781006071 0.00907215711642, 51.5766011073 0.00368048451906, 51.5796735219 0.0017516629076, 51.5811495312 0.00115257434997, 51.5808918374 -0.0011392736254, 51.5826775974 -0.00514580323675, 51.5832384771 -0.00745961715069, 51.5806107619 -0.0185007991604, 51.5830972616 -0.0198360622321, 51.5837964817 -0.0202387000908, 51.5825533223 -0.0243776131692, 51.5831144625 -0.0294053002793, 51.5825501265 -0.0322155124054, 51.581890837 -0.0341925802244, 51.5797065758 -0.0417777064425)"^^geosparql:wktLiteral .
```
<p>Example SPARQL query: T.B.C.</p>

Bus TfL data: Bus Correspondence
------------
<p>The bus correspondence contains the information that links the bus stops with the line route number, and the buses serving them.</p>
<p>Each bus-correspondence entity contains:</p>
<ul>
<li>The sequence number representing the position in the bus' sequence of stops.</li>
<li>The service number i.e. route number and sequence number</li>
<li>The TfL stop ID</li>
</ul>

```Turtle
<http://data.linkedevents.org/transit/london/serviceStop/100_1/2585> a transit:ServiceStop ;
    transit:sequence "6"^^xsd:int ;
    transit:service <http://data.linkedevents.org/transit/london/service/100_1> ;
    transit:stop <http://data.linkedevents.org/transit/london/stop/2585> .
```

Underground TfL data
------------
<p>The ttl dataset for London Underground stations published by Transport for London contains:</p>
<ul>
<li>Unique URI for each tube station in the TfL network</li>
<li>Station name and extended description</li>
<li>Semantic links to tube lines which stop at given station</li>
<li>Geometry property represented both as coordinates and geoSPARQL literal value</li>
<li>Address property</li>
<li>The route servicing the stops</li>
</ul>
[London underground station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/undergroundStation_rdfDiagram.svg)</br>
[Example of London underground RDF ontology diagram: Acton Town station](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/undergroundStationExample_rdfDiagram.svg)<br>
<p>Underground station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/london/station/00900227-8a9d-5227-a59e-dd520b48c7ac> a dul:Place,
        transit:Station ;
    rdfs:label "Swiss Cottage Underground Station" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/subway> ;
    dc:identifier "940GZZLUSWC" ;
    dc:publisher <https://tfl.gov.uk> ;
    dct:description "Swiss Cottage Station,London Underground Ltd.,Finchley Rd,London,NW3 6HY" ;
    transit:route <http://data.linkedevents.org/transit/london/subwayRoute/jubilee> ;
    geo:location <http://data.linkedevents.org/transit/london/station/00900227-8a9d-5227-a59e-dd520b48c7ac/geometry> ;
    locn:address <http://data.linkedevents.org/location/00900227-8a9d-5227-a59e-dd520b48c7ac/address> .
    
<http://data.linkedevents.org/transit/london/station/00900227-8a9d-5227-a59e-dd520b48c7ac/geometry> a geo:Point ;
    geo:lat "51.543681"^^xsd:double ;
    geo:long "-0.174894"^^xsd:double ;
    locn:geometry "POINT (51.543681 -0.174894)"^^geosparql:wktLiteral .

<http://data.linkedevents.org/location/00900227-8a9d-5227-a59e-dd520b48c7ac/address> a dct:Location,
        schema:PostalAddress ;
    dct:title "Swiss Cottage Underground Station" ;
    schema:streetAddress "Swiss Cottage Station,London Underground Ltd.,Finchley Rd,London,NW3 6HY"
    
<http://data.linkedevents.org/transit/london/subwayRoute/jubilee> a transit:RailRoute ;
    schema:name "jubilee" ;
    transit:Station <http://data.linkedevents.org/transit/london/station/00900227-8a9d-5227-a59e-dd520b48c7ac>,
        <http://data.linkedevents.org/transit/london/station/0a689524-fa81-5e8e-839f-5b3a8008562d>,
        <http://data.linkedevents.org/transit/london/station/0e5afc17-c3da-587b-a28a-6d23ef0bfcb3>,
        <http://data.linkedevents.org/transit/london/station/1aa03ce4-705b-5826-b8d3-2e6ffd9fd9db>,
        <http://data.linkedevents.org/transit/london/station/1cc33497-2fee-5bbc-bbf5-a4014ed6c6d6>...
```
<p>Example SPARQL query:</p>
```SPARQL
prefix dct: <http://purl.org/dc/terms/> 

SELECT ?label ?route ?long ?lat ?description
WHERE {
{?node rdfs:label ?label .
?node a transit:Station . 
?node dct:description ?description . 
?node geo:location ?location .
?node transit:route ?route . 
FILTER ( regex (str(?label), "Underground Station", "i") )}
{?location geo:long ?long ; geo:lat ?lat . }
}limit 20
```

Overground TfL data
-----------
<p>Data on overground stations.</p>
<p>The generated ttl has the following structure:</p>
<ul>
<li>Unique URI for each overground station in the TfL network</li>
<li>Station name and extended description</li>
<li>Geometry property represented both as coordinates and geoSPARQL literal value</li>
<li>Address property</li>
<li>The route servicing the stops</li>
</ul>
<p>Overground station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/london/subwayStop/0060c7fd_a2ab_53d9_ac8e_79e602992259> a dul:Place,
        transit:Station ;
    rdfs:label "Wood Street Rail Station" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/subway> ;
    dc:identifier "910GWDST" ;
    dc:publisher <https://tfl.gov.uk> ;
    dct:description "RailStation" ;
    transit:route <http://data.linkedevents.org/transit/london/subwayRoute/london-overground> ;
    geo:location <http://data.linkedevents.org/transit/london/subwayStop/0060c7fd_a2ab_53d9_ac8e_79e602992259/geometry> .

<http://data.linkedevents.org/transit/london/subwayStop/0060c7fd_a2ab_53d9_ac8e_79e602992259/geometry> a geo:Point ;
    geo:lat "51.58658"^^xsd:double ;
    geo:long "-0.002405"^^xsd:double ;
    locn:geometry "POINT (51.58658 -0.002405)"^^geosparql:wktLiteral .
        
<http://data.linkedevents.org/transit/london/subwayRoute/london-overground> a transit:RailRoute ;
    schema:name "london-overground" ;
    transit:Station <http://data.linkedevents.org/transit/london/subwayStop/0060c7fd_a2ab_53d9_ac8e_79e602992259>,
        <http://data.linkedevents.org/transit/london/subwayStop/02fe5a5f_2452_5dac_adfe_931c9d5e19ba>,
        <http://data.linkedevents.org/transit/london/subwayStop/03458137_e50c_5d87_9fe3_329cf5433b83>,
        <http://data.linkedevents.org/transit/london/subwayStop/046aa6af_14f4_5e7f_95c7_f42e53af6379>,
        <http://data.linkedevents.org/transit/london/subwayStop/047e195e_59aa_577e_af54_9560c5c17a22>...
```
<p>Example SPARQL query: </p>
```SPARQL
prefix dct: <http://purl.org/dc/terms/> 
 
SELECT ?label ?long ?lat ?description
WHERE {
{ ?node rdfs:label ?label .
?node a transit:Station . 
?node dct:description ?description . 
?node geo:location ?location .
?node transit:route <http://data.linkedevents.org/transit/london/subwayRoute/london-overground> . }
{?location geo:long ?long ; geo:lat ?lat . }
}limit 20
```
</br>

Docklands Light Railway (DLR) data
-----------
<p>Data on DLR stations.</p>
<p>The generated ttl has the following structure:</p>
<ul>
<li>Unique URI for each overground station in the TfL network</li>
<li>Station name and extended description</li>
<li>Geometry property represented both as coordinates and geoSPARQL literal value</li>
<li>Address property</li>
<li>The route servicing the stops</li>
</ul>
<p>DLR station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/london/subwayStop/017b639b_2867_5dce_916c_7e885ec7c10a> a dul:Place,
        transit:Station ;
    rdfs:label "Lewisham DLR Station" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/subway> ;
    dc:publisher <https://tfl.gov.uk> ;
    dct:description "MetroStation" ;
    transit:route <http://data.linkedevents.org/transit/london/subwayRoute/dlr> ;
    geo:location <http://data.linkedevents.org/transit/london/subwayStop/017b639b_2867_5dce_916c_7e885ec7c10a/geometry> .

<http://data.linkedevents.org/transit/london/subwayStop/017b639b_2867_5dce_916c_7e885ec7c10a/geometry> a geo:Point ;
    geo:lat "51.464665"^^xsd:double ;
    geo:long "-0.012874"^^xsd:double ;
    locn:geometry "POINT (51.464665 -0.012874)"^^geosparql:wktLiteral .
        
<http://data.linkedevents.org/transit/london/subwayRoute/dlr> a transit:RailRoute ;
    schema:name "dlr" ;
    transit:Station <http://data.linkedevents.org/transit/london/subwayStop/017b639b_2867_5dce_916c_7e885ec7c10a>,
        <http://data.linkedevents.org/transit/london/subwayStop/079e84fb_94b0_5cd0_a493_fc003b86fd86>,
        <http://data.linkedevents.org/transit/london/subwayStop/098fbb8d_f70a_5705_a3e0_fc908f689afb>,
        <http://data.linkedevents.org/transit/london/subwayStop/169d6df4_5113_5687_b7c0_2d69be89f9ac>,
        <http://data.linkedevents.org/transit/london/subwayStop/1f34ed50_08c0_5c02_8a52_c29a8e6e6722>...
```
<p>Example DLR SPARQL query:</p>
```SPARQL
prefix dct: <http://purl.org/dc/terms/> 
 
SELECT ?label ?long ?lat ?description
WHERE {
{ ?node rdfs:label ?label .
?node a transit:Station . 
?node dct:description ?description . 
?node geo:location ?location .
?node transit:route <http://data.linkedevents.org/transit/london/subwayRoute/dlr> . }
{?location geo:long ?long ; geo:lat ?lat . }
}limit 20
```

Tram TfL data
-----------
<p>Data on DLR stations.</p>
<p>The generated ttl has the following structure:</p>
<ul>
<li>Unique URI for each overground station in the TfL network</li>
<li>Station name and extended description</li>
<li>Geometry property represented both as coordinates and geoSPARQL literal value</li>
<li>Address property</li>
<li>The route servicing the stops</li>
</ul>
<p>Tram stops turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/london/subwayStop/09ac2894_fdc2_5c47_b61a_d080973e7ea9> a dul:Place,
        transit:Station ;
    rdfs:label "Birkbeck Tram Stop" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/subway> ;
    dc:publisher <https://tfl.gov.uk> ;
    dct:description "MetroStation" ;
    transit:route <http://data.linkedevents.org/transit/london/subwayRoute/tram> ;
    geo:location <http://data.linkedevents.org/transit/london/subwayStop/09ac2894_fdc2_5c47_b61a_d080973e7ea9/geometry> .
    
<http://data.linkedevents.org/transit/london/subwayStop/09ac2894_fdc2_5c47_b61a_d080973e7ea9/geometry> a geo:Point ;
    geo:lat "51.403767"^^xsd:double ;
    geo:long "-0.055787"^^xsd:double ;
    locn:geometry "POINT (51.403767 -0.055787)"^^geosparql:wktLiteral .
    
<http://data.linkedevents.org/transit/london/subwayRoute/tram> a transit:RailRoute ;
    schema:name "tram" ;
    transit:Station <http://data.linkedevents.org/transit/london/subwayStop/09ac2894_fdc2_5c47_b61a_d080973e7ea9>,
        <http://data.linkedevents.org/transit/london/subwayStop/0c750e9d_7134_5ca0_9071_cbf6c9fcc682>,
        <http://data.linkedevents.org/transit/london/subwayStop/13e99cc7_ed00_528d_af0b_2a81df44cc37>,
        <http://data.linkedevents.org/transit/london/subwayStop/1530e627_d722_5930_aaab_7127484a5d88>...
```
<p>Example SPARQL query: </p>
```SPARQL
prefix dct: <http://purl.org/dc/terms/> 
 
SELECT ?label ?long ?lat ?description
WHERE {
{ ?node rdfs:label ?label .
?node a transit:Station . 
?node dct:description ?description . 
?node geo:location ?location .
?node transit:route <http://data.linkedevents.org/transit/london/subwayRoute/tram>  . }
{?location geo:long ?long ; geo:lat ?lat . }
}limit 20
```

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
    dc:identifier "BikePoints_630" ;
    dc:publisher <https://tfl.gov.uk> ;
    schema:dateCreated "2016-10-25T12:29:43"^^xsd:dateTime ;
    schema:url <https://api-argon.tfl.gov.uk/Place/BikePoints_630> ;
    geo:location <http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/geometry> ;
    locn:address <http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/address> .
    
<http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/geometry> a geo:Point ;
    geo:lat "51.470732"^^xsd:double ;
    geo:long "-0.126994"^^xsd:double ;
    locn:geometry "POINT (51.470732 -0.126994)"^^geosparql:wktLiteral .
    
<http://data.linkedevents.org/location/002534a0-bd31-563b-9443-ad39e23a1b15/address> a schema:PostalAddress ;
    dct:title "Clarence Walk, Stockwell" ;
    schema:streetAddress "Clarence Walk" ;
    locn:address "Clarence Walk, Stockwell" .
```
<p>Example SPARQL query:</p>
```SPARQL
SELECT ?label ?identifier ?lat ?long ?streetAddress
WHERE {
{?node rdfs:label ?label .
?node a dul:Place . 
?node dc:identifier ?identifier . 
?node geo:location ?location .
?node locn:address ?address .
?node locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/bikestation> . }
{?location geo:long ?long ; geo:lat ?lat . }
{?address schema:streetAddress ?streetAddress. }
}limit 20
```

Ferry TfL data
-----------
<p>Data on Ferry stops published by TfL.</p>
<p>The generated ttl has the following structure:</p>
<ul>
<li>A unique URI for each ferry stop along with its identifier and label</li>
<li>A geometry URI with geometry properties represented both by point coordinates and geoSPARQL literal value</li>
<li>Ferry route</li>
</ul>
<p>London TfL Ferry stop turtle file example:</p>
```Turtle
<http://data.linkedevents.org/transit/london/ferryStop/10ff9350-4462-5f1d-bfbc-1d7e4bcdc98c> a dul:Place,
        transit:Station ;
    rdfs:label "Greenland Pier" ;
    locationOnt:businessType <http://data.linkedevents.org/kos/3cixty/ferrystation> ;
    dc:publisher <https://tfl.gov.uk> ;
    dct:description "FerryBerth" ;
    transit:route <http://data.linkedevents.org/transit/london/ferryRoute/RB1> ;
    geo:location <http://data.linkedevents.org/transit/london/ferryStop/10ff9350_4462_5f1d_bfbc_1d7e4bcdc98c/geometry> .
    
<http://data.linkedevents.org/transit/london/ferryStop/10ff9350_4462_5f1d_bfbc_1d7e4bcdc98c/geometry> a geo:Point ;
    geo:lat "51.494732"^^xsd:double ;
    geo:long "-0.031822"^^xsd:double ;
    locn:geometry "(51.494732 -0.031822)"^^geosparql:wktLiteral .
    
<http://data.linkedevents.org/transit/london/ferryRoute/RB1> a transit:ferryRoute ;
    schema:name "RB1" ;
    transit:Station <http://data.linkedevents.org/transit/london/ferryStop/058481e7-20cb-5cc8-85ef-d871fd0260bc>,
        <http://data.linkedevents.org/transit/london/ferryStop/10ff9350-4462-5f1d-bfbc-1d7e4bcdc98c>,
        <http://data.linkedevents.org/transit/london/ferryStop/16a74c32-8ddb-589a-bc80-02b967cddae3>,
        <http://data.linkedevents.org/transit/london/ferryStop/1c993218-f145-5f4d-a54a-aca0bd86c11a>,
        <http://data.linkedevents.org/transit/london/ferryStop/1e52ab49-6079-5675-90cb-44713db05d2a>...
```
<p>Example SPARQL query: TBC</p>
```SPARQL
```

