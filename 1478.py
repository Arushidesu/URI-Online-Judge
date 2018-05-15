while True:
    N = int(input())
    if N == 0:
        break
    X = []
    for i in range(N):
        Y = []
        for j in range(N):
            Y.append(0)
        X.append(Y)
    for i in range(N):
        for j in range(N):
            if i == j: X[i][j] = 1
            else: X[i][j] = abs(i - j) + 1
    for i in range(N):
        for j in range(N):
            if j == N - 1:
                print("%3d" % X[i][j])
            else:
                print("%3d" % X[i][j], end=' ')
    print()
