N = int(input())
cont = 0
for i in range(N):
    X, Y = map(int, input().split())
    for i in range(Y):
        if X % 2 == 0:
            cont = X+1 + cont
            X += 2
        else:
            cont = X + cont
            X += 2
    print(cont)
    cont = 0
