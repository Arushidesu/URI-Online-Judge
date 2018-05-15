for i in range(0, 22, 2):
    i = float("%.1f" % (i / 10))
    if i == 0 or i == 1 or i == 2:
        i = int(i)
    j1 = i + 1
    j2 = i + 2
    j3 = i + 3
    print("I=%s J=%s" %(i, j1))
    print("I=%s J=%s" %(i, j2))
    print("I=%s J=%s" %(i, j3))
