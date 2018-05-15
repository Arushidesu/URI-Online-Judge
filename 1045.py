A, B, C = map(float, input().split())
if B > A and B > C:
    A, B = B, A
elif C > A and C > B:
    A, C = C, A
if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif (A ** 2) == (B ** 2) + (C ** 2):
    print("TRIANGULO RETANGULO")
elif (A ** 2) > (B ** 2) + (C ** 2):
    print("TRIANGULO OBTUSANGULO")
elif (A ** 2) < (B ** 2) + (C ** 2):
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
if (A == B and A != C) or (B == C and B != A) or (A == C and A != B):
    print("TRIANGULO ISOSCELES")
