if(__name__=="__main__"):
    count = raw_input()
    data = []
    for i in range(0,int(count)):
        a = raw_input()
        data.append(a.split(' '))

    data.sort(key= lambda x : int(x[2]))
    print ' '.join(data[-1][0:2])
    print ' '.join(data[0][0:2])