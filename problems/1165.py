N = int(input())
cont = 0
for i in range(N):
    X = int(input())
    for i in range(2, X):
        if X % i == 0:
            cont = 1
    if cont == 1:
        print("%s nao eh primo" %X)
    else:
        print("%s eh primo" %X)
    cont = 0
