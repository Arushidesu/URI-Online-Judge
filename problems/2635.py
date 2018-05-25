while True:
    try:
        palavras = []
        for i in range(int(input())):
            palavras.append(input())
        for i in range(int(input())):
            palavra = input()
            soma = 0
            for j in palavras:
                if palavra in j:
                    soma += 1
                    if soma == 1:
                        maior = len(j)
                    else:
                        if len(j) > maior:
                            maior = len(j)
            if soma == 0:
                print(-1)
            else:
                print(soma, maior)
    except EOFError:
        break
