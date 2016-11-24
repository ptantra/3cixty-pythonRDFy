import os, threading, imp
from time import strftime

os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/') # @patrick CASA Mac setup
print os.getcwd()

def wundergroundRetrieveData():
    print "* thread wunderground_retrieveData"
    os.system('python SRC/wunderground_retrieveData.py')
    return

def wundergroundPreValid():
    print "* * thread wunderground_preValid"
    os.system('python SRC/wunderground_preValid.py')
    return

def wundergroundRdfy():
    print "* * * thread wunderground_rdfy"
    os.system('python SRC/wunderground_rdfy.py')
    return

def wundergroundPostValid():
    print "* * * * thread wunderground_postValid"
    os.system('python SRC/wunderground_postValid.py')
    return

def wundergroundZip():
    print "* * * * * thread wunderground_zip"
    os.system('python SRC/wunderground_toZip.py')
    return

def main():
    threads =[]

    '''
    s = threading.Thread(target = wundergroundRetrieveData)
    threads.append(s)
    s.start()
    s.join()
    '''
    t = threading.Thread(target=wundergroundPreValid)
    threads.append(t)
    t.start()
    t.join()

    l = threading.Thread(target=wundergroundRdfy)
    threads.append(l)
    l.start()
    l.join()

    x = threading.Thread(target=wundergroundPostValid)
    threads.append(x)
    x.start()
    x.join()

    m = threading.Thread(target=wundergroundZip)
    threads.append(m)
    m.start()

if __name__ == '__main__':
    main()

