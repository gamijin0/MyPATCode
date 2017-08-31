def findRank(grade,ID):
    for i,v in enumerate(grade):
        if(v[0]==ID):
            return i
    return -1

if(__name__=="__main__"):
    record_num,query_num  = [int(x) for x in raw_input().split(' ')]
    records = []
    Score = [[0 for i in range(101)], [0 for i in range(101)], [0 for i in range(101)], [0 for i in range(101)]]

    res = []

    for i in range(record_num):
        l = raw_input().split(' ')
        ID = l[0]
        c,m,e =[int(x) for x in l[1:]]
        a = int((c+m+e)/3)
        records.append([ID,a,c,m,e])
        for col,grade in enumerate([a,c,m,e]):
            for i in range(grade):
                Score[col][i]+=1
    s = ["A","C","M","E"]
    names = [x[0] for x in records]
    for i in range(query_num):
        ID = raw_input()
        if(ID not in names):
            res.append('N/A')
        else:
            score = [Score[i][x] for i,x in enumerate(records[names.index(ID)][1:])]
            bestGrade = min(score)
            bestIndex = score.index(bestGrade)
            res.append('%d %s' % (bestGrade+1,s[bestIndex]))

    print '\n'.join(res)



