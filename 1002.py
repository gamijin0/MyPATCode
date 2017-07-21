
if(__name__=="__main__"):
    chi = ["ling","yi","er","san","si","wu","liu","qi","ba","jiu"]
    a = input()
    a_str = str(a)
    s = 0
    for c in a_str:
        s+=int(c)



    print ' '.join([chi[int(c)] for c in str(s) ])