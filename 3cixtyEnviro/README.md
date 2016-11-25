
Wunderground stations
------------
<p>The rdf graph for the London wunderground weather stations is generated with data collected from Wunderground forecast api, as published by [Wunderground](https://www.wunderground.com/). The weather stations emits various weather readings. Included in the rdf graph is the weather condition reading and its corresponding timestamps. Each weather station can be identified by its given station id number and is immediately linked with its geometry and address information. A uri observation link is also listed. Because the observations are to be updated periodically, the observations are graphed in a separate 'real-time' ttl file.</p>
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




