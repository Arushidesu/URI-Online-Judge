aux = cont = 0
X = int(input())
Z = int(input())
while Z <= X:
    Z = int(input())
while aux < Z:
    if cont == 0:
        aux = X
    else:
        X += 1
        aux = X + aux
    cont += 1
print(cont)
