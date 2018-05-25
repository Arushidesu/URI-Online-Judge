frases = {"dodo": "Os atributos dos monstros vao ser inteligencia, sabedoria...",
        "leo": "Iron Maiden's gonna get you, no matter how far!",
        "peper": "Urano perdeu algo muito precioso...",
        "empate": "Putz vei, o Leo ta demorando muito pra jogar..."}
opcoes = ["pedra", "papel", "tesoura"]
while True:
    try:
        r = input().split()
        if r.count("tesoura") == 2 and r.count("pedra") == 1:
            if r[0] == "pedra":
                print(frases["dodo"])
            elif r[1] == "pedra":
                print(frases["leo"])
            else:
                print(frases["peper"])
        elif r.count("pedra") == 2 and r.count("papel") == 1:
            if r[0] == "papel":
                print(frases["dodo"])
            elif r[1] == "papel":
                print(frases["leo"])
            else:
                print(frases["peper"])
        elif r.count("papel") == 2 and r.count("tesoura") == 1:
            if r[0] == "tesoura":
                print(frases["dodo"])
            elif r[1] == "tesoura":
                print(frases["leo"])
            else:
                print(frases["peper"])
        else:
            print(frases["empate"])

    except EOFError:
        break
