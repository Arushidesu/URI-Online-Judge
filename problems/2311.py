n = int(input())
for i in range(n):
    nome = input()
    gd = float(input())
    notas = input().split()
    for i in range(7):
        notas[i] = float(notas[i])
    notas.remove(min(notas))
    notas.remove(max(notas))
    print("{} {:.2f}" .format(nome, sum(notas) * gd))
