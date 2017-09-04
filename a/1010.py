
s = [str(x) for x in range(10)]+[chr(x) for x in range(97,123)]


def v(ch):
    return s.index(ch)

def ToDec(num_str,radix):
    res = 0
    for i,c in enumerate(num_str[::-1]):
        if(v(c)>=radix):
            return -1
        res+=radix**i*v(c)
    return res

def recFindRadix(a,b,front,rear):
    mid = (front+rear)/2
    mid_Dec = ToDec(b,mid)
    if(mid_Dec==a):
        print mid
        return None
    if(front==rear or front==mid or mid==rear):
        print "Impossible"
        return None
    if(mid_Dec<a):
        recFindRadix(a,b,mid,rear)
    else:
        recFindRadix(a,b,front,mid)


if(__name__=="__main__"):
    a,b,flag,radix = [x for x in raw_input().split(' ')]
    flag = int(flag)
    radix = int(radix)
    if(flag==2):
        b,a=a,b
    else:
        pass
    a = ToDec(a,radix)
    
    if(len(b)==1):
        f = False
        r = 0
        for r in range(1,37):
            r += 1
            if (ToDec(b,r) == a):
                print r
                f = True
                break
        if (not f):
            print "Impossible"
    else:
        f = r = 1
        while(True):
            if (ToDec(b, r)==a):
                print r
                break
            if(ToDec(b,r)<a):
                f = r
                r = r*2
            else:
                recFindRadix(a,b,f,r)
                break








