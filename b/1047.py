if (__name__ == "__main__"):
    num = int(raw_input())
    res = dict()
    for i in range(0, num):
        s = raw_input().split()
        t, p= [int(x) for x in s[0].split('-')]
        score = int(s[1])
        if (t not in res):
            res[t] = score
        else:
            res[t] += score
    print ' '.join([str(x) for x in max(res.iteritems(),key = lambda x:x[1])])

