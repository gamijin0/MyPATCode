def tc(_t1, _t2):
    t1 = _t1.split(':')
    t2 = _t2.split(':')
    if (t1[0] > t2[0]):
        return 1
    elif (t1[0] < t2[0]):
        return -1
    else:
        if (t1[1] > t2[1]):
            return 1
        elif (t1[1] < t2[1]):
            return -1
        else:
            if (t1[0] > t2[0]):
                return 1
            elif (t1[0] < t2[0]):
                return -1
            else:
                return 0


if (__name__ == "__main__"):
    num = int(raw_input())
    records = []
    for i in range(num):
        t = raw_input().split(' ')
        records.append([t[0], t[1], 1])  # in
        records.append([t[0], t[2], 2])  # out
    records.sort(cmp=tc, key=lambda x: x[1])

    print ' '.join([records[0][0], records[-1][0]])