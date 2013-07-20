#!/usr/bin/env python

import sys
import datetime
from hashlib import md5

start = datetime.datetime.now()
lasttime = datetime.timedelta(seconds=0)

num = 0L
maxNum = (2**128) - 1

lastnum = num

logPoints = []
logpoint = 1

print "populating log points"
while logpoint < maxNum:
    print logpoint
    logPoints.append(logpoint)
    logpoint = logpoint << 1
    

def longToHexString(longval):
    return '{:032x}'.format(longval)

while num <= maxNum:
    numHexStr = longToHexString(num)
    hashHexStr = md5(numHexStr).hexdigest()
    
    if num in logPoints:
        nowtime = datetime.datetime.now() - start
        togo = maxNum - num
        pps = (num-lastnum)/ (nowtime.total_seconds()-lasttime.total_seconds())
        estSecondsRemain = togo*pps
        
        
        print("%s at %s" % (numHexStr, nowtime))
        print("%s left to go" % (togo,))
        print("processing %s per sec" % ( pps ))
        try:
            print("estimated time left: %s" % (datetime.timedelta(seconds=estSecondsRemain),))
        except OverflowError:
            print("estimated time left: %s hours" % (estSecondsRemain/3600,))
            print("estimated time left: %s days" % (estSecondsRemain/(3600*24),))
            print("estimated time left: %s years" % (estSecondsRemain/(3600*24*365),))
        
        lasttime = nowtime
        lastnum = num
        
    
    if numHexStr == hashHexStr:
        print("Identity!  '%s' hashes to itself" % (numHexStr,))
        
        
    hashOfHash = md5(hashHexStr).hexdigest()
    
    #print("attempting inverse, %s -> %s -> %s" % (numHexStr, hashHexStr, hashOfHash))
    
    if hashOfHash == numHexStr:
        print("Inverse Identity pair found! (%s, %s)" % (numHexStr, hashHexStr))
        
    num = num+1
    
    
    
    
