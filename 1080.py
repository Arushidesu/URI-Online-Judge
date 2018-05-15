aux1 = aux2 = 0
for i in range(1, 101):
    x = int(input())
    if x > aux1:
        aux1 = x
        aux2 = i
print("%d\n"
      "%d" %(aux1, aux2))
