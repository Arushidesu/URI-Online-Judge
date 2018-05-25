while True:
    try:
        num = den = 0
        d = int(input())
        for i in range(d):
            n, c = map(int, input().split())
            num += n * c
            den += c * 100
        print("{:.4f}" .format(num / den))
    except EOFError:
        break
