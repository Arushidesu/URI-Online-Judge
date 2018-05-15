T = int(input())
cont = 0
for i in range(T):
    PA, PB, G1, G2 = input().split()
    PA, PB, G1, G2 = int(PA), int(PB), float(G1), float(G2)
    while PA <= PB:
        cont += 1
        PA = int(PA + (PA * (G1 / 100)))
        PB = int(PB + (PB * (G2 / 100)))
        if cont > 100:
            break
    if cont > 100:
        print("Mais de 1 seculo.")
    else:
        print("%s anos." %cont)
    cont = 0
