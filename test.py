# définir un nombre random ok
# faire trouver ce nb a qqun ok
# définir le nb d'essais ok
# définir le temps mit pour trouver le nb

import random
import datetime
from datetime import datetime

#1er time
dt = datetime.today()
seconds_1 = dt.timestamp()

#nb random
x = random.randint(0, 100)    

# nb tries
tries = 1

# valeur à faire deviner
def valid_input(inp):
    try:
        ret=int(inp)
        if not 0<ret<100:
            print ("Le nombre doit être compris entre 0 et 100 !")
            return None
        return ret
    except:
        print ("Veuillez saisir un nombre !")
        return None

while True:
    y = valid_input(input("Saisissez une valeur entre 0 et 100 : "))
    if y:break

while x != y:
    if x<y:
        y = int(input("Saisissez une valeur plus petite : "))
        tries = tries+1
    elif x>y:
        y = int(input("Saisissez une valeur plus grande : "))
        tries = tries+1


print("Bravo vous avez trouvé !")

#2e time
dt = datetime.today()
seconds_2 = dt.timestamp()

# calcul du temps
time = abs(seconds_2-seconds_1)
time = datetime.utcfromtimestamp(time).strftime('%Hh %Mm et %Ss')
print ("Vous avec effectuer", tries, "tentatives, en", time, "secondes.")

seconds_2 = dt.timestamp()

# calcul du temps
time = abs(seconds_2-seconds_1)
if time < 60:
	print ("Vous avec effectuer", tries, "tentatives, en", time, "secondes.")
elif 60 < time < 3600:
	print("Vous avec effectuer", tries, "tentatives, en", time/60, "minutes")
elif time > 3600:
	print("Vous avec effectuer", tries, "tentatives, en", time/3600, "heures")
