if (__name__ == "__main__"):
    count = raw_input()
    num = [int(x) for x in raw_input().split(' ')]
    tempsum = 0
    f=0
    l=0
    maxf = maxl = maxsum = num[0]
    for i in num:
        if (tempsum == 0):
            f = i
        if (i >= 0):
            tempsum += i
            if (tempsum > maxsum):
                l = i
                maxsum = tempsum
                maxf = f
                maxl = l
            continue
        tempsum += i
        if (tempsum < 0):
            tempsum = 0
    if(maxsum>=0):
        print maxsum, maxf, maxl
    else:
        print 0,num[0],num[-1]