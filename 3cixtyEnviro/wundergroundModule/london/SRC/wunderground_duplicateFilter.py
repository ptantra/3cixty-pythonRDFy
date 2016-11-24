import os

#os.chdir('Z:/3cixty/3cixty_160822/3cixtyEnviro/wundergroundModule/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/london/') # @patrick CASA Mac setup
print os.getcwd()

inFile = open('DATA/stations_full.csv','r')
outFile = open('DATA/stations_fullNoDuplicate.csv','w')
listLines = []

for line in inFile:
    if line in listLines:
        continue
    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()
inFile.close()