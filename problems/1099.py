N = int(input())
aux1 = aux2 = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X > Y:
        for i2 in range(X-1, Y, -1):
            if i2 % 2 != 0:
                aux1 = aux1 + i2
        print(aux1)
        aux1 = 0
    else:
        for i2 in range(X+1, Y):
            if i2 % 2 != 0:
                aux2 = aux2 + i2
        print(aux2)
        aux2 = 0
