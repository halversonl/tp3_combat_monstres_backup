import random

niveau_vie = 20
numero_monstre = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0

def combat_monstre():

    force_monstre = random.randint(1, 5)
    global numero_monstre
    numero_monstre = numero_monstre + 1
    global numero_combat
    numero_combat = numero_combat + 1
    global nombre_victoires
    global nombre_defaites
    global niveau_vie

    print("Vous tombez face à face avec un adversaire de difficulté : {}".format(force_monstre))
    reponse = input("""
    Que voulez-vous faire ? 
    1- Combattre cet adversaire
    2- Contourner cet adversaire et aller ouvrir une autre porte
    3- Afficher les règles du jeu
    4- Quitter la partie
    Votre réponse ici: """)

    if reponse == "1":
        force_joueur = random.randint(1, 6)

        print("""Adversaire : {}
        Force de l’adversaire : {}
        Niveau de vie de l’usager : {}
        Combat numero_combat : {} vs {}""".format(numero_monstre, force_monstre, niveau_vie, numero_combat,
                                                  nombre_victoires, nombre_defaites))

        print("Lancé du dé: {}".format(force_joueur))

        if force_monstre > force_joueur:
            niveau_vie = niveau_vie - 1
            nombre_defaites = nombre_defaites +1
            statut_partie = "Gagné"

        elif force_monstre < force_joueur:
            niveau_vie = niveau_vie + 1
            nombre_victoires = nombre_victoires + 1
            statut_partie = "Perdu"


combat_monstre()