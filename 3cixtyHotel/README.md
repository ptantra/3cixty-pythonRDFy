
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
