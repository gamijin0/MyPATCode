
if(__name__=="__main__"):
    chi = ["ling","yi","er","san","si","wu","liu","qi","ba","jiu"]
    s = 0
    for c in raw_input():
        s+=int(c)
    print ' '.join([chi[int(c)] for c in str(s) ])
