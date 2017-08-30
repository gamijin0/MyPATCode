
if(__name__=="__main__"):
    count = raw_input()
    for i in range(0,int(count)):
        a,b,c = [int(x)/2.0 for x in raw_input().split(' ')]
        print "Case #%d: %s" % (i+1,str(a+b>c).lower())