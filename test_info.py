
# Pierre Feuille Ciseaux


import random


def pierre_feuille_ciseaux():

    score = [0, 0]

    while (score[0] < 3) and (score[1] < 3):
        print("Pierre, feuille, ciseaux !")
        joueur1 = random.randint(1,3)
        joueur2 = random.randint(1,3)
        if joueur1 == joueur2:
            print("Egalité, on enchaîne !")
            print(score)
            continue
        elif (joueur1 == 1 and joueur2 == 2) or (joueur1 == 2 and joueur2 == 3) or (joueur1 == 3 and joueur2 == 1):
            print("Joueur1 l'emporte sur joueur2")
            score[0] = score[0] + 1
            print(score)
        elif (joueur1 == 1 and joueur2 == 3) or (joueur1 == 2 and joueur2 == 1) or (joueur1 == 3 and joueur2 == 2):
            print("Joueur2 l'emporte sur joueur1")
            score[1] = score[1] + 1
            print(score)

    if score[0] == 3:
        print("Le score est de", str(score[0]), "à", str(score[1]), "le gagnant est donc Joueur1")
    elif score[1] == 3:
        print("Le score est de", str(score[0]), "à", str(score[1]), "le gagnant est donc Joueur2")
