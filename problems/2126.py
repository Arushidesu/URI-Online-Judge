caso = 1
while True:
    try:
        a = input()
        c = input()
        print("Caso #{}:" .format(caso))
        if c.count(a) == 0:
            print("Nao existe subsequencia")
        else:
            print("Qtd.Subsequencias: {}" .format(c.count(a)))
            print("Pos: {}" .format(len(c) - c[::-1].index(a[::-1]) - len(a) + 1))
        print()
        caso += 1
    except EOFError:
        break
