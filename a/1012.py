def findRank(grade,ID):
    for i,v in enumerate(grade):
        if(v[0]==ID):
            return i
    return -1

if(__name__=="__main__"):
    record_num,query_num  = [int(x) for x in raw_input().split(' ')]
    A = []
    C = []
    M = []
    E = []
    for i in range(record_num):
        l = raw_input().split(' ')
        ID = l[0]
        c,m,e =[int(x) for x in l[1:]]
        a = int((c+m+e)/3)
        A.append([ID,a])
        C.append([ID, c])
        M.append([ID, m])
        E.append([ID, e])

    for i in [A,C,M,E]:
        i.sort(key=lambda x:x[1],reverse=True)

    res = []
    s = ['A','C','M','E']
    for i in range(query_num):
        ID = raw_input()
        temp = [findRank(grade=g,ID=ID) for g in [A,C,M,E]]
        if(-1 in temp):
            res.append('N/A')
        else:
            bestIndex,bestRank = min(enumerate(temp),key=lambda x:x[1])
            # if(temp.count(bestRank)>1):
            #     bestIndex = temp.index(bestRank)
            res.append('%d %s' % (bestRank+1,s[bestIndex]))

    print '\n'.join(res)