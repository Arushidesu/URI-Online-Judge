cont = 0
cont2 = 1
tudo = [cont, cont2]
for i in range(2, 46):
    soma = cont + cont2
    cont = cont2
    cont2 = soma
    tudo.append(soma)
N = int(input())
for i in range(N):
    if i == N-1:
        print(tudo[i])
    else:
        print(tudo[i], end=" ")
