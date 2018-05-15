V = int(input())
X = [V]
for i in range(1, 10):
    V = V * 2
    X.append(V)
for i in range(10):
    print("N[%s] = %s" %(i, X[i]))
