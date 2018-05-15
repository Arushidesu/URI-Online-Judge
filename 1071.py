X = int(input())
Y = int(input())
aux = 0
if X > Y:
    for i in range(X-1, Y, -1):
        if i % 2 != 0:
            aux = aux + i
    print(aux)
else:
    for i in range(X, Y):
        if i % 2 != 0:
            aux = aux + i
    print(aux)
