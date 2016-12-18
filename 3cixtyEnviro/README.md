
Wunderground stations
------------
The rdf graph for the London wunderground weather stations is generated with data collected from Wunderground forecast api, as published by [Wunderground](https://www.wunderground.com/). The weather stations emits various weather readings. Included in the rdf graph is the weather condition reading and its corresponding timestamps. Each weather station can be identified by its given station id number and is immediately linked with its geometry and address information. A uri observation link is also listed. Because the observations are to be updated periodically, the observations are graphed in a separate 'real-time' ttl file.

<p>Each weather station node contains:</p>
<ul>
<li>Identifier</li>
<li>Label</li>
<li>Publisher</li>
<li>Link to weather station observation properties</li>
<li>Link to weather address properties</li>
<li>Weather station geometry has both point coordinates and geoSPARQL literal value.</li>
</ul>
[Wunderground weather station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStations.svg)</br>
[Example of a Wunderground weather station RDF ontology diagram: East Street bus stop](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStationsExample.svg)
[Real time observation from a Wunderground weather station RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStations.svg)</br>
[Example of a real time observation from a Wunderground weather station RDF ontology diagram: East Street bus stop](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/wundergroundStationsExample.svg)
<p>London Wunderground weather station turtle file example:</p>
```Turtle
<http://data.linkedevents.org/wunderground/deviceId/I90579897> a ssn:sensingDevice ;
    rdfs:label "I90579897" ;
    dc:publisher <https://www.wunderground.com> ;
    ssn:hasLocation <http://data.linkedevents.org/wunderground/deviceId/I90579897/address> ;
    ssn:hasRegion <http://data.linkedevents.org/wunderground/deviceId/I90579897/geometry> ;
    ssn:observationResult <http://data.linkedevents.org/wunderground/observation/59ed2715-f5aa-53ac-bc01-1eb72c028e7d> .
    
<http://data.linkedevents.org/wunderground/deviceId/I90579897/address> a schema:PostalAddress ;
    schema:addressLocality "North Finchley" ;
    schema:streetAddress "North Finchley" ;
    locn:address "North Finchley, North Finchley" ;
    ssn:isLocationOf <http://data.linkedevents.org/wunderground/deviceId/I90579897> .

<http://data.linkedevents.org/wunderground/deviceId/I90579897/geometry> a dul:spaceRegion,
        geo:Point ;
    geo:lat "51.613396"^^xsd:double ;
    geo:long "-0.17326"^^xsd:double ;
    locn:geometry "POINT (51.613396 -0.17326)"^^geosparql:wktLiteral .
```
<p>Each real time weather station observation node contains:</p>
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
    ssn:property "weather condition"@en .
```
<p>Example SPARQL query:</p>
```Turtle
prefix ssn: <http://www.w3.org/ns/ssn/>

SELECT DISTINCT ?name ?publisher ?lat ?long  ?area
WHERE
{
    ?ref a ssn:sensingDevice ; rdfs:label ?name ; ssn:hasLocation ?addr ; dc:publisher ?publisher  ; ssn:hasRegion ?geometry .
    ?addr a schema:PostalAddress ; locn:address ?area.
    ?geometry geo:long ?long ; geo:lat ?lat .
 BIND(bif:st_distance(bif:st_point(?long, ?lat), bif:st_point(-0.1292638, 51.5254607)) AS ?distance)
 FILTER(?publisher=<https://www.wunderground.com> && ?distance <= 100)
 }
 ORDER BY ASC (?distance)
 LIMIT 40
```
</br>




