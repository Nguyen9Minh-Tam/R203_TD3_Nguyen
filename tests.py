import random

m = random.randint(0, 1000)
reponse = -1

while reponse!=m:
    reponse = int(input("Entrez un nombre entre 0 et 1000 : "))
    if reponse < m:
        print("Plus !")
    elif reponse > m:
        print("Moins !")
    else:
        print("Bravo, vous avez gagné !")