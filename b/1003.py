def a_check(s):
    if(len(s)==0):
        return True
    if(len(s.replace('A',''))!=0):
        return False
    return True


def check(s):
    if(len([c for c in s if c not in ['P','A','T']])!=0):
        return False

    p = s.find('P')
    t = s.find('T')

    if(p==-1 or t==-1 or s.count('P')!=1 or s.count('T')!=1 ):
        return False

    head = s[:p]
    mid = s[p+1:t]
    tail = s[t+1:]

    if(a_check(head) is not True):
        return False

    if(len(mid) in (1,2)):
        if (tail[-1:-1 - len(head):-1] == head and a_check(tail[:len(tail) - len(head)])):
            return True


    # if(len(mid)==1 and head==tail):
    #     return True
    # if(len(mid)==2):
    #     if(mid[1]!='A'):
    #         return False
    #     if(tail[-1:-1-len(head):-1]==head and a_check(tail[:len(tail)-len(head)])):
    #         return True

    return False


if(__name__=="__main__"):
    count = raw_input()
    for i in range(0,int(count)):
        s = raw_input()
        if(check(s)):
            print "YES"
        else:
            print "NO"

