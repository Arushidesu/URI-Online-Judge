N = int(input())
aux1 = aux2 = 0
for i in range(N):
    X = int(input())
    if 10 <= X <= 20:
        aux1 += 1
    else:
        aux2 += 1
print("%d in\n"
      "%d out" %(aux1, aux2))
