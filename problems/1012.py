A, B, C = input().split(" ")
A, B, C = float(A), float(B), float(C)
TRIANGULO = "%.3f" % ((A * C) / 2)
CIRCULO = "%.3f" % (3.14159 * (C ** 2))
TRAPEZIO = "%.3f" % ((C * (A + B) / 2))
QUADRADO = "%.3f" % (B * B)
RETANGULO = "%.3f" % (A * B)
print("TRIANGULO: %s\n"
      "CIRCULO: %s\n"
      "TRAPEZIO: %s\n"
      "QUADRADO: %s\n"
      "RETANGULO: %s" % (TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO))
