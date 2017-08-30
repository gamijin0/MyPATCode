if(__name__=="__main__"):
    a1 = raw_input()
    a2 = raw_input()
    b1 = raw_input()
    b2 = raw_input()

    W = -1
    H = -1
    M = -1
    for i,x in enumerate(a1):
        if(a2[i]==x and x>='A' and x<='G'):
            W = i
            break

    for i, x in enumerate(a1):
        if (i>W and a2[i] == x and ((x >= 'A' and x <= 'N') or (x>='0' and x <='9'))):
            if(x >= 'A' and x <= 'N'):
                H = ord(x)-ord('A')+10
            else:
                H = ord(x)-ord('0')
            break

    for i, x in enumerate(b1):
        if (b2[i] == x and ((x >= 'A' and x <= 'Z') or (x>='a' and x <='z'))):
            M = i
            break



    w = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

    res = "%s %02.d:%02.d" % (w[ord(a1[W])-ord('A')],H,M)

    print res
    exit(0)