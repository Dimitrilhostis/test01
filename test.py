import random
import datetime
from datetime import datetime

dt = datetime.today()
seconds_1 = dt.timestamp()

class Guesser:
  
  def __init__(self):
    self.min = 0
    self.max = 100
    self.x = random.randint(self.min, self.max)

  def valid_input(number):
    try:
        response=int(number)
        if not 0<response<100:
            print ("Le nombre doit être compris entre 0 et 100 !")
            return None
        return response
    except:
        print ("Veuillez saisir un nombre !")
        return None
  while True:
    number = valid_input(input("Saisissez une nombre entre 0 et 100 : "))
    if number:break


g = Guesser()
number = g.number
x = g.x
tries = 1
while x != number:
  if x<number:
      number = int(input("Saisissez une valeur plus petite : "))
      tries = tries+1
  elif x>number:
      number = int(input("Saisissez une valeur plus grande : "))
      tries = tries+1

print ("Bravo !")
dt = datetime.today()
seconds_2 = dt.timestamp()
time = abs(seconds_2-seconds_1)
time = datetime.utcfromtimestamp(time).strftime('%Hh %Mm et %Ss')
print ("Vous avec effectuer", tries, "tentatives, en", time, "secondes.")
