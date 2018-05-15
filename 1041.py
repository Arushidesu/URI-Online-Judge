entrada = input().split(" ")

valores = [float(valores) for valores in entrada]

x, y = valores

if x > 0 and y > 0:
    print("Q1")
if x > 0 and y == 0:
    print("Eixo X")

if x < 0 and y == 0:
    print("Eixo X")
          
if x > 0 and y < 0:
    print("Q4")
    
if x < 0 and y > 0:
    print ("Q2")

if x < 0 and y < 0:
    print ("Q3")

if x == 0 and y < 0:
    print("Eixo Y")

if x == 0 and y > 0:
    print("Eixo Y")

if x == y == 0:
    print("Origem")
