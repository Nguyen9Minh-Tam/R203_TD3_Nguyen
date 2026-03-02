import random

m = random.randint(0, 100)
reponse = -1

while reponse!=m:
    reponse = int(input("Entrez un nombre entre 0 et 100 : "))
    if reponse < m:
        print("Plus !")
    elif reponse > m:
        print("Moins !")
    else:
        print("Bravo, vous avez gagné !")