compteur = 0

while compteur !=1000:
    valide = int(input(f"Comptons jusqu'à 1000 ! Entrez le nombre après {compteur} : "))
    for _ in range(1000):
        print("")
    compteur += 1
    if valide != compteur:
        print("Recommencez ! Compteur remis à 0 !")
        compteur = 0