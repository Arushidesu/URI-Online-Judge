while True:
    try:
        h, m = map(int, input().split(':'))
        if h > 7 or (h == 7 and m >= 1):
            h += 1
            cont = 0
            while True:
                if h == 8 and m == 0:
                    break
                m -= 1
                if m == -1:
                    m = 59
                    h -= 1
                cont += 1
            print("Atraso maximo:", cont)
        else:
            print("Atraso maximo: 0")
    except EOFError:
        break
