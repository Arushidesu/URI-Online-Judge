a, b, c, d = input().split(" ")
a, b, c, d = float(a), float(b), float(c), float(d)
media = float("%.1f" % (((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10))
print("Media: %s" %media)
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5 <= media < 7:
    print("Aluno em exame.")
    x = float(input())
    print("Nota do exame: %s" %x)
    media2 = float("%.1f" % ((media + x) / 2))
    if media2 >= 5:
        print("Aluno aprovado.")
        print("Media final: %s" %media2)
    else:
        print("Aluno reprovado.")
        print("Media final: %s" %media2)
