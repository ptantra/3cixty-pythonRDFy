import os, threading, imp
from time import strftime

def busRetrieveData():
    print "* thread bus_retrieveData"
    os.system('python SRC/bus_retrieveData.py')
    return

def busPreValidate():
    print "* * thread bus_preValidate"
    os.system('python SRC/bus_preValidate.py')
    return

def busRdfy():
    print "* * * thread bus_rdfy"
    os.system('python SRC/bus_rdfy.py')
    return

def busPostValidate():
    print "* * * * thread bus_postValidate"
    os.system('python SRC/bus_postValid.py')
    return

def busZip():
    print "* * * * * thread bus_zip"
    os.system('python SRC/bus_toZip.py')
    return

def main():
    threads =[]

    s = threading.Thread(target = busRetrieveData)
    threads.append(s)
    s.start()
    s.join()

    t = threading.Thread(target=busPreValidate)
    threads.append(t)
    t.start()
    t.join()

    l = threading.Thread(target=busRdfy)
    threads.append(l)
    l.start()
    l.join()

    x = threading.Thread(target=busPostValidate)
    threads.append(x)
    x.start()
    x.join()

    m = threading.Thread(target=busZip)
    threads.append(m)
    m.start()

if __name__ == '__main__':
    main()

