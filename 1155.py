for i in range(1, 101):
    if i == 1:
        S = i
    else:
        S = 1/i + S
print("%.2f" % S)
