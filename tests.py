import random

compte = 0
m = random.randint(0, 100)
reponse = -1

while reponse!=m:
    reponse = int(input("Entrez un nombre entre 0 et 100 : "))
    if reponse < m:
        print("Plus !")
        compte += 1
        if compte%3 == 0:
            m = random.randint(0, 100)
    elif reponse > m:
        print("Moins !")
        compte += 1
        if compte%3 == 0:
            m = random.randint(0, 100)
    else:
        print("Bravo, vous avez gagné !")