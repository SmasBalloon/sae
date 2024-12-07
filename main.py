import os
from allumettes import allumette
from morpions import morpion
from devinettes import devinette
from scores import lire_meilleurs
from puissances4 import lancer_partie
from fichierregle import regledevinette, regleallumette, reglemorpion, reglepuissance4
scores : int
nb : float = 0


def nettoyer_terminal():
    os.system('cls')

def debut():
    '''
    Fonction qui permet de lancer le jeu
    '''
    global nb
    while nb != 5:
        joueur1 = str(input('quelle est le nom du joueur 1 : '))
        joueur2 = str(input('quelle est le nom du joueur 2 : '))
        jeux(joueur1, joueur2)

def jeux(joueur1 : str, joueur2 : str):
    print('|----------------------------------------------------------------------------|')
    print('|                                                                            |')
    print('| -saisir 1 pour jouer au devinnette ;                                       |')
    print('| -saisir 2 pour jouer au allumettes ;                                       |')
    print('| -saisir 3 pour jouer au morpion ;                                          |')
    print('| -saisir 4 pour jouer au puissance 4 ;                                      |')
    print('| -saisir 5 pour quitter ;                                                   |')
    print('|                                                                            |')
    print('|----------------------------------------------------------------------------|')
    try:
        nb = float(input('saisir quel jeux vous voulez jouer : '))
    except ValueError:
        print("Veuillez saisir un nombre valide.")
        return
    nettoyer_terminal()
    if nb == 1:
        regledevinette()
        nettoyer_terminal()
        lire_meilleurs('devinette')
        nettoyer_terminal()
        devinette(joueur1, joueur2)
    elif nb == 2:
        regleallumette()
        nettoyer_terminal()
        lire_meilleurs('allumette')
        nettoyer_terminal()
        allumette(joueur1, joueur2)
    elif nb == 3:
        reglemorpion()
        nettoyer_terminal()
        lire_meilleurs('morpion')
        nettoyer_terminal()
        morpion(joueur1, joueur2)
    elif nb == 4:
        reglepuissance4()
        nettoyer_terminal()
        lire_meilleurs('puissance')
        nettoyer_terminal()
        lancer_partie(joueur1, joueur2)
    elif nb == 5:
        print("Merci d'avoir joué !")
    else:
        print("Veuillez saisir un nombre entre 1 et 5.")
if __name__ == "__main__" :
    debut()