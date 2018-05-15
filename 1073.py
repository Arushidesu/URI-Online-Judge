N = int(input())
aux1 = aux2 = 0
for i in range(1, N+1):
    if i % 2 == 0:
        X = i ** 2
        print("%d^2 = %d" %(i, X))
