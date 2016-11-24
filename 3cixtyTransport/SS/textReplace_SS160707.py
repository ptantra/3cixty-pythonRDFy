
from time import strftime

pathf = "/Users/patrick/3cixty/IN/tfl/"
#pathf = "z:/3cixty/3cxity_160627/in/TFL/"
inputFile = pathf + "tfl_bikes" + strftime("%Y%m%d") + "_toVal.ttl"
outFile = pathf + "tfl_bikes" + strftime("%Y%m%d") + ".ttl"

f = open(inputFile,'r')
filedata = f.read()
f.close()

newdata = filedata.replace("xsd:placeholder","xsd:double")

f = open(outFile,'w')
f.write(newdata)
f.close()