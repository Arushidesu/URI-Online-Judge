while True:
    try:
        N = int(input())
        M = []
        for i in range(N):
            M2 = []
            for j in range(N):
                M2.append(0)
            M.append(M2)
        for i in range(N):
            for j in range(N):
                if i == j:
                    M[i][j] = 2
        cont = N-1
        for i in range(N):
            for j in range(cont, cont+1):
                M[i][j] = 3
            cont -= 1
        for i in range(int(N/3), (N-1) - int(N/3)+1):
            for j in range(int(N/3), (N-1) - int(N/3)+1):
                if i == j and i == int(N / 2):
                    M[i][j] = 4
                else:
                    M[i][j] = 1
        for i in range(N):
            for j in range(N):
                if j == N - 1:
                    print(M[i][j])
                else:
                    print(M[i][j], end='')
        print()
    except EOFError:
        break
