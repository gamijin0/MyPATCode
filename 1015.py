def mycmp(a,b):
    #mycmp(a,b) --> -1(a<b),0(a==b),1(a>b)
    if(a[1]+a[2]<b[1]+b[2]):
        return -1
    elif(a[1]+a[2]>b[1]+b[2]):
        return 1
    else:
        if(a[1]<b[1]):
            return -1
        elif(a[1]>b[1]):
            return 1
        else:
            if(a[0]>b[0]):
                return -1
            else:
                return 1

if(__name__=="__main__"):
    num,L,H = [int(x) for x in raw_input().split()]
    A,B,C,D = [],[],[],[]
    count = 0
    for i in range(0,num):
        count += 1
        no,d,c = [int(x) for x in raw_input().split()]
        if(d<L or c<L):
            count-=1
            continue
        if(d>=H and c>=H):
            A.append((no,d,c))
        elif(d>=H and c>=L):
            B.append((no,d,c))
        elif(d>=c):
            C.append((no,d,c))
        else:
            D.append((no,d,c))

    for i in (A,B,C,D):
        i.sort(cmp=mycmp,reverse=True)

    print "%d" % count
    print '\n'.join(["%d %d %d" % (x) for x in A+B+C+D])


