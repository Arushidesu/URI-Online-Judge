cont = cont2 = 0
while True:
    N = int(input())
    aux = N
    cont2 = aux
    if N == 0:
        break
    X = []
    for i in range(N):
        Y = []
        for j in range(N):
            Y.append(0)
        X.append(Y)
    while N > 0:
        for i in range(cont, cont2):
            for j in range(cont, cont2):
                X[i][j] += 1
        cont += 1
        cont2 -= 1
        N = N - 2
    cont = 0
    for i in range(aux):
        for j in range(aux):
            if j == aux - 1:
                print("%3d" % X[i][j])
            else:
                print("%3d" % X[i][j], end=' ')
    print()
