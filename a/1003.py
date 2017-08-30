if (__name__) == "__main__":
    N,M,C1,C2 = [int(x) for  x in raw_input().split()]
    team_num = [int(x) for  x in raw_input().split()]

    roads = [[0 for i in range(N)] for i in range(N)]

    C1C2_shotest = [0, 0]  # num len

    for i in range(0,M):
        f,t,l = [int(x) for  x in raw_input().split(' ')]
        roads[f][t] = l
        roads[t][f] = l
        if(f==C1 and t==C2):
            C1C2_shotest = [1,l]



    updated = True
    while(updated):
        updated = False
        for i in range(0,N):
            for j in range(0,N):
                if(roads[i][j]!=0):
                    for jndex in range(0,N):
                        if(jndex!=i and jndex!=j and roads[i][jndex]!=0):
                            new_len = roads[i][jndex]+roads[i][j]
                            if (roads[j][jndex] == 0):
                                roads[j][jndex] = new_len
                                updated = True
                                if(j==C1 and jndex==C2):
                                    #find a new road from C1 to C2
                                    C1C2_shotest = [1,new_len]
                            elif(new_len<roads[j][jndex]):
                                roads[j][jndex] = new_len
                                updated=True
                                if(j==C1 and jndex==C2):
                                    #find a new shotest road from C1 to C2
                                    C1C2_shotest = [1, new_len]
                            elif(new_len==roads[j][jndex]):
                                if (j == C1 and jndex == C2 and updated):
                                    #find another shoutest road from C1 to C2
                                    C1C2_shotest[0]+=1

    print C1C2_shotest
    for line in roads:
        print ' '.join([str(x) for x in line])

    gather = 0
    for i in range(0,N):
        if(roads[C2][i]<=C1C2_shotest[1]):
            gather+=team_num[i]

    print C1C2_shotest[0],gather

