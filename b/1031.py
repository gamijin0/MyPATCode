if (__name__ == "__main__"):
    num = int(raw_input())
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    M = ['1' ,'0', 'X' ,'9', '8', '7', '6', '5' ,'4', '3' ,'2']
    wrong = []
    for i in range(0, num):
        s = raw_input()

        for c in s[0:17]:
            if (len(s)!=18 or c not in [str(x) for x in range(0, 10)]):
                wrong.append(s)
                continue
        if(s in wrong):
            continue
        v = sum([int(x) * weight[i] for i, x in enumerate(s[0:17])]) % 11

        if(M[v]!=s[17]):
            wrong.append(s)
            continue

    if(len(wrong)==0):
        print "All passed"
    else:
        print '\n'.join(wrong)