import os, random, threading
from time import strftime

#os.chdir('/Users/patrick/3cixty/codes/3cixtyTransport/') # @patrick CASA Mac setup
#print os.getcwd()

def subwayRetrieveFile():
    print "* thread subway_retrieveFile"
    os.system('python SRC/london_subway_retrieveFile.py')
    return

def subwayRdfy():
    print "* thread subway_rdfy"
    os.system('python SRC/london_subway_rdfy.py')
    return

def subwayPostValid():
    print "* * thread subway_postValid"
    os.system('python SRC/london_subway_postValid.py')
    return

def subwayZip():
    print "* * * thread subwayZip"
    os.system('python SRC/london_subway_toZip.py')
    return

def dlrRdfy():
    print "* thread dlr_rdfy"
    os.system('python SRC/london_dlr_rdfy.py')
    return

def dlrPostValid():
    print "* * thread dlr_postValid"
    os.system('python SRC/london_dlr_postValid.py')
    return

def dlrZip():
    print "* * * thread dlrZip"
    os.system('python SRC/london_dlr_toZip.py')
    return

def tramRdfy():
    print "* thread tram_rdfy"
    os.system('python SRC/london_tram_rdfy.py')
    return

def tramPostValid():
    print "* * thread tram_postValid"
    os.system('python SRC/london_tram_postValid.py')
    return

def tramZip():
    print "* * * thread tramZip"
    os.system('python SRC/london_tram_toZip.py')
    return

def main():
    threads =[]

    #a = threading.Thread(target=subwayRetrieveFile)
    #threads.append(a)
    #a.start()
    #a.join()

    b = threading.Thread(target=subwayRdfy)
    threads.append(b)
    b.start()
    b.join()

    c = threading.Thread(target=subwayPostValid)
    threads.append(c)
    c.start()
    c.join()

    d = threading.Thread(target=subwayZip)
    threads.append(d)
    d.start()
    d.join()

    a1 = threading.Thread(target=tramRdfy)
    threads.append(a1)
    a1.start()
    a1.join()

    b1 = threading.Thread(target=tramPostValid)
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

    b2 = threading.Thread(target=dlrPostValid)
    threads.append(b2)
    b2.start()
    b2.join()

    c2 = threading.Thread(target=dlrZip)
    threads.append(c2)
    c2.start()
    c2.join()

if __name__ == '__main__':
    main()

