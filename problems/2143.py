while True:
    t = int(input())
    if t == 0:
        break
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print(int((((n - 2) / 2) * 4) + 2))
        else:
            print(((n // 2) * 4) + 1)
