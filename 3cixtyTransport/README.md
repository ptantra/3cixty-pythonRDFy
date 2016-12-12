LONDON RDF DATA DOCUMENTATION
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
<p>Example SPARQL query: T.B.C.</p>
</br>

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
</br>

Bus TfL data: Bus correspondence
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

Underground, overground, tram and light rail TfL data 
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
        <http://data.linkedevents.org/transit/london/station/1cc33497-2fee-5bbc-bbf5-a4014ed6c6d6>,
        <http://data.linkedevents.org/transit/london/station/244f5aa3-dd09-59e0-a0a2-bcd2a401a713>,
        <http://data.linkedevents.org/transit/london/station/2dc668b9-de4c-5425-881a-c71065c7c1a7>,
        <http://data.linkedevents.org/transit/london/station/368ed3d7-1108-5fd2-ac8e-70f9120b7be3>,
        <http://data.linkedevents.org/transit/london/station/45950594-0bfb-5e17-91e3-780e15b07017>,
        <http://data.linkedevents.org/transit/london/station/4e277dfe-5ec9-5c1c-8f40-56a6df695e48>,
        <http://data.linkedevents.org/transit/london/station/5999c426-7224-58c1-95db-b9135e2920b5>,
        <http://data.linkedevents.org/transit/london/station/5c565ac5-b2e9-5d5a-a585-3b9d48a28234>,
        <http://data.linkedevents.org/transit/london/station/6989c255-63e3-569e-9728-f2729fdf654f>,
        <http://data.linkedevents.org/transit/london/station/71cfd603-4a74-56c6-bffd-2ab1200b00aa>,
        <http://data.linkedevents.org/transit/london/station/9a7dce4c-5851-59f9-ae56-7af784891703>,
        <http://data.linkedevents.org/transit/london/station/a3bf15dc-6ab2-5836-ad16-7f947215235c>,
        <http://data.linkedevents.org/transit/london/station/aa3f96b7-318e-512f-982f-4cd64940c896>,
        <http://data.linkedevents.org/transit/london/station/ab97ad9b-0239-5e10-98e6-933a5b291a37>,
        <http://data.linkedevents.org/transit/london/station/b757fb7c-076e-5416-955f-8af96f769643>,
        <http://data.linkedevents.org/transit/london/station/ceef7697-3341-575d-bc93-aa18d4197799>,
        <http://data.linkedevents.org/transit/london/station/d72cdea5-0c99-5950-a7a3-2c89575d3275>,
        <http://data.linkedevents.org/transit/london/station/dcff3a7d-d8e6-55a6-9ba2-ecb5fc49e033>,
        <http://data.linkedevents.org/transit/london/station/ee0fea2e-1d2c-52a4-8065-dd7ac7da4f16>,
        <http://data.linkedevents.org/transit/london/station/ef660c68-0a13-510e-9e42-7bf0dd379cae>,
        <http://data.linkedevents.org/transit/london/station/f2a20c52-1cc2-5e66-93c9-b1fe22c55bd8>,
        <http://data.linkedevents.org/transit/london/station/fc822d85-4664-5800-b16f-d69db38eb5f5>,
        <http://data.linkedevents.org/transit/london/station/ff90da5f-8d25-5c2d-b68a-724f77eea35c> .
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
<p>Example SPARQL query: T.B.C.</p>
</br>

