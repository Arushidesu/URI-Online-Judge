a, b, c = map(int, input().split())
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    if a != b and b != c and c != a:
        print("Valido-Escaleno")
    elif a == b == c:
        print("Valido-Equilatero")
    else:
        print("Valido-Isoceles")
    if a > b and a > c:
        if a ** 2 == (b ** 2) + (c ** 2):
            print("Retangulo: S")
        else:
            print("Retangulo: N")
    elif b > a and b > c:
        if b ** 2 == (a ** 2) + (c ** 2):
            print("Retangulo: S")
        else:
            print("Retangulo: N")
    elif c > a and c > b:
        if c ** 2 == (a ** 2) + (b ** 2):
            print("Retangulo: S")
        else:
            print("Retangulo: N")
    else:
        print("Retangulo: N")
else:
    print("Invalido")
