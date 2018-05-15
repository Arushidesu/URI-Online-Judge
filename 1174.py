A = []
for i in range(100):
    X = float(input())
    A.append(X)
for i in range(100):
    if A[i] <= 10:
        print("A[%s] = %s" %(i, round(A[i], 1)))
    else:
        continue
