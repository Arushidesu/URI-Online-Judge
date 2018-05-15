N = int(input())
aux1 = aux2 = aux3 = auxt = pr = ps = pc = 0
per = "%"
for i in range(N):
    A, B = map(str, input().split())
    A = int(A)
    if B == "R":
        aux1 = aux1 + A
    elif B == "S":
        aux2 = aux2 + A
    elif B == "C":
        aux3 = aux3 + A
    auxt = auxt + A
pr = "%.2f" % ((aux1 / auxt) * 100)
ps = "%.2f" % ((aux2 / auxt) * 100)
pc = "%.2f" % ((aux3 / auxt) * 100)
print("Total: %s cobaias\n"
      "Total de coelhos: %s\n"
      "Total de ratos: %s\n"
      "Total de sapos: %s\n"
      "Percentual de coelhos: %s %s\n"
      "Percentual de ratos: %s %s\n"
      "Percentual de sapos: %s %s" %(auxt, aux3, aux1, aux2, pc, per, pr, per, ps, per))
