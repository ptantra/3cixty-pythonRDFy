import os, threading, imp
from time import strftime
from Naked.toolshed.shell import execute_js


os.chdir('/Users/patrick/3cixty/codes/3cixtyEnviro/wundergroundModule/NCE/') # @patrick CASA Mac setup
print os.getcwd()

def wunderground_NCE_retrieveData():
    success = execute_js('wunderground_pws_NCE.js')
    if success:
        print 'weather station extracted'
    else:
        print 'error: weather station not extracted'
    return

def wunderground_NCE_rdfy():
    print "* thread wunderground_NCE_rdfy"
    os.system('python wundergroundNice_rdfy.py')
    return

def wunderground_NCE_postValidate():
    print "* thread wunderground_NCE_rdfy"
    os.system('python wundergroundNice_postValidate.py')
    return

def wunderground_NCE_retrieveForecastData():
    success = execute_js('forecast_NCE.js')
    print "* thread wunderground_NCE_retrieveForecastData"
    if success:
        print 'forecast data extracted'
    else:
        print 'error: forecast data not extracted'
    return

def wunderground_NCEforecast_rdfy():
    print "* thread wunderground_NCEforecast_rdfy"
    os.system('python wundergroundNice_rdfy_realtime.py')
    return


def main():
    threads =[]

    a = threading.Thread(target = wunderground_NCE_retrieveData)
    threads.append(a)
    a.start()
    a.join()

    b = threading.Thread(target= wunderground_NCE_rdfy)
    threads.append(b)
    b.start()
    b.join()

    c = threading.Thread(target=wunderground_NCE_postValidate)
    threads.append(c)
    c.start()
    c.join()

    d = threading.Thread(target=wunderground_NCE_retrieveForecastData)
    threads.append(d)
    d.start()
    d.join()

    e = threading.Thread(target=wunderground_NCEforecast_rdfy)
    threads.append(e)
    e.start()
    e.join()


if __name__ == '__main__':
    main()