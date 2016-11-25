#About 3cixty-pythonRDFy
These codes are part of the London component of the 3cixty project development. These codes are mostly written in Python, and they function to retrieve, manipulate and transform unstructured data into turtle RDF and to then validate it. 

The 3cixty project aim to create city specific 'knowledge bases' comprising of the city's events, places, transport facilities, environmental/weather information and hotel booking data that are semantically linked.

In this repository the I include the codes that are used on the London transport facilities, London environmental/ weather data and London hotel booking data.

##Requirements
To be used with [Python version 2.70](https://www.python.org/downloads/release/python-2712)

##Dependencies
The following Python libraries are required:
[PyProj](https://pypi.python.org/pypi/pyproj), [Crontab](https://pypi.python.org/pypi/crontab/0.21.3), CSV, [RDFlib](https://pypi.python.org/pypi/crontab/0.21.3), imp, os, sys, zipfile, [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [pandas](http://pandas.pydata.org), uuid, unicodedata and re

##Endpoints
The SPARQL endpoint for the London 3cixty knowledge base is http://3cixty.casa.ucl.ac.uk:8890/sparql. 

