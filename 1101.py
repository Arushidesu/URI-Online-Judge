aux = 0
while True:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    else:
        if M > N:
            for i in range(N, M+1):
                print(i, end=" ")
                aux = aux + i
            print("Sum=%s" %aux)
            aux = 0
        else:
            for i in range(M, N+1):
                print(i, end=" ")
                aux = aux + i
            print("Sum=%s" %aux)
            aux = 0
