import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://3cixty.casa.ucl.ac.uk:8890/sparql")
sparql.setQuery("""
SELECT distinct ?publisher ?cat COUNT(DISTINCT ?event) AS ?numberEvents
WHERE {
 ?event a lode:Event.
 ?event dc:publisher ?publisher.
 ?event lode:hasCategory ?cat.
} GROUP BY ?publisher ?cat
  ORDER BY DESC(?numberEvents)
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

res=[]

for result in results["results"]["bindings"]:
    numberEvents = result["numberEvents"]["value"]
    publisher = result["publisher"]["value"]
    category = result["cat"]["value"]

    res.append((numberEvents, publisher, category))

print res

eventsDf = pd.DataFrame(numberEvents)


print eventsDf