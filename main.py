import random

niveau_vie = 20


def combat_monstre():
    force_monstre = random.randint(1, 5)

    print("Vous tombez face à face avec un adversaire de difficulté : {}".format(force_monstre))
    reponse = input("""
    Que voulez-vous faire ? 
    1- Combattre cet adversaire
    2- Contourner cet adversaire et aller ouvrir une autre porte
    3- Afficher les règles du jeu
    4- Quitter la partie
    Votre réponse ici: """)

    if reponse == 1:
        force_joueur = random.randint(1, 6)

        if force_monstre > force_joueur:
            print("""
            """)


combat_monstre()