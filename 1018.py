x = int(input())
aux = i = 0
print(x)
for i in [100, 50, 20, 10, 5, 2, 1]:
    while x >= i:
        x -= i
        aux += 1
    print("%d nota(s) de R$ %d,00" %(aux, i))
    aux = 0
