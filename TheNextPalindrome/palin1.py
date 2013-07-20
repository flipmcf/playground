#!/usr/bin/env python

import sys;


def p_split(s):
    """returns tuple of 3 strings - head, middle, tail
       head & tail always equal length
    """
    
    head = s[:len(s)/2]
    tail = s[len(s)/2:]
        
    if len(tail) > len(head):
        (middle, tail) = tail[0], tail[1:]
    else:
        (head, middle, tail) = head[:-1], head[-1:]+tail[0], tail[1:]    
        
    return head, middle, tail
        
        
def isPalendrome(s):
    if len(s) == 1:
        return True
    
    elif len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
        
    else:
        h,m,t = p_split(s)        
        if h == t[::-1] and isPalendrome(m):
            return True
        else:
            return False
        
def generatorotareneg(n=0):
    num = n
    while True:  
        if isPalendrome(str(num)):
            yield num
        num += 1
        
if __name__ == "__main__":
    tests = int(sys.stdin.readline())
    for x in range(0,tests):
        test = int(sys.stdin.readline()) 
        g = generatorotareneg(test+1)
        print g.next()
        
        


