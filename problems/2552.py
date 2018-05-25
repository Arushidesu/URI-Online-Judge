while True:
    try:
        l, c = map(int, input().split())
        m = []
        m2 = []
        for i in range(l):
            m.append(input().split())
        for i in range(l):
            somas = []
            for j in range(c):
                soma = 0
                if l > 1:
                    if m[i][j] == '0':
                        if i == 0 and j == 0:
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i+1][j] == '1':
                                soma += 1
                        elif i == 0 and (1 <= j < c-1):
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i+1][j] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif i == 0 and j == c-1:
                            if m[i+1][j] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif (1 <= i < l-1) and j == 0:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i+1][j] == '1':
                                soma += 1
                        elif (1 <= i < l-1) and (1 <= j < c-1):
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i+1][j] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif (1 <= i < l-1) and j == c-1:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i+1][j] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif i == l-1 and j == 0:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                        elif i == l-1 and (1 <= j < c-1):
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif i == l-1 and j == c-1:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        somas.append(soma)
                    else:
                        somas.append(9)
                else:
                    if m[i][j] == '0':
                        if i == 0 and j == 0:
                            if m[i][j+1] == '1':
                                soma += 1
                        elif i == 0 and (1 <= j < c-1):
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif i == 0 and j == c-1:
                            if m[i][j-1] == '1':
                                soma += 1
                        elif (1 <= i < l-1) and j == 0:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i+1][j] == '1':
                                soma += 1
                        elif (1 <= i < l-1) and (1 <= j < c-1):
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif (1 <= i < l-1) and j == c-1:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif i == l-1 and j == 0:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                        elif i == l-1 and (1 <= j < c-1):
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j+1] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        elif i == l-1 and j == c-1:
                            if m[i-1][j] == '1':
                                soma += 1
                            if m[i][j-1] == '1':
                                soma += 1
                        somas.append(soma)
                    else:
                        somas.append(9)
            m2.append(somas)
        for i in range(l):
            for j in range(c):
                if j == c-1:
                    print(m2[i][j])
                else:
                    print(m2[i][j], end='')
    except EOFError:
        break
