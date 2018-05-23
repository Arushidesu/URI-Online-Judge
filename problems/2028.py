caso, ns = 1, ""
while True:
    try:
        n = int(input())
        for i in range(n+1):
            if i == 0:
                ns = str(i)
            else:
                ns += ((" " + str(i)) * i)
        if len(ns.split()) == 1:
            print("Caso {}: {} numero" .format(caso, len(ns.split())))
        else:
            print("Caso {}: {} numeros" .format(caso, len(ns.split())))
        print(ns)
        caso += 1
        print()
    except EOFError:
        break
