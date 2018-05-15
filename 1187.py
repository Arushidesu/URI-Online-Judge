O = input()
matriz = []
soma = media = 0
cont = 1
cont2 = 11
for i in range(12):
   tmp = []
   for j in range(12):
       elemento = float(input())
       tmp.append(elemento)
   matriz.append(tmp[:])
if O == "S":
    for i in range(0, 5):
        for j in range(cont, cont2):
            soma = matriz[i][j] + soma
        cont += 1
        cont2 -= 1
    print("%.1f" % (soma))
elif O == "M":
    for i in range(0, 5):
        for j in range(cont, cont2):
            soma = matriz[i][j] + soma
        cont += 1
        cont2 -= 1
    media = "%.1f" % (soma / 30)
    print(media)
