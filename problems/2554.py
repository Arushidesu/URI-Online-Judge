while True:
    try:
        cond = False
        cond2 = True
        n, d = map(int, input().split())
        for i in range(d):
            datas = input()
            if datas.split(' ', 1)[1].split(' ').count('1') == n and cond2:
                cond = True
                cond2 = False
                data = datas.split(' ', 1)[0]
        if cond:
            print(data)
        else:
            print("Pizza antes de FdI")
    except EOFError:
        break
