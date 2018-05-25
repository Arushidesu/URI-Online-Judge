while True:
    try:
        rumado = {}
        n = int(input())
        for i in range(n):
            carne, val = input().split()
            rumado[int(val)] = carne
        for i in range(n):
            if i == n-1:
                print(rumado[sorted(rumado)[i]])
            else:
                print(rumado[sorted(rumado)[i]], end=' ')
    except EOFError:
        break
