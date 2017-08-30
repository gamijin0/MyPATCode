

if(__name__=="__main__"):
    a = input()
    count=0
    while(a!=1):
      if(a%2==0):
        a = a/2
      else:
        a = (3*a+1)/2
      count+=1
    print count