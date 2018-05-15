O = input()
matriz = []
soma = media = 0
cont = 11
for i in range(12):
   tmp = []
   for j in range(12):
       elemento = float(input())
       tmp.append(elemento)
   matriz.append(tmp[:])
if O == "S":
    for i in range(11):
        for j in range(cont):
            soma = matriz[i][j] + soma
        cont -= 1
    print("%.1f" % (soma))
elif O == "M":
    for i in range(11):
        for j in range(cont):
            soma = matriz[i][j] + soma
        cont -= 1
    media = "%.1f" % (soma / 66)
    print(media)
