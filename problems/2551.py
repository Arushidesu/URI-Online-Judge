while True:
    try:
        for i in range(int(input())):
            t, d = map(int, input().split())
            v = d/t
            if i == 0:
                print(1)
                maior = v
            else:
                if v > maior:
                    print(i+1)
                    maior = v
    except EOFError:
        break
