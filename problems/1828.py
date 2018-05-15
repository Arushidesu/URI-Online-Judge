T = int(input())
for i in range(1, T+1):
    teste = input().split()
    if (teste[0] == 'tesoura' and teste[1] == 'papel') or (teste[0] == 'tesoura' and teste[1] == 'lagarto'):
        print("Caso #{}: Bazinga!" .format(i))
    elif (teste[0] == 'papel' and teste[1] == 'pedra') or (teste[0] == 'papel' and teste[1] == 'Spock'):
        print("Caso #{}: Bazinga!".format(i))
    elif (teste[0] == 'pedra' and teste[1] == 'lagarto') or (teste[0] == 'pedra' and teste[1] == 'tesoura'):
        print("Caso #{}: Bazinga!".format(i))
    elif (teste[0] == 'lagarto' and teste[1] == 'Spock') or (teste[0] == 'lagarto' and teste[1] == 'papel'):
        print("Caso #{}: Bazinga!".format(i))
    elif (teste[0] == 'Spock' and teste[1] == 'tesoura') or (teste[0] == 'Spock' and teste[1] == 'pedra'):
        print("Caso #{}: Bazinga!".format(i))
    elif (teste[0] == 'papel' and teste[1] == 'tesoura') or (teste[0] == 'lagarto' and teste[1] == 'tesoura'):
        print("Caso #{}: Raj trapaceou!".format(i))
    elif (teste[0] == 'pedra' and teste[1] == 'papel') or (teste[0] == 'Spock' and teste[1] == 'papel'):
        print("Caso #{}: Raj trapaceou!".format(i))
    elif (teste[0] == 'lagarto' and teste[1] == 'pedra') or (teste[0] == 'tesoura' and teste[1] == 'pedra'):
        print("Caso #{}: Raj trapaceou!".format(i))
    elif (teste[0] == 'Spock' and teste[1] == 'lagarto') or (teste[0] == 'papel' and teste[1] == 'lagarto'):
        print("Caso #{}: Raj trapaceou!".format(i))
    elif (teste[0] == 'tesoura' and teste[1] == 'Spock') or (teste[0] == 'pedra' and teste[1] == 'Spock'):
        print("Caso #{}: Raj trapaceou!".format(i))
    else:
        print("Caso #{}: De novo!".format(i))
