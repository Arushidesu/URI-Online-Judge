contg = inter = gremio = emp = quem = 0
cond = 1
while cond == 1:
    gr1, gr2 = map(int, input().split())
    contg += 1
    if gr1 > gr2:
        inter += 1
    elif gr2 > gr1:
        gremio += 1
    else:
        emp += 1
    cond = int(input("Novo grenal (1-sim 2-nao)\n"))
if inter > gremio:
    quem = "Inter venceu mais"
elif gremio > inter:
    quem = "Gremio venceu mais"
else:
    quem = "Nao houve vencedor"
print("%s grenais\n"
      "Inter:%s\n"
      "Gremio:%s\n"
      "Empates:%s\n"
      "%s" %(contg, inter, gremio, emp, quem))
