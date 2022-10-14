import random
import time

niveau_vie = 5
numero_monstre = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
victoires_consec = 0
statut_partie = 0


def combat_monstre():

    force_monstre = random.randint(1, 5)
    global numero_monstre
    numero_monstre = numero_monstre + 1
    global numero_combat
    numero_combat = numero_combat + 1
    global nombre_victoires
    global nombre_defaites
    global niveau_vie
    global victoires_consec
    global statut_partie

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

        print("""
        Adversaire #{}
        Force de l’adversaire : {}
        Niveau de vie de l’usager avant le combat: {}
        Combat #{} : {} victoires vs {} défaites
        LANCÉ DU DÉ (FORCE DE L'UTILISATEUR): {}""".format(numero_monstre, force_monstre, niveau_vie,
        numero_combat, nombre_victoires, nombre_defaites, force_joueur))

        if force_monstre >= force_joueur:
            niveau_vie = niveau_vie - 1
            nombre_defaites = nombre_defaites + 1
            victoires_consec = 0
            statut_partie = "PERTE"

        elif force_monstre < force_joueur:
            niveau_vie = niveau_vie + 1
            nombre_victoires = nombre_victoires + 1
            victoires_consec = victoires_consec + 1
            statut_partie = "VICTOIRE"

        print("""
        {}
        Niveau de vie de l'usager après le combat: {}
        Nombre de victoires consécutives: {}
        """.format(statut_partie, niveau_vie, victoires_consec))

        if niveau_vie < 1:
            print("""
            La partie est terminée, vous avez vaincu {} monstre(s)
            et mené {} batailles.""".format(nombre_victoires, numero_combat))

        else:
            # time.sleep(5)
            combat_monstre()


combat_monstre()