pot = 2
for i in range(1, 40, 2):
    if i == 1:
        S = i
    else:
        S = (i / pot) + S
        pot = pot * 2
print("%.2f" % S)
