aux = 1
while aux == 1:
    while True:
        x = float(input())
        if x < 0 or x > 10:
            print("nota invalida")
        else:
            while True:
                x2 = float(input())
                if x2 < 0 or x2 > 10:
                    print("nota invalida")
                else:
                    m = "%.2f" % ((x + x2) / 2)
                    print("media = %s" %m)
                    aux = int(input("novo calculo (1-sim 2-nao)\n"))
                    while aux != 1 and aux != 2:
                        aux = int(input("novo calculo (1-sim 2-nao)\n"))
                    break
            break
