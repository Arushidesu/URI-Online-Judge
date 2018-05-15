while True:
    L = []
    L = input().split()
    if len(L) > 1:
        A, B, C = int(L[0]), int(L[1]), int(L[2])
    else: A = int(L[0])
    if A == 0:
        break
    cont = 1
    while True:
        if ((cont * cont) * (C / 100)) == (A*B) or ((cont * cont) * (C / 100)) < (A*B) and (((cont+1)*(cont+1)) * (C / 100) > (A*B)):
            print(cont)
            break
        cont += 1
