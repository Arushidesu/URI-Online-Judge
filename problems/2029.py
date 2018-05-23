while True:
    try:
        v = float(input())
        d = float(input())
        print("ALTURA = {:.2f}" .format((v / (3.14 * ((d/2) ** 2)))))
        print("AREA = {:.2f}" .format(3.14 * ((d/2) ** 2)))
    except EOFError:
        break
