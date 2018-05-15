par, impar = [], []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        if len(par) == 5:
            for i in range(5):
                print("par[%s] = %s" %(i, par[i]))
            par = []
            par.append(n)
        else:
            par.append(n)
    else:
        if len(impar) == 5:
            for i in range(5):
                print("impar[%s] = %s" %(i, impar[i]))
            impar = []
            impar.append(n)
        else:
            impar.append(n)
if len(impar) > 0:
    for i in range(len(impar)):
        print("impar[%s] = %s" % (i, impar[i]))
if len(par) > 0:
    for i in range(len(par)):
        print("par[%s] = %s" % (i, par[i]))
