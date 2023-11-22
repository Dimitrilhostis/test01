# Creer un mdp
'''
base_de_donnees = []
mdp = input("Mot de passe de 8 caractères : ")
while len(mdp) < 8:
    if len(mdp) < 8:
        mdp = input("Mot de passe de 8 caractères : ")
    else:
        break
base_de_donnees.append(mdp)

print(mdp, base_de_donnees)


# Accès au compte

def integer(phrase):
    a = False
    x = input(phrase)
    while a == False:
        try:
            x = int(x)
            a = True
        except:
            x = input(phrase)
            a = False
    return x

liste_utilisateurs = [1, 2, 3, 4, 5]
liste_mots_de_passe = ["azertyui", "azertyui", "azertyui", "azertyui", "azertyui"]
lenght_liste = len(liste_utilisateurs)
false = False

# Age

age = integer("Quel est votre âge ? ")

if age >= 18:
    a = ("vous avez l'âge recquis ! ")
else:
    a = ("vous n'avez pas l'âge recquis...")
    print("Vous avez", str(age), "ans", a)
    exit()

print("Vous avez", str(age), "ans", a)

# Numéro d'identifiant

num = integer("Quel est votre numéro d'utilisateur ? ")

for i in range (0, lenght_liste):
    if num == i:
        false = True
    else:
        continue
if false == False:
    print("Vous n'êtes pas dans la liste...")
    exit()
else:
    print("Vous êtes bien dans la liste ! ")

# Mot de passe

mdp = input("Saisissez votre mot de passe : ")

for i in range (0, 3):
    if mdp == liste_mots_de_passe[num]:
        false = True
    else:
        mdp = input(f"Il vous reste {3-i} essais, saisissez votre mot de passe : ")
        false = False

if false == False:
    print("T'es baisé, désolé :)")
    exit()
else:
    print("Vous avez accès au site, enjoy :)")


nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [nombres[i] for i in range (len(nombres)) if nombres[i]%2 == 0]
print(nombres_pairs)

nombres1 = range(-10, 10)
nombres_positifs = [ i for i in nombres1 if i >= 0]
print(nombres_positifs)

nombres2 = range(5)
nombres_doubles = [i*2 for i in nombres2]
print(nombres_doubles)

nombres3 = range(10)
nombres_inverses = [i if i%2 == 0 else -i for i in nombres3]
print(nombres_inverses)

for i in range (1, 11):
    print("Utilisateur", i)

mot = input("Ecrivez un mot : ")
for i in range (len(mot)):
    print(mot[len(mot)-i-1])

'''

# Projet liste de courses

# Fonctions
def between2numbers(x):
    false = False
    while false == False:
        try:
            0 <= int(x) <= 5
            false = True
            return x
        except:
            x = input("Votre choix : ")

def quefairede(x):
    while x != 5:
        if x == 1:
            a = input("Que voulez-vous rajouter à votre liste ? ")
            liste.append(a)
            continue
        elif x == 2:
            b = input("Que voulez-vous retirer de votre liste ? ")
            liste.remove(b)
            continue
        elif x == 3:
            print(liste)
            continue
        elif x == 4:
            liste.clear()
            continue
        elif x == 5:
            print("Bonnes courses, voici votre liste :")
            for i in range (len(liste)):
                print(liste(i))

# Code
liste = []
print("Choisissez parmi les 5 options suivantes :\n1) Ajouter un élément à la liste \n2) Retirer un élément de la liste \n3) Afficher la liste\n4) Vider la liste \n5) Valider la liste")
choix = between2numbers(input("Votre choix : "))
quefairede(choix)