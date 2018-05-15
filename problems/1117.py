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
                break
        break
