O = input()
matriz = []
soma = media = 0
cont = 11
cont2 = 0
for i in range(12):
   tmp = []
   for j in range(12):
       elemento = float(input())
       tmp.append(elemento)
   matriz.append(tmp[:])
if O == "S":
    for i in range(1, 11):
        for j in range(cont, 12):
            soma = matriz[i][j] + soma
        if cont2 == 1:
            cont += 1
        elif cont == 7:
            cont2 += 1
        else:
            cont -= 1
    print("%.1f" % (soma))
elif O == "M":
    for i in range(1, 11):
        for j in range(cont, 12):
            soma = matriz[i][j] + soma
        if cont2 == 1:
            cont += 1
        elif cont == 7:
            cont2 += 1
        else:
            cont -= 1
    media = "%.1f" % (soma / 30)
    print(media)
