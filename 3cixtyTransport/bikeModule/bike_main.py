import os, random, threading
from time import strftime

def bikeRdfy():
    print "* thread bike_rdfy"
    os.system('python SRC/bike_rdfy.py')
    return

def bikePreValidate():
    print "* thread bike_preValidate"
    os.system('python SRC/bike_preValidate.py')
    return

def bikePostValidate():
    print "* * thread bike_postValid"
    os.system('python SRC/bike_postValidate.py')
    return

def bikeZip():
    print "* * * thread bikeZip"
    os.system('python SRC/bike_toZip.py')
    return

def main():
    threads =[]

    a = threading.Thread(target=bikeRdfy)
    threads.append(a)
    a.start()
    a.join()

    b = threading.Thread(target=bikePostValidate)
    threads.append(b)
    b.start()
    b.join()

    c = threading.Thread(target=bikeZip)
    threads.append(c)
    c.start()

if __name__ == '__main__':
    main()

