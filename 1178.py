X = float(input())
N = []
for i in range(100):
    N.append(X)
    X = X/2
for i in range(100):
    print("N[%s] = %s" %(i, "%.4f"%(N[i])))
