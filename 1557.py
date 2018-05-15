while True:
    N = int(input())
    if N == 0:
        break
    cont = 1
    cont2 = 1
    M = []
    for i in range(N):
        M2 = []
        for j in range(N):
            M2.append(cont)
            cont = cont * 2
        cont = int((cont / cont) + cont2)
        cont2 = (cont2 * 2) + 1
        M.append(M2)
    dig = str(M[N-1][N-1])
    digcont = len(dig)
    for i in range(N):
        for j in range(N):
            test = str(M[i][j])
            ajuste = test.rjust(digcont, ' ')
            if j == N - 1:
                print(ajuste)
            else:
                print(ajuste, end=" ")
    print()
