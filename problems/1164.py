N = int(input())
cont = 0
for i in range(N):
    X = int(input())
    for i in range(1, X):
        if X % i == 0:
            cont = cont + i
    if cont == X:
        print("%s eh perfeito" %X)
    else:
        print("%s nao eh perfeito" %X)
    cont = 0
