import os, random, threading
from time import strftime

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/ferryModule/') # @patrick CASA Mac setup
print os.getcwd()

def ferryRetrieveData():
    print "* thread ferry_retrieveData"
    os.system('python SRC/ferry_retrieveData.py')
    return

def ferryPreValidate():
    print "* * thread ferry_preValidate"
    os.system('python SRC/ferry_preValidate.py')

def ferryRdfy():
    print "* * * thread ferry_rdfy"
    os.system('python SRC/ferry_rdfy.py')
    return

def ferryPostValidate():
    print "* * * * thread ferry_postValidate"
    os.system('python SRC/ferry_postValidate.py')
    return

def ferryZip():
    print "* * * * * thread ferryZip"
    os.system('python SRC/ferry_toZip.py')
    return

def main():
    threads =[]

    a = threading.Thread(target=ferryRetrieveData)
    threads.append(a)
    a.start()
    a.join()

    b = threading.Thread(target=ferryPreValidate())
    threads.append(b)
    b.start()
    b.join()

    c = threading.Thread(target=ferryRdfy)
    threads.append(c)
    c.start()
    c.join()

    d = threading.Thread(target=ferryPostValidate)
    threads.append(d)
    d.start()
    d.join()

    e = threading.Thread(target=ferryZip)
    threads.append(e)
    e.start()
    e.join()

if __name__ == '__main__':
    main()

