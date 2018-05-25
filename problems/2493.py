while True:
    try:
        exps = []
        nomes = []
        t = int(input())
        for i in range(t):
            exp = input()
            x = exp.split(' ')[0]
            y = exp.split(' ')[1].split('=')[0]
            z = exp.split(' ')[1].split('=')[1]
            exps.append([x, y, z])
        for i in range(t):
            coisas = input()
            nome = coisas.split(' ')[0]
            ind = int(coisas.split(' ')[1])
            op = coisas.split(' ')[2]
            if op != 'I':
                if not eval(exps[ind-1][0] + op + exps[ind-1][1]) == int(exps[ind-1][2]):
                    nomes.append(nome)
            else:
                if (int(exps[ind-1][0]) + int(exps[ind-1][1]) == int(exps[ind-1][2]) or int(exps[ind-1][0]) - int(exps[ind-1][1]) == int(exps[ind-1][2]) or int(exps[ind-1][0]) * int(exps[ind-1][1]) == int(exps[ind-1][2])):
                    nomes.append(nome)
        if len(nomes) == 0:
            print("You Shall All Pass!")
        elif len(nomes) == t:
            print("None Shall Pass!")
        else:
            for i in range(len(nomes)):
                if i == len(nomes) - 1:
                    print(sorted(nomes)[i])
                else:
                    print(sorted(nomes)[i], end=" ")
    except EOFError:
        break
