import os, random, threading
from time import strftime

os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/railModule/') # @patrick CASA Mac setup
print os.getcwd()

def subwayRetrieveData():
    print "* thread subway_retrieveData"
    os.system('python SRC/underground_retrieveData.py')
    return

def undergroundPreValidate():
    print "* thread underground_preValidate"
    os.system('python SRC/underground_preValidate.py')
    return

def undergroundRdfy():
    print "* thread underground_rdfy"
    os.system('python SRC/underground_rdfy.py')
    return

def undergroundPostValidate():
    print "* * thread underground_postValidate"
    os.system('python SRC/underground_postValidate.py')
    return

def undergroundZip():
    print "* * * thread undergroundZip"
    os.system('python SRC/underground_toZip.py')
    return

def dlrPreValidate():
    print "* thread dlr_preValidate"
    os.system('python SRC/dlr_preValidate.py')
    return

def dlrRdfy():
    print "* thread dlr_rdfy"
    os.system('python SRC/dlr_rdfy.py')
    return

def dlrPostValidate():
    print "* * thread dlr_postValidate"
    os.system('python SRC/dlr_postValidate.py')
    return

def dlrZip():
    print "* * * thread dlrZip"
    os.system('python SRC/dlr_toZip.py')
    return

def tramPreValidate():
    print "* thread tram_preValidate"
    os.system('python SRC/tram_preValidate.py')
    return

def tramRdfy():
    print "* thread tram_rdfy"
    os.system('python SRC/tram_rdfy.py')
    return

def tramPostValidate():
    print "* * thread tram_postValid"
    os.system('python SRC/tram_postValidate.py')
    return

def tramZip():
    print "* * * thread tramZip"
    os.system('python SRC/tram_toZip.py')
    return

def overgroundPreValidate():
    print "* thread tram_preValidate"
    os.system('python SRC/overground_preValidate.py')
    return

def overgroundRdfy():
    print "* thread overground_rdfy"
    os.system('python SRC/overground_rdfy.py')
    return

def overgroundPostValidate():
    print "* * thread overground_postValid"
    os.system('python SRC/overground_postValidate.py')
    return

def overgroundZip():
    print "* * * thread overgroundZip"
    os.system('python SRC/overground_toZip.py')
    return

def main():
    threads =[]

    #a = threading.Thread(target=undergroundRetrieveData)
    #threads.append(a)
    #a.start()
    #a.join()

    b = threading.Thread(target=undergroundPreValidate())
    threads.append(b)
    b.start()
    b.join()

    c = threading.Thread(target=undergroundRdfy)
    threads.append(c)
    c.start()
    c.join()

    d = threading.Thread(target=undergroundPostValidate)
    threads.append(d)
    d.start()
    d.join()

    e = threading.Thread(target=undergroundZip)
    threads.append(e)
    e.start()
    e.join()




    a1 = threading.Thread(target=tramRdfy)
    threads.append(a1)
    a1.start()
    a1.join()

    a11 = threading.Thread(target=tramPreValidate)
    threads.append(a11)
    a11.start()
    a11.join()

    b1 = threading.Thread(target=tramPostValidate)
    threads.append(b1)
    b1.start()
    b1.join()

    c1 = threading.Thread(target=tramZip)
    threads.append(c1)
    c1.start()
    c1.join()

    a2 = threading.Thread(target=dlrRdfy)
    threads.append(a2)
    a2.start()
    a2.join()

    a22 = threading.Thread(target=dlrPreValidate)
    threads.append(a22)
    a22.start()
    a22.join()

    b2 = threading.Thread(target=dlrPostValidate)
    threads.append(b2)
    b2.start()
    b2.join()

    c2 = threading.Thread(target=dlrZip)
    threads.append(c2)
    c2.start()
    c2.join()

    a3 = threading.Thread(target=overgroundRdfy)
    threads.append(a3)
    a3.start()
    a3.join()

    a33 = threading.Thread(target=overgroundPreValidate)
    threads.append(a33)
    a33.start()
    a33.join()

    b3 = threading.Thread(target=overgroundPostValidate)
    threads.append(b3)
    b3.start()
    b3.join()

    c3 = threading.Thread(target=overgroundZip)
    threads.append(c3)
    c3.start()
    c3.join()

if __name__ == '__main__':
    main()

