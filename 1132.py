X = int(input())
Y = int(input())
cont = 0
if X > Y:
    for i in range(Y, X+1):
        if i % 13 != 0:
            cont += i
else:
    for i in range(X, Y+1):
        if i % 13 != 0:
            cont += i
print(cont)
