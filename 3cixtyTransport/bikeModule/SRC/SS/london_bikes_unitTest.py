from SPARQLWrapper import SPARQLWrapper, JSON
import unittest

'''
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
'''




sparql = SPARQLWrapper("http://3cixty.casa.ucl.ac.uk:8890/sparql")
sparql.setQuery("""
PREFIX gsp: <http://www.opengis.net/ont/geosparql#>
PREFIX ev: <http://data.linkedevents.org/event/>
PREFIX pl: <http://data.linkedevents.org/location/>
SELECT DISTINCT ?cat ?venue ?title #?description ?img ?long ?lat ?cell ?seeAlso
WHERE {
	GRAPH ?g {?venue a dul:Place .}
	VALUES ?g {<http://3cixty.com/london/tfl>}
OPTIONAL{?venue <http://data.linkedevents.org/def/location#businessType> ?cat .}
	?venue rdfs:label ?title .
 FILTER(!bound(?cat))
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print result["cat"]["value"]
    print result["venue"]["value"]
    print result["title"]["value"]


class TestStringMethods(unittest.TestCase):

    def test_upper(self):

        self.sparql = SPARQLWrapper("http://3cixty.casa.ucl.ac.uk:8890/sparql")
        self.sparql.setQuery("""
        SELECT distinct ?publisher ?cat COUNT(DISTINCT ?event) AS ?numberEvents
WHERE {
 ?event a lode:Event.
 ?event dc:publisher ?publisher.
 ?event lode:hasCategory ?cat.
} GROUP BY ?publisher ?cat
  ORDER BY DESC(?numberEvents)
        """)
        self.sparql.setReturnFormat(JSON)
        self.results = sparql.query().convert()

        for result in self.results["results"]["bindings"]:
            print self.result["cat"]["value"]
            print self.result["venue"]["value"]
            print self.result["title"]["value"]

            assertFalse(self.result["cat"]["value"] <= 0)

    def test_isupper(self):
        self.assertTrue('Foo'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)