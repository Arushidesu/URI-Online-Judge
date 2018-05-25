alimentos = {"suco de laranja": 120, "morango fresco": 85, "mamao": 85,
            "goiaba vermelha": 70, "manga": 56, "laranja": 50, "brocolis": 34}
while True:
    soma = 0
    t = int(input())
    if t == 0:
        break
    for i in range(t):
        ref = input().split(' ', 1)
        soma += int(ref[0]) * alimentos[ref[1]]
    if soma > 130:
        print("Menos {} mg" .format(soma - 130))
    elif soma < 110:
        print("Mais {} mg" .format(110 - soma))
    else:
        print("{} mg" .format(soma))
