x = cont = cont2 = cont3 = 0
while True:
    x = int(input())
    if x < 0:
        break
    cont = x + cont
    cont2 += 1
cont3 = "%.2f" % (cont/cont2)
print(cont3)
