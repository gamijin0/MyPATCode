if(__name__=="__main__"):
    res = []
    nums = [int(x) for x in raw_input().split(' ')][1:]
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    for i in nums:
        if(i%10==0):
            a1.append(i)
        elif(i%5==1):
            a2.append(i)
        elif (i % 5 == 2):
            a3.append(i)
        elif (i % 5 == 3):
            a4.append(i)
        elif (i % 5 == 4):
            a5.append(i)

    if(len(a1)==0):
        res.append('N')
    else:
        res.append(sum([x for x in a1 if x%2==0]))
    if(len(a2)==0):
        res.append('N')
    else:
        res.append(sum([(-1)**i*x for i,x in enumerate(a2) ]))
    if(len(a3)==0):
        res.append('N')
    else:
        res.append(len(a3))
    if(len(a4)==0):
        res.append('N')
    else:
        res.append("%.1f" % (sum(a4)/float(len(a4))) )
    if(len(a5)==0):
        res.append('N')
    else:
        res.append(max(a5))

    print ' '.join([str(x) for x in res])