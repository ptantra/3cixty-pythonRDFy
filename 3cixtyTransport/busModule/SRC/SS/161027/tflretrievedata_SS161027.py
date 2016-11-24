import urllib, json, csv

######gets bus station data from tfl website
inUrl = "http://data.tfl.gov.uk/tfl/syndication/feeds/bus-stops.csv?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0"
outFile = "./bus-stops.csv"
urllib.urlretrieve(inUrl, outFile)

###########pulls bike data from tfl api
def apiJsonCsv(inputURL):
    response = urllib.urlopen(inputURL)
    x = json.load(response)

    f = csv.writer(open( "./tfl_bikes.csv", "wb+"))
    f.writerow(["id",
                "url",
                "commonName",
                "placeType",
                "bikePointsNo",
                "timeModified",
                "nFilledDocks",
                "nEmptyDocks",
                "nTotalDocks",
                "lat",
                "lon"])

    for x in x:
        f.writerow([x["id"],
                    x["url"],
                    x["commonName"],
                    x["placeType"],
                    x["additionalProperties"][0]['value'],
                    x["additionalProperties"][0]['modified'],
                    x["additionalProperties"][6]['value'],
                    x["additionalProperties"][7]['value'],
                    x["additionalProperties"][8]['value'],
                    x["lat"],
                    x["lon"]])

    return x

def main():

    url="https://api.tfl.gov.uk/BikePoint?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0" #url for bike api
    apiJsonCsv(url) #json to csv conversion

    print ('Bike retrieve data')

if __name__ == "__main__":
    main();