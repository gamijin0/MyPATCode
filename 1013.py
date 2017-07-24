import math
def IsPrime(num):
    for i in range(2,int(math.sqrt(num))+2):
        if(num%i==0):
            return False

    return True


if(__name__=="__main__"):
    begin,end = [int(x) for x in raw_input().split(' ')]
    primes = [2,3,5,7]
    i = 9
    while(len(primes)<1000):
        if(IsPrime(i)):
            primes.append(i)
        i+=2

    res = ""
    c = 0
    for x in primes[begin-1:end]:
        c+=1
        res += str(x)
        if(c!=10):
            res+=' '
        else:
            res+='\n'
            c=0
    print res.strip()

