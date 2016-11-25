##About 3cixty-pythonRDFy
These codes are part of the London component of the 3cixty project development. These codes are mostly written in Python, and they function to retrieve, manipulate and transform unstructured data into Turtle RDF and to validate it then. 

The 3cixty project aims to create city-specific 'knowledge bases' comprising of the city's events, places, transport facilities, environmental/weather information and hotel booking data that are semantically linked.

In this repository the I include the codes that are used on the London transport facilities, London environmental/weather data and London hotel booking data.

[![3cixty Video](http://img.youtube.com/vi/K6_ylq1ufH8/0.jpg)](https://youtu.be/K6_ylq1ufH8)

https://youtu.be/K6_ylq1ufH8

http://img.youtu.be/K6_ylq1ufH8/0.jpg

##Requirements
To be used with [Python version 2.70](https://www.python.org/downloads/release/python-2712)

##Dependencies
The following Python libraries are required:
- [PyProj](https://pypi.python.org/pypi/pyproj)
- [Crontab](https://pypi.python.org/pypi/crontab/0.21.3)
- [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [pandas](http://pandas.pydata.org)
- [RDFlib](https://pypi.python.org/pypi/rdflib)
- CSV
- imp
- os
- sys
- zipfile
- uuid
- unicodedata 
- re

##Endpoints
The SPARQL endpoint for the London 3cixty knowledge base is http://3cixty.casa.ucl.ac.uk:8890/sparql. 

##Installation
To run these scripts, clone this Github repo and install all dependencies. Crucially, the folder and file structures must be maintained.
<p>Various 'modules' have been created for this project.</p>
1. Transport
    - commonModule
    - bikeModule
    - busModule
    - railModule
    - ferryModule
2. Environment
    - icriModule
    - wundergroundModule
3. Hotel
    - airbnbModule

To execute the files in the module, run the *_main.py file.
<p>bikeModule file structure example: </p>
````appleScript
|-- bikeModule',
|   |-- bike_main.py',
|   |-- SRC',
|   |   |-- bike_preValidate.py',
|   |   |-- bike_rdfy.py',
|   |   |-- bike_postValidate.py',
|   |   |-- bike_toZip.py',
|   |-- DATA',
|   |   |-- tfl_bikes_csv',
|   |   |-- tfl_bikes_dirty.ttl',
|   |   |-- tfl_bikes_validated.ttl',
|   |   |-- tfl_bikes.ttl',
|   |   |-- tfl_bikes.zip',
|   |   |-- LOG',
|   |   |   |-- tfl_bikes_errorLog1.csv',
|   |   |   |-- tfl_bikes_errorLog2.csv',
````
