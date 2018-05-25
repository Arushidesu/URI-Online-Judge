n = int(input())
totala = totalb = totalc = sucessox = sucessoy = sucessoz = 0
for i in range(n):
    nome = input()
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())
    totala += a
    totalb += b
    totalc += c
    sucessox += x
    sucessoy += y
    sucessoz += z
print("Pontos de Saque: {:.2f} %." .format((sucessox / totala) * 100))
print("Pontos de Bloqueio: {:.2f} %." .format((sucessoy / totalb) * 100))
print("Pontos de Ataque: {:.2f} %." .format((sucessoz / totalc) * 100))
