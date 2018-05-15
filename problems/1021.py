x = float(input())
aux = i = 0
print("NOTAS:")
for i in [100, 50, 20, 10, 5, 2]:
    while x >= i:
        x -= i
        aux += 1
    print("%d nota(s) de R$ %d.00" %(aux, i))
    aux = 0
x2 = int(x * 100)
print("MOEDAS:")
for i in [100, 50, 25, 10, 5, 1]:
    while x2 >= i:
        x2 -= i
        aux += 1
    x3 = "%.2f" % (i / 100)
    print("%d moeda(s) de R$ %s" %(aux, x3))
    aux = 0
