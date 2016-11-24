__author__ = '3cixty team'

import csv, os, re, unicodedata
from time import strftime

#os.chdir('Z:/3cixty/3cixty_160822/3cixtyEnviro/wundergroundModule/') # @wick1 windows setup
os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/') # @patrick CASA Mac setup
print os.getcwd()


if not os.path.exists('IN/validation/'):
    os.makedirs(strftime('IN/validation/'))

##CHECKS

def validateEmpty(Content):
    if Content =='NaN' or Content =='NONE':
        return 1
    elif Content == '':
        return 1
    else:
        return 0


'''
def validateNaptan(Naptan):
    if Naptan[-1].isdigit() and Naptan[-2].isdigit():
        return 5
    else:
        if Naptan[0] == "9":
            return 0
        else:
            return 5
        return 0
'''

def validateNumber(Content):
    try:
        float(Content)
        return 0
    except ValueError:
        pass
    try:
        unicodedata.numeric(Content)
        return True
    except (TypeError, ValueError):
        pass
        return 2

def validateAlphaNumeric(Content):
    if not Content.isalnum():
        return 2
    else:
        return 0

'''
def validateUrl(url):
    if not validators.url(url):
        return 3
    else:
        return 0
'''

def cleanSpecialCharacter(row):
    for index in range(0,len(row)):
        cleaned=re.sub('[<>#]','',row[index])
        row[index]=re.sub('[/]','-',cleaned)
    return row

def checkEqualValues(iterator):
    iterator = iter(iterator)
    first = next(iterator)
    if not all(first == rest for rest in iterator):
        return 0
    else:
        return 4

##FUNCTIONS
def writeCsv(output,row):
    #print row
    row=[(str.strip()) for str in row]
    if os.path.exists(output):
        f = open(output, 'a')
        spamwriter = csv.writer(f,lineterminator='\n')
        spamwriter.writerow(row)
    else:
        f = open(output, 'w+')
        spamwriter = csv.writer(f,lineterminator='\n')
        spamwriter.writerow(row)
        f.close()

def writeLogP(status,row):

    if status==1:
        row.append('Error: Empty fields')
        writeCsv('IN/validation/wunderground_errorLog_p1.csv',row)
        return 1
    elif status==2:
        row.append('Error: Non numeric and/or digit value')
        writeCsv('IN/validation/wunderground_errorLog_p2.csv',row)
        return 2
    elif status == 3:
        row.append('Error: Invalid URL')
        writeCsv('IN/validation/wunderground_errorLog_p3.csv', row)
        return 3
    elif status == 4:
        row.append('Error: Equal values Invalid URL')
        writeCsv('IN/validation/wunderground_errorLog_p4.csv', row)
        return 4
    elif status == 5:
        row.append('Error: Naptan')
        writeCsv('IN/validation/wunderground_errorLog_p4.csv', row)
        return 5

def deleteFile(filename):
    filename = 'IN/validation/wundergound_validated.csv'
    try:
        os.remove(filename)
    except OSError:
        pass

def writeCleaned(row):
    #writeCsv('IN/validation/wunderground_validated.csv',row)
    writeCsv('IN/validation/wunderground_validated.csv', row)
    return 0

if __name__ == "__main__":
    ##create non duplicate file
    #inFile = open('IN/stations_full.csv', 'r')
    inFile = open('IN/stations_fullNoDuplicate.csv','r')
    outFile = open("IN/validation/wunderground_validated.csv", 'w')
    listLines = []

    for line in inFile:
        if line in listLines:
            continue
        else:
            outFile.write(line)
            listLines.append(line)

    outFile.close()
    inFile.close()

    #inFileB = "ferryModule/IN/" + strftime("%Y%m%d") + "/wunderground-stops.csv"
    inFileB = "IN/stations_fullNoDuplicate.csv"

    f =open(inFileB, 'rU')
    print f
    wundergroundData=list(csv.reader(f,delimiter=';', quotechar='"'))

    '''#delete the last line if it contains the ASCII code
    if wundergroundData[0] == '\x1a' and wundergroundData[1:].isnull().all(): #look through csv and clean the last row if ASCII or null
        wundergroundData = wundergroundData[:-1]
    '''
    #print wundergroundData

    print  'Validating and cleaning....'

    #deleteFile(pathf + 'IN/validation/wunderground_validated.csv')

    if os.path.exists('IN/validation/wunderground_validated.csv'):
        os.remove('IN/validation/wunderground_validated.csv')

    for index in range(1,len(wundergroundData)):

        # Clean special character for all columns

        '''
        wundergroundData[index]=cleanSpecialCharacter(wundergroundData[index][2])
        wundergroundData[index]=cleanSpecialCharacter(wundergroundData[index][3])
        wundergroundData[index]=cleanSpecialCharacter(wundergroundData[index][4])
        wundergroundData[index]=cleanSpecialCharacter(wundergroundData[index][9])
        wundergroundData[index]=cleanSpecialCharacter(wundergroundData[index][10])
        '''

        # Validate data
        status0 = validateEmpty(wundergroundData[index][0])#returns 0 or 1
        status1 = validateEmpty(wundergroundData[index][1])#returns 0 or 1
        status2 = validateEmpty(wundergroundData[index][2])#returns 0 or 1
        status3 = validateEmpty(wundergroundData[index][3])#returns 0 or 1
        status4 = validateEmpty(wundergroundData[index][4])#returns 0 or 1

        status5 = validateAlphaNumeric(wundergroundData[index][0])#returns 0 or 3
        status6 = validateNumber(wundergroundData[index][3])#returns 0 or 3
        status7 = validateNumber(wundergroundData[index][4])  # returns 0 or 3

        #status10=checkEqualValues(wundergroundData[index][0])#returns 0 or 4

        if status0==0 and status1==0 and status2==0  and status3==0 and status4==0 and status5==0 and status6==0 and status7==0 : # and status8==0 : #and status9==0 : #and status10==0 : #and status11==0:
            writeCleaned(wundergroundData[index])
            continue

        if status0!=0:
            writeLogP(status0,wundergroundData[index])
        elif status1!=0:
            writeLogP(status1,wundergroundData[index])
        elif status2!=0:
            writeLogP(status2,wundergroundData[index])
        elif status3!=0:
            writeLogP(status3,wundergroundData[index])
        elif status4!=0:
            writeLogP(status4,wundergroundData[index])
        elif status5!=0:
            writeLogP(status5,wundergroundData[index])
        elif status6!=0:
            writeLogP(status6,wundergroundData[index])
        elif status7!=0:
            writeLogP(status7,wundergroundData[index])
        #elif status8 != 0:
        #    writeLogP(status8, wundergroundData[index])
        #elif status9 != 0:
        #   writeLogP(status9, wundergroundData[index])
        #elif status10 != 0:
        #  writeLogP(status10, wundergroundData[index])
        #elif status11 != 0:
         #   writeLogP(status11, wundergroundData[index])


    print "DONE pre validating file"


