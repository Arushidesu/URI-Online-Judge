C = int(input())
for i in range(C):
    cont = 0
    N = int(input())
    for i in range(N):
        if i % 2 == 0 or i == 0:
            cont += 1
        else:
            cont -= 1
    print(cont)
