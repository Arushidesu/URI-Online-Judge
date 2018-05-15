N = int(input())
cont = 1
cont2 = cont3 = cont4 = 0
while cont <= N:
    cont2 = cont
    for i in range(3):
        if i == 0:
            print(cont2, end=" ")
        elif i == 1:
            cont3 = cont2 * cont2
            print(cont3, end=" ")
        else:
            cont3 = cont3 * cont2
            print(cont3)
    cont += 1
