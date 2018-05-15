X = []
for i in range(10):
    X.append(int(input()))
    if X[-1] <= 0:
        X[-1] = 1
for i in range(10):
    print("X[%s] = %s" %(i, X[i]))
