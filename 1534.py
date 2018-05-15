while True:
    try:
        N = int(input())
        X = []
        for i in range(N):
            Y = []
            for j in range(N):
                Y.append(0)
            X.append(Y)
        for i in range(N):
            for j in range(N):
                if i + j == N - 1: X[i][j] = 2
                elif i == j: X[i][j] = 1
                else: X[i][j] = 3
        for i in range(N):
            for j in range(N):
                if j == N - 1:
                    print(X[i][j])
                else:
                    print(X[i][j], end='')
    except EOFError:
        break
