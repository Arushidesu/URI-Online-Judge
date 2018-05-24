import datetime
while True:
    try:
        m, d = map(int, input().split())
        natal = datetime.date(day = 25, month = 12, year = 2016)
        dia = datetime.date(day = d, month = m, year = 2016)
        dif = natal - dia
        if dif.days == 0:
            print("E natal!")
        elif dif.days == 1:
            print("E vespera de natal!")
        elif dif.days < 0:
            print("Ja passou!")
        else:
            print("Faltam {} dias para o natal!" .format(dif.days))
    except EOFError:
        break
