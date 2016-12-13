
AirBnB
-------
<p>The AirBnB ttl dataset for London is obtained from a secondary source: www.insideairbnb.com. A website dedicated to test Airbnb's claim to be part of the "sharing economy" and disrupting the hotel industry by providing the data scraped from airbnb's websites for analysis. AirBnB itself do not openly share its data via an official api.</p>

Browse the data for your city below, and see for yourself.</p>
<p>The semantic dataset contains:<p>
<ul>
<li>Unique URI for each accommodation offering</li>
<li>Host name and id along with the description of each offering</li>
<li>Price, minimum nights stay</li>
<li>Business type and yearly availability</li>
<li>Geometry and address URIs</li>
<li>Location as both point coordinates and geoSPARQL literal values</li>
<li>Locality and neighbourhood</li>
</ul>

[London AirBnB RDF ontology diagram](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/airBnB_rdfDiagram.svg)</br>
[Example of London AirBnB RDF ontology diagram: Jonas in Hackney](https://github.com/3cixty/knowledgebase/blob/master/documentation/London/airBnbExample_rdfDiagram.svg)
<p>AirBnB turtle file example:</p>
```Turtle
locationRes:00017da-ac0a-50ef-96df-90e84258115a a dul:Place,
        acco:Hotel,
        gr:Offering ;
    rdfs:label "Elegant Family Home In Hackney" ;
    locationOnt:businessType threecixtyKOS:residence ;
    dc:identifier "10916060" ;
    dc:publisher <https://www.airbnb.com> ;
    gr:description "Entire home apt" ;
    gr:hasCurrencyValue "189"^^xsd:GBP ;
    gr:hasUnitOfMeasurement "3"^^xsd:minimumNights ;
    sioc:has_host "Tom" ;
    owl:sameAs <http://www.airbnb.co.uk/rooms/10916060> ;
    geo:location <http://data.linkedevents.org/location/00017da-ac0a-50ef-96df-90e84258115a/geometry> ;
    locn:address <http://data.linkedevents.org/location/00017da-ac0a-50ef-96df-90e84258115a/address> .
    
<http://data.linkedevents.org/location/00017da-ac0a-50ef-96df-90e84258115a/geometry> a geo:Point ;
    geo:lat "51.539617334573705"^^xsd:double ;
    geo:long "-0.0450270513750273"^^xsd:double ;
    locn:geometry "POINT (51.539617334573705 -0.0450270513750273)"^^geosparql:wktLiteral .
    
<http://data.linkedevents.org/location/00017da-ac0a-50ef-96df-90e84258115a/address> a schema:postalAddress ;
    schema:addressCountry "UK" ;
    schema:addressLocality "Hackney" .
```
<p>Example SPARQL query:</p>
```SPARQL
prefix gr: <http://purl.org/goodrelations/v1#> 
prefix threecixtyKOS: <http://data.linkedevents.org/kos/3cixty/>

SELECT ?label ?price ?long ?lat ?description
WHERE {{?node rdfs:label ?label .
?node gr:description ?description . 
?node geo:location ?location .
?node gr:hasCurrencyValue  ?price . 
?node locationOnt:businessType threecixtyKOS:residence}
{?location geo:long ?long ; geo:lat ?lat . }
}limit 20
```
</br>
