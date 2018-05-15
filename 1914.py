QT = int(input())
for i in range(QT):
    T = input().split()
    N, M = map(int, input().split())
    if (N + M) % 2 == 0:
        if T[1] == 'PAR':
            print(T[0])
        else:
            print(T[2])
    else:
        if T[1] == 'IMPAR':
            print(T[0])
        else:
            print(T[2])
