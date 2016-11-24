import os, random, threading
from time import strftime

def bikeRdfy():
    print "* thread bike_rdfy"
    os.system('python src/london_bikes_rdfy.py')
    return

def bikePostValid():
    print "* * thread bike_postValid"
    os.system('python src/london_bike_postValid.py')
    return

def bikeZip():
    print "* * * thread bikeZip"
    os.system('python src/london_bikes_toZip.py')
    return

def main():
    threads =[]

    a = threading.Thread(target=bikeRdfy)
    threads.append(a)
    a.start()
    a.join()

    b = threading.Thread(target=bikePostValid)
    threads.append(b)
    b.start()
    b.join()

    c = threading.Thread(target=bikeZip)
    threads.append(c)
    c.start()

if __name__ == '__main__':
    main()

