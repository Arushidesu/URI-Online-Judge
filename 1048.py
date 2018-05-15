s = float(input())
pt = str("%")
if 0 <= s <= 400:
    ns = "%.2f" % float(s + s * 0.15)
    r = "%.2f" % (float(ns) - s)
    print("Novo salario: %s\n"
          "Reajuste ganho: %s\n"
          "Em percentual: 15 %s" %(ns, r, pt))
elif 400 <= s <= 800:
    ns = "%.2f" % float(s + s * 0.12)
    r = "%.2f" % (float(ns) - s)
    print("Novo salario: %s\n"
          "Reajuste ganho: %s\n"
          "Em percentual: 12 %s" %(ns, r, pt))
elif 800 <= s <= 1200:
    ns = "%.2f" % float(s + s * 0.10)
    r = "%.2f" % (float(ns) - s)
    print("Novo salario: %s\n"
          "Reajuste ganho: %s\n"
          "Em percentual: 10 %s" %(ns, r, pt))
elif 1200 <= s <= 2000:
    ns = "%.2f" % float(s + s * 0.07)
    r = "%.2f" % (float(ns) - s)
    print("Novo salario: %s\n"
          "Reajuste ganho: %s\n"
          "Em percentual: 7 %s" %(ns, r, pt))
elif s > 2000:
    ns = "%.2f" % float(s + s * 0.04)
    r = "%.2f" % (float(ns) - s)
    print("Novo salario: %s\n"
          "Reajuste ganho: %s\n"
          "Em percentual: 4 %s" %(ns, r, pt))
