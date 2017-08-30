
if(__name__=="__main__"):
    try:
        s= [int(x) for x in raw_input().split(' ')]
        a = s[::2]
        x = s[1::2]

        res = []
        for i,v in enumerate(x):
            if(v>0):
                    res.append(v*a[i])
                    res.append(v-1)
        if(len(res)==0):
            print '0 0'
        else:
            print ' '.join([str(x) for x in res])
    except:
        pass

    exit(0)
