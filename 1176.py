cont1, cont2 = 0, 1
fibo = [cont1, cont2]
for i in range(2, 61):
    soma = cont1 + cont2
    cont1 = cont2
    cont2 = soma
    fibo.append(soma)
T = int(input())
for i in range(T):
    N = int(input())
    for i2 in range(61):
        if i2 == N:
            print("Fib(%s) = %s" %(i2, fibo[i2]))
