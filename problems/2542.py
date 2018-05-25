while True:
    try:
        num_atributos = int(input())
        num_cartasm, num_cartasl = map(int, input().split())
        cartasm = []
        for i in range(num_cartasm):
            atributos = input().split()
            for j in range(num_atributos):
                atributos[j] = int(atributos[j])
            cartasm.append(atributos)
        cartasl = []
        for i in range(num_cartasl):
            atributos = input().split()
            for j in range(num_atributos):
                atributos[j] = int(atributos[j])
            cartasl.append(atributos)
        escolham, escolhal = map(int, input().split())
        atributoc = int(input())
        if cartasm[escolham-1][atributoc-1] > cartasl[escolhal-1][atributoc-1]:
            print("Marcos")
        elif cartasm[escolham-1][atributoc-1] < cartasl[escolhal-1][atributoc-1]:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError:
        break
