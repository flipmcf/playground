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
        
        
def isPalindrome(s):
    if len(s) == 1:
        return True
    
    elif len(s) == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
        
    else:
        h,m,t = p_split(s)        
        if h == t[::-1] and isPalindrome(m):
            return True
        else:
            return False
        
        
        
def generatorotareneg(n=0):
    num = n
    while True:  
        if isPalindrome(str(num)):
            yield num
        num += 1
        
def bruteForceNextPalendrome(num):   
    g = generatorotareneg(num)
    return g.next()
        
        


def nextPalendrome(s):
    """note that input is type str - easier to chop it up"""
   
    (head, middle, tail) = p_split(num)
         
    if tail[::1] == head:
        if len(middle) == 1:
            if int(middle) < 9:
                middle = str(int(middle)+1)
            else:
                middle = '0'
                head = tail = str(long(head)+1)
        else:
            pass
                        
    return head+middle+tail


        
if __name__ == "__main__":
    tests = int(sys.stdin.readline())
    for x in range(0,tests):
        test = int(sys.stdin.readline()) 
        g = generatorotareneg(test+1)
        print g.next()


