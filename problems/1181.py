L = int(input())
T = input()
matriz = []
soma = media = 0
for i in range(12):
   tmp = []
   for j in range(12):
       elemento = float(input())
       tmp.append(elemento)
   matriz.append(tmp[:])
if T == "S":
    for i in range(12):
        soma = matriz[L][i] + soma
    print("%.1f" % soma)
elif T == "M":
    for i in range(12):
        soma = matriz[L][i] + soma
    media = "%.1f" % (soma / 12)
    print(media)
