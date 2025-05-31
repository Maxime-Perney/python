import itertools
import string
import time

def force_brute(password):
    caracteres = string.ascii_letters + string.digits + string.punctuation  # Ensemble des caractères possibles
    essais_totaux = 0  # Compteur pour le nombre total d'essais

    for longueur in range(1, 100000000000000000000000000000):  # Limité à des mots de passe de longueur maximale 5 pour éviter les temps longs
        print(f"Test des mots de passe de longueur {longueur}...")
        combinaisons_totales = len(caracteres) ** longueur  # Nombre total de combinaisons pour cette longueur
        compteur = 0  # Compteur pour suivre la progression

        for combinaison in itertools.product(caracteres, repeat=longueur):
            tentative = ''.join(combinaison)
            essais_totaux += 1
            compteur += 1

            # Afficher la progression toutes les 10 000 tentatives
            if compteur % 100000 == 0 or compteur == combinaisons_totales:
                progression = (compteur / combinaisons_totales) * 100
                print(f"Progression : {progression:.2f}% ({compteur}/{combinaisons_totales} tentatives)")

            if tentative == password:
                return tentative, essais_totaux

    return None, essais_totaux


# Exemple d'utilisation
mot_de_passe = input("Entrez un mot de passe à tester : ")
debut = time.time()
resultat, essais = force_brute(mot_de_passe)
fin = time.time()

if resultat:
    print(f"\nMot de passe trouvé : {resultat}")
else:
    print("\nMot de passe introuvable (limite atteinte).")

print(f"Nombre total d'essais : {essais}")
print(f"Temps écoulé : {fin - debut:.20f} secondes")