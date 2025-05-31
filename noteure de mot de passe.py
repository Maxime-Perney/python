import re

def tester_mot_de_passe(mot_de_passe):
    # Vérifier la longueur
    longueur_suffisante = len(mot_de_passe) >= 12

    # Vérifier la présence de lettres majuscules
    a_majuscule = bool(re.search(r'[A-Z]', mot_de_passe))

    # Vérifier la présence de lettres minuscules
    a_minuscule = bool(re.search(r'[a-z]', mot_de_passe))

    # Vérifier la présence de chiffres
    a_chiffre = bool(re.search(r'\d', mot_de_passe))

    # Vérifier la présence de caractères spéciaux
    a_special = bool(re.search(r'[!@#$[%^&*(),.?":{}|<>]', mot_de_passe))

    # Évaluation du mot de passe
    if longueur_suffisante and a_majuscule and a_minuscule and a_chiffre and a_special:
        return "Mot de passe très fort"
    elif longueur_suffisante and (a_majuscule or a_minuscule) and (a_chiffre or a_special):
        return "Mot de passe fort"
    elif longueur_suffisante and (a_majuscule or a_minuscule):
        return "Mot de passe moyen"
    elif longueur_suffisante and (a_chiffre or a_special):
        return "Mot de passe moyen"
    elif longueur_suffisante and a_majuscule:
        return "Mot de passe moyen"
    elif longueur_suffisante and a_minuscule:
        return "Mot de passe moyen"
    elif longueur_suffisante and a_chiffre:
        return "Mot de passe moyen"
    elif longueur_suffisante and a_special:
        return "Mot de passe moyen"
    elif longueur_suffisante:
        return "Mot de passe moyen"
    elif a_majuscule:
        return "Mot de passe faible"
    elif a_minuscule:
        return "Mot de passe faible"
    elif a_chiffre:
        return "Mot de passe faible"
    elif a_special:
        return "Mot de passe faible"
    else:
        return "Mot de passe faible"

# Demander à l'utilisateur d'entrer un mot de passe
mot_de_passe = input("Veuillez entrer votre mot de passe : ")
resultat = tester_mot_de_passe(mot_de_passe)
print(resultat)
