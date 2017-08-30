if (__name__ == "__main__"):
    count = int(raw_input())
    a, b = 0, 0
    for i in range(0, count):
        a1, a2, b1, b2 = [int(x) for x in raw_input().split()]
        if (a2 == (a1 + b1) and b2 != a2):
            b += 1
        elif (b2 == (a1 + b1) and b2 != a2):
            a += 1

    print ' '.join((str(a), str(b)))
    exit(0)