cont = 0
while True:
    X = int(input())
    if X == 0:
        break
    for i in range(5):
        if X % 2 == 0:
            cont = X + cont
            X += 2
        else:
            cont = X+1 + cont
            X += 2
    print(cont)
    cont = 0
