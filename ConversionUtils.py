'''
Created on 2013-04-20
A Simple module to go from RA Time/degrees to Radians and from Dec/degrees Time to Radians
@author: jono
'''
import re
import math
from decimal import Decimal

'''
Get the radians for RA based on a string. 
We can accept 
00:00:00.0+
00h00m00.00+s
0.0+d
'''
def parseRAToRadians(raString):
    aMatch = re.match("^([0-9]?[0-9])h([0-9]?[0-9])m([0-9]?[0-9])s$", raString, re.IGNORECASE)
    if aMatch:
#        print "MATCH " + aMatch.group(1) + " hours " + aMatch.group(2) + " min " + aMatch.group(3) + " sec "
        return getRadiansByHHMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))
    
    aMatch = None
    aMatch = re.match("^([0-9]?[0-9])h([0-9]?[0-9])m([0-9]?[0-9]\\.[0-9]+)s$", raString, re.IGNORECASE)
    if aMatch: 
 #       print "MATCH " + aMatch.group(1) + " hours " + aMatch.group(2) + " min " + aMatch.group(3) + " sec " 
        return getRadiansByHHMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))

    
    aMatch = None
    aMatch = re.match("^([0-9]?[0-9]):([0-9]?[0-9]):([0-9]?[0-9])(.[0-9]+)$", raString, re.IGNORECASE)
    if aMatch: 
  #      print "MATCH " + aMatch.group(1) + ":" + aMatch.group(2) + ":" + aMatch.group(3) 
        return getRadiansByHHMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))

    aMatch = re.match("^([0-9]?[0-9]):([0-9]?[0-9]):([0-9]?[0-9])$", raString, re.IGNORECASE)
    if aMatch: 
   #     print "MATCH " + aMatch.group(1) + ":" + aMatch.group(2) + ":" + aMatch.group(3) 
        return getRadiansByHHMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))
    
    aMatch = None
    aMatch = re.match("^([0-9]+)d$", raString, re.IGNORECASE)
    if aMatch:
    #    print "MATCH degrees = " + aMatch.group(1) 
        return getRadiansByDegrees(Decimal(aMatch.group(1)))

    
    aMatch = None
    aMatch = re.match("^([0-9]+\\.[0-9]+)d$", raString, re.IGNORECASE)
    if aMatch:
     #   print "MATCH degrees = " + aMatch.group(1) 
        return getRadiansByDegrees(Decimal(aMatch.group(1)))
        
    return None

def getRadiansByDegrees(degrees): # return Fibonacci series up to n
    if type(degrees) != type(Decimal(0)):
        raise Exception("degrees has to be a decimal")
    return math.radians(degrees)

def getRadiansByHHMMSS(hours, minutes, seconds):
    if isinstance(hours, Decimal) != True:
        raise Exception("hours has to be a decimal")

    if isinstance(minutes, Decimal) != True:
        raise Exception("minutes has to be a decimal")

    if isinstance(seconds, Decimal) != True:
        raise Exception("seconds has to be a decimal")
                
    degreeHours = hours * 15
    degreesMin = (minutes/60) * 15
    degreesSec = (seconds/3600) * 15
    degrees = degreeHours + degreesMin + degreesSec
    return math.radians(degrees)

'''
Get the radians for Dec based on a string. 
We can accept 
00:00:00.0+
00h00m00.00+s
0.0+d
'''

def parseDecToRadians(raString):
    aMatch = re.match("^([1-3]?[0-9]?[0-9])d([0-9]?[0-9])m([0-9]?[0-9])s$", raString, re.IGNORECASE)
    if aMatch:
#        print "MATCH " + aMatch.group(1) + " hours " + aMatch.group(2) + " min " + aMatch.group(3) + " sec "
        return getRadiansByDegMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))
    
    aMatch = None
    aMatch = re.match("^([1-3]?[0-9]?[0-9])d([0-9]?[0-9])m([0-9]?[0-9]\\.[0-9]+)s$", raString, re.IGNORECASE)
    if aMatch: 
 #       print "MATCH " + aMatch.group(1) + " hours " + aMatch.group(2) + " min " + aMatch.group(3) + " sec " 
        return getRadiansByDegMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))

    
    aMatch = None
    aMatch = re.match("^([1-3]?[0-9]?[0-9]):([0-9]?[0-9]):([0-9]?[0-9])(.[0-9]+)$", raString, re.IGNORECASE)
    if aMatch: 
  #      print "MATCH " + aMatch.group(1) + ":" + aMatch.group(2) + ":" + aMatch.group(3) 
        return getRadiansByDegMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))

    aMatch = re.match("^([1-3]?[0-9]?[0-9]):([0-9]?[0-9]):([0-9]?[0-9])$", raString, re.IGNORECASE)
    if aMatch: 
   #     print "MATCH " + aMatch.group(1) + ":" + aMatch.group(2) + ":" + aMatch.group(3) 
        return getRadiansByDegMMSS(Decimal(aMatch.group(1)), Decimal(aMatch.group(2)), Decimal(aMatch.group(3)))
    
    aMatch = None
    aMatch = re.match("^([0-9]+)d$", raString, re.IGNORECASE)
    if aMatch:
    #    print "MATCH degrees = " + aMatch.group(1) 
        return getRadiansByDegrees(Decimal(aMatch.group(1)))

    
    aMatch = None
    aMatch = re.match("^([0-9]+\\.[0-9]+)d$", raString, re.IGNORECASE)
    if aMatch:
     #   print "MATCH degrees = " + aMatch.group(1) 
        return getRadiansByDegrees(Decimal(aMatch.group(1)))

    return None

def getRadiansByDegMMSS(degrees, minutes, seconds):
    if isinstance(degrees, Decimal) != True:
        raise Exception("hours has to be a decimal")

    if isinstance(minutes, Decimal) != True:
        raise Exception("minutes has to be a decimal")

    if isinstance(seconds, Decimal) != True:
        raise Exception("seconds has to be a decimal")
                
    degreesMin = (minutes/60) * 15
    degreesSec = (seconds/3600) * 15
    degrees = degrees + degreesMin + degreesSec
    return math.radians(degrees)


    