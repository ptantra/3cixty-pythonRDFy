__author__ = '3cixty team'

import csv, os, re, unicodedata
from time import strftime

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/subwayModule/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists('DATA/'):
    os.makedirs(strftime('DATA/'))

##CHECKS

def validateEmpty(Content):
    if Content =='NaN' or Content =='NONE':
        return 1
    elif Content == '':
        return 1
    else:
        return 0


def validateNaptan(Naptan):
    if Naptan[-1].isdigit() and Naptan[-2].isdigit():
        return 5
    else:
        if Naptan[0] == "9":
            return 0
        else:
            return 5
        return 0


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
        writeCsv(pathf + 'DATA/underground_errorLog_p1.csv',row)
        return 1
    elif status==2:
        row.append('Error: Non numeric and/or digit value')
        writeCsv(pathf + 'DATA/underground_errorLog_p2.csv',row)
        return 2
    elif status == 3:
        row.append('Error: Invalid URL')
        writeCsv(pathf + 'DATA/underground_errorLog_p3.csv', row)
        return 3
    elif status == 4:
        row.append('Error: Equal values Invalid URL')
        writeCsv(pathf + 'DATA/underground_errorLog_p4.csv', row)
        return 4
    elif status == 5:
        row.append('Error: Naptan')
        writeCsv(pathf + 'DATA/underground_errorLog_p4.csv', row)
        return 5

def deleteFile(filename):
    filename = pathf + 'DATA/undergound_validated.csv'
    try:
        os.remove(filename)
    except OSError:
        pass

def writeCleaned(row):
    #writeCsv(pathf + 'IN/validation/underground_validated.csv',row)
    writeCsv(pathf + 'DATA/underground_validated.csv', row)
    return 0

if __name__ == "__main__":

    pathf = "./"
    #inFileB = pathf + "ferryModule/IN/" + strftime("%Y%m%d") + "/underground-stops.csv"
    inFileB = pathf + "DATA/subwayLine_ALL.csv"

    f =open(inFileB, 'rU')
    print f
    undergroundData=list(csv.reader(f,delimiter=',', quotechar='"'))

    '''#delete the last line if it contains the ASCII code
    if undergroundData[0] == '\x1a' and undergroundData[1:].isnull().all(): #look through csv and clean the last row if ASCII or null
        undergroundData = undergroundData[:-1]
    '''
    #print undergroundData

    print  'Validating and cleaning....'

    #deleteFile(pathf + 'IN/validation/underground_validated.csv')

    if os.path.exists(pathf + 'DATA/underground_validated.csv'):
        os.remove(pathf + 'DATA/underground_validated.csv')

    for index in range(1,len(undergroundData)):

        # Clean special character for all columns

        '''
        undergroundData[index]=cleanSpecialCharacter(undergroundData[index][2])
        undergroundData[index]=cleanSpecialCharacter(undergroundData[index][3])
        undergroundData[index]=cleanSpecialCharacter(undergroundData[index][4])
        undergroundData[index]=cleanSpecialCharacter(undergroundData[index][9])
        undergroundData[index]=cleanSpecialCharacter(undergroundData[index][10])
        '''

        # Validate data
        status0 = validateEmpty(undergroundData[index][0])#returns 0 or 1
        status1 = validateEmpty(undergroundData[index][1])#returns 0 or 1
        status2 = validateEmpty(undergroundData[index][3])#returns 0 or 1
        status3 = validateEmpty(undergroundData[index][4])#returns 0 or 1
        status4 = validateEmpty(undergroundData[index][5])#returns 0 or 1

        status5 = validateNaptan(undergroundData[index][0])#returns 0 or 5

        status6 = validateAlphaNumeric(undergroundData[index][0])#returns 0 or 3
        status7 = validateNumber(undergroundData[index][3])#returns 0 or 3
        status8 = validateNumber(undergroundData[index][4])  # returns 0 or 3

        #status10=checkEqualValues(undergroundData[index][0])#returns 0 or 4


        if status0==0 and status1==0 and status2==0  and status3==0 and status4==0 and status5==0 and status6==0 and status7==0 and status8==0 : #and status9==0 : #and status10==0 : #and status11==0:
            writeCleaned(undergroundData[index])
            continue

        if status0!=0:
            writeLogP(status0,undergroundData[index])
        elif status1!=0:
            writeLogP(status1,undergroundData[index])
        elif status2!=0:
            writeLogP(status2,undergroundData[index])
        elif status3!=0:
            writeLogP(status3,undergroundData[index])
        elif status4!=0:
            writeLogP(status4,undergroundData[index])
        elif status5!=0:
            writeLogP(status5,undergroundData[index])
        elif status6!=0:
            writeLogP(status6,undergroundData[index])
        elif status7!=0:
            writeLogP(status7,undergroundData[index])
        elif status8 != 0:
            writeLogP(status8, undergroundData[index])
        #elif status9 != 0:
        #   writeLogP(status9, undergroundData[index])
        #elif status10 != 0:
        #  writeLogP(status10, undergroundData[index])
        #elif status11 != 0:
         #   writeLogP(status11, undergroundData[index])


    print "DONE pre validating file"

