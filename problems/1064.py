aux1 = aux2 = aux3 = 0
for i in range(6):
    x = float(input())
    if x > 0:
        aux1 += 1
        aux2 = aux2 + x
aux3 = "%.1f" % (aux2 / aux1)
print("%d valores positivos" %aux1)
print(aux3)
