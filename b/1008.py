if(__name__=="__main__"):
    s= raw_input()
    count,offset = s.split(' ')
    count = int(count)

    offset = int(offset)
    nums = raw_input()
    nums = [int(x) for x in nums.split(' ')]

    offset %=count

    nums = (nums[:count-offset][::-1]+nums[count-offset:][::-1])[::-1]

    # nums = nums[count-offset:]+nums[:count-offset]

    print ' '.join([str(x) for x in nums])

    exit(0)

