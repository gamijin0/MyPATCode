if(__name__=="__main__"):
    s = raw_input()
    s = [x for x in s if x in "PATest"]
    res = ''
    while(len([c for c in  s if c!=' '])>0):
        temp = [x for x in [''.join(s).find(c) for c in "PATest"]]
        for i in temp:
            if(i!=-1):
                res+=s[i]
                s[i]=' '
    print res
