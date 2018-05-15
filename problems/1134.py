cond = al = gas = die = 0
while cond != 4:
    pref = int(input())
    if pref == 1:
        al += 1
    elif pref == 2:
        gas += 1
    elif pref == 3:
        die += 1
    elif pref == 4:
        cond = 4
print("MUITO OBRIGADO\n"
      "Alcool: %s\n"
      "Gasolina: %s\n"
      "Diesel: %s" %(al, gas, die))
