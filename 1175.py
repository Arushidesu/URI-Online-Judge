N = []
aux = -1
for i in range(20):
    X = int(input())
    N.append(X)
for i in range(10):
    N[i], N[aux] = N[aux], N[i]
    aux -= 1
for i in range(20):
    print("N[%s] = %s" %(i, N[i]))
