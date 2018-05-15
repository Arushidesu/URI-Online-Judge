aux1 = aux2 = aux3 = aux4 = 0
for i in range(5):
    x = int(input())
    if x % 2 == 0:
        aux1 += 1
    else:
        aux2 += 1
    if x > 0:
        aux3 += 1
    elif x < 0:
        aux4 += 1
print("%d valor(es) par(es)\n"
      "%d valor(es) impar(es)\n"
      "%d valor(es) positivo(s)\n"
      "%d valor(es) negativo(s)" %(aux1, aux2, aux3, aux4))
