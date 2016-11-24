import os, random, threading
from time import strftime

def airbnbRdfy():
    print "* thread airbnb_rdfy"
    os.system('python SRC/airbnb_rdfy.py')
    return

def airbnbPreValidate():
    print "* thread airbnb_preValidate"
    os.system('python SRC/airbnb_preValidate.py')
    return

def airbnbPostValidate():
    print "* * thread airbnb_postValid"
    os.system('python SRC/airbnb_postValidate.py')
    return

def airbnb_toZip():
    print "* * * thread airbnb_toZip"
    os.system('python SRC/airbnb_toZip.py')
    return

def main():
    threads =[]

    a = threading.Thread(target=airbnbPreValidate)
    threads.append(a)
    a.start()
    a.join()

    b = threading.Thread(target=airbnbRdfy)
    threads.append(b)
    b.start()
    b.join()

    c = threading.Thread(target=airbnbPostValidate)
    threads.append(c)
    c.start()
    c.join()

    d = threading.Thread(target=airbnb_toZip)
    threads.append(d)
    d.start()

if __name__ == '__main__':
    main()

