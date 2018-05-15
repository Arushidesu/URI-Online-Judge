N = int(input())
cont = 0
pum = 1
while cont < N:
    for i in range(4):
        if pum % 4 == 0 and pum != 1:
            print("PUM")
        else:
            print(pum, end=" ")
        pum += 1
    cont += 1
