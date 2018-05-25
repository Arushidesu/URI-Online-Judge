while True:
    try:
        m = []
        l, c = map(int, input().split())
        for i in range(l):
            m.append(input().split())
        for i in m:
            if '2' in i:
                l2, c2 = m.index(i), i.index('2')
            if '1' in i:
                l1, c1 = m.index(i), i.index('1')
        if l2 < l1:
            if c2 < c1:
                print((l1 - l2) + (c1 - c2))
            elif c1 < c2:
                print((l1 - l2) + (c2 - c1))
            else:
                print(l1 - l2)
        elif l2 > l1:
            if c2 < c1:
                print((l2 - l1) + (c1 - c2))
            elif c1 < c2:
                print((l2 - l1) + (c2 - c1))
            else:
                print(l2 - l1)
        else:
            if c2 < c1:
                print(c1 - c2)
            elif c1 < c2:
                print(c2 - c1)
            else:
                print(0)
    except EOFError:
        break
