cont = 0
bin = []
soma = []
for i in range(8):
    bin.append(i)
while True:
    N = input()
    if N == 'caw caw':
        print(sum(soma))
        soma = []
        cont += 1
    if cont == 3:
        break
    if N == '---':
        soma.append(bin[0])
    elif N == '--*':
        soma.append(bin[1])
    elif N == '-*-':
        soma.append(bin[2])
    elif N == '-**':
        soma.append(bin[3])
    elif N == '*--':
        soma.append(bin[4])
    elif N == '*-*':
        soma.append(bin[5])
    elif N == '**-':
        soma.append(bin[6])
    elif N == '***':
        soma.append(bin[7])
