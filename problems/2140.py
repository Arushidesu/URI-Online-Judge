while True:
    cont = 0
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    d = m - n
    for i in [100, 50, 20, 10, 5, 2]:
        while d >= i:
            d -= i
            cont += 1
    if cont == 2:
        print("possible")
    else:
        print("impossible")
