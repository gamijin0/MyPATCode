if(__name__=="__main__"):
    num,_ = [int(x) for x in raw_input().split()]
    score = [int(x) for x in raw_input().split()]
    true_answer = [int(x) for x in raw_input().split()]
    res = []

    for i in range(0,num):
        answer = [int(x) for x in raw_input().split()]
        s  = 0
        for i,v in enumerate(answer):
            if(v==true_answer[i]):
                s+=score[i]
        res.append(s)

    print '\n'.join([str(x) for x in res])
