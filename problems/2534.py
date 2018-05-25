while True:
    try:
        n, q = map(int, input().split())
        notas = []
        for i in range(n):
            notas.append(int(input()))
        notasordem = sorted(notas)
        notasordem.reverse()
        for i in range(q):
            print(notasordem[int(input())-1])
    except EOFError:
        break
