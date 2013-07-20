#!/usr/bin/env python

import sys;
from copy import copy;

def p_split(s):
    """returns tuple head, middle, tail
       head & tail always equal length, and are lists
       middle is a str of one char, or None.
    """
    
    head = s[:len(s)/2]
    tail = s[len(s)/2:]
        
    if len(tail) > len(head):
        (middle, tail) = tail[0], tail[1:]
    else:
        middle = None    
        
    return list(head), middle, list(tail)
        
def p_join(head, middle, tail):
    """reverse of p_split"""
    
    if middle is None:
        middle = ''
        
    return ''.join(head)+middle+''.join(tail)
    
        
def nextPalindrome(s):

    (head, middle, tail) = p_split(s)

    if head[-1] <= tail[0]:
        #head or middle must increment
        if middle is not None:
            middle = int(middle)+1

            if middle > 9:
                middle = 0
                head = list(str(long(''.join(head))+1))
            middle = str(middle)
                
            if len(head) > len(tail):
                #head overflowed
                middle = ''
            
        else:
            head = list(str(long(''.join(head))+1))
        
    #now, simply copy the head to the tail
    rtail = copy(head)
    tail = rtail[::-1]
                
    return p_join(head, middle, tail)


if __name__ == "__main__":
    tests = int(sys.stdin.readline())
    for x in range(0,tests):
        test = sys.stdin.readline()
        print nextPalindrome(test)
        
        


