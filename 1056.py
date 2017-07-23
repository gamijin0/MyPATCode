if(__name__=="__main__"):
    nums = [int(x) for x in raw_input().split(' ')][1:]
    res = 0
    for i in nums:
        res+=11*i*(len(nums)-1)
    print res
