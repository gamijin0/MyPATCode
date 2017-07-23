if(__name__=="__main__"):
    count = raw_input()
    count = int(count)
    nums = [2]+range(3,count+1,2)
    i = 1
    while(i<len(nums)-2):
        nums[i+1:] = [x for x  in nums[i+1:] if x%nums[i]!=0 ]
        i+=1

    res = 0
    for j in range(1,len(nums)):
        if(nums[j]-nums[j-1]==2):
            res+=1
    print res


