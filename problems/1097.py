x = 7
for i in range(1, 10, 2):
    print("I=%s J=%s" %(i, x))
    print("I=%s J=%s" % (i, x-1))
    print("I=%s J=%s" % (i, x-2))
    x += 2
