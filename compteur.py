import random

compteur = 0
nombre = random.randint(0, 1000)

while compteur !=nombre:
    valide = int(input(f"Comptons jusqu'au nombre inconnu ! Entrez le nombre après {compteur} : "))
    for _ in range(50):
        print("")
    compteur += 1
    if valide != compteur:
        print("Recommencez ! Compteur remis à 0.")
        compteur = 0

print("Bravo! Vous avez fini de compter")