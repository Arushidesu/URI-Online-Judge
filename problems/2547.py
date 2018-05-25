while True:
    try:
        n, min, max = map(int, input().split())
        soma = 0
        for i in range(n):
            if min <= int(input()) <= max:
                soma += 1
        print(soma)
    except EOFError:
        break
