__author__ = '3cixty team'

import csv, os, re
from time import strftime

os.chdir('/Users/patrick/3cixty/codes/3cixtyHotel/airbnbModule/nice/') # @patrick CASA Mac setup
print os.getcwd()

if not os.path.exists('DATA/'):
    os.makedirs('DATA/')

if not os.path.exists('DATA/LOG/'):
    os.makedirs('DATA/LOG/')


##CHECKS
def validateStopCode(StopCode):
    if not StopCode or StopCode =='NaN' or StopCode =='NONE':
        return 2
    else:
        return 0


def validateBusStop(BusStop):
    if not BusStop or BusStop =='NaN' or BusStop =='NONE':
        return 1
    else:
        return 0

'''
def validateNaptan(Naptan):
    if not Naptan or Naptan =='NaN' or Naptan =='NONE':
        return 1
    else:
        if(Naptan.find('E')!=-1 and Naptan.find('.')!=-1):
            return 1
        else:
            naptanlen=len(Naptan)
            if(naptanlen>9):
                if (Naptan[(naptanlen-2)].isdigit() and Naptan[(naptanlen-1)].isdigit()):
                    return 1
                else:
                    return 0
            else:
                return 1
'''


def validateHeading(Heading):
    if not Heading or Heading =='NaN' or Heading =='NONE':
        return 1
    else:
        return 0

def validateStopArea(Stoparea):
    if not Stoparea or Stoparea =='NaN' or Stoparea =='NONE':
        return 1
    else:
        return 0

def validateVirtualBusStop(VirtualBusStop):
    if not VirtualBusStop or VirtualBusStop =='NaN' or VirtualBusStop =='NONE':
        return 1
    else:
        return 0

def validateLonLatNum(Lon,Lat):
    if not Lon.isdigit() and not Lat.isdigit():
        return 2
    else:
        return 0

def validateLonLatNaN(Lon,Lat):
    if (not Lon or Lon=='NaN' or Lon=='NONE' ) and (not Lat or Lat=='NaN' or Lat=='NONE'):
        return 1
    else:
        return 0

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
        row.append('P1')
        writeCsv('DATA/LOG/airbnb_errorLog_p1.csv',row)
        return 1
    elif status==2:
        row.append('P2')
        writeCsv('DATA/LOG/airbnb_errorLog_p2.csv',row)
        return 2

def deleteFile(filename):
    filename = 'DATA/LOG/airbnb_validated.csv'
    try:
        os.remove(filename)
    except OSError:
        pass

def cleanSpecialCharacter(row):
    for index in range(0,len(row)):
        cleaned=(re.sub('[<>#*]',' ',row[index]))
        row[index]=re.sub('[/]','-',cleaned)
    return row

def writeCleaned(row):
    #writeCsv(pathf + 'IN/validation/bus_validated.csv',row)
    writeCsv('DATA/airbnbLondon_validated.csv', row)
    return 0


if __name__ == "__main__":

    pathf = "./"
    inFileB = pathf + "DATA/airbnbNiceTest.csv"

    f =open(inFileB, 'rU')
    print f
    data=list(csv.reader(f,delimiter=',', quotechar='"'))

 #delete the last line if it contains the ASCII code
    if data[0] == '\x1a' and data[1:].isnull().all():
        data = data[:-1]#look through csv and clean the last row if ASCII or null

    #print data

    print  'Validating and cleaning....'

    #deleteFile(pathf + 'IN/validation/bus_validated.csv')

    if os.path.exists(pathf + 'DATA/airbnNice_Validated.csv'):
        os.remove(pathf + 'DATA/airbnbNice_Validated.csv')

    for index in range(1,len(data)):

        # Clean special character for all columns
        data[index]=cleanSpecialCharacter(data[index])
        #print data[index]

        # Validate data
        status0=validateStopCode(data[index][0])
        status1=validateBusStop(data[index][1])
        #status1=validateLonLatNum(data[index][5],data[index][6])
        status2=validateLonLatNaN(data[index][5],data[index][6])
        status3=validateHeading(data[index][2])
        status4=validateStopArea(data[index][3])
        status5=validateVirtualBusStop(data[index][4])

        if status0==0 and status1==0 and status2==0 and status3==0 and status4==0 and status5==0:


            writeCleaned(data[index])
            continue

        '''
        if status0==0 and status1==0 and status2==0 and status3==0 and status4==0 and status5==0 and status6==0 and status7==0:
            writeCleaned(data[index])
            continue
        '''

        if status0!=0 :
            writeLogP(status0,data[index])
        elif status1!=0:
            writeLogP(status1,data[index])
        elif status2!=0:
            writeLogP(status2,data[index])
        elif status3!=0:
            writeLogP(status3,data[index])
        elif status4!=0:
            writeLogP(status4,data[index])
        elif status5!=0:
            writeLogP(status5,data[index])
        elif status6!=0:
            writeLogP(status6,data[index])
        '''
        elif status7!=0:
            writeLogP(status7,data[index])
        '''

    print "DONE pre validating file"


