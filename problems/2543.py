while True:
    try:
        soma = 0
        n, id = map(int, input().split())
        for i in range(n):
            ide, j = map(int, input().split())
            if ide == id and j == 0:
                soma += 1
        print(soma)
    except EOFError:
        break
