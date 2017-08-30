if(__name__=="__main__"):
  num = raw_input()
  num = int(num)
  res = (num/100)*"B"+(num%100/10)*"S"+''.join([str(i) for i in range(1,num%10+1)])
  print res