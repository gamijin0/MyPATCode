data = set()

def getChildren(num):
    res = []
    while(num!=1):
        if(num%2==0):
            num/=2
        else:
            num = (3*num+1)/2
        res.append(num)
    return set(res)

if(__name__=="__main__"):
    count = raw_input()
    target = []
    # for i in range(0,int(count)):
    s = raw_input()
    for n in s.split(' '):
        t = int(n)
        target.append(t)
        if(t not in data):
            data|=getChildren(t)

    res = [t for t in target if t not in data]
    res.sort(reverse=True)
    print ' '.join([str(t) for t in res])