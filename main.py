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

def insription():
    try:
        bot = str(input('Vous voulez jouer contre un bot ou un joueur ? O/N : ')).lower()
    except ValueError:
        print("")
        bot = ''
    while bot not in ['o', 'n']:
        print("Veuillez saisir un nombre valide.")
        try:
            bot = str(input('Vous voulez jouer contre un bot ou un joueur ? O/N : ')).lower()
        except ValueError:
            print("")

    joueur1, joueur2 = '', ''
    if bot == 'o':
        try:
            combien = int(input('Combien de bot voulez-vous mettre ? : '))
        except ValueError:
            print("Veuillez saisir un nombre valide.")
            combien = 0
        while combien not in [1, 2]:
            print("Veuillez saisir un nombre valide.")
            try:
                combien = int(input('Combien de bot voulez-vous mettre ? : '))
            except ValueError:
                print("")
        if combien == 1:
            try:
                print('quelle niveau de difficulté du joueur 1 ?')
                print('saisir 1 pour facile')
                print('saisir 2 pour moyen')
                print('saisir 3 pour imposible')
                bot_level = int(input())
            except ValueError:
                print("Veuillez saisir un nombre valide.")
                bot_level = 0
            while bot_level not in [1, 2, 3]:
                bot_level = int(input())
                
            if bot_level == 1:
                joueur1 = str("botfacile@")
                joueur2 = str(input('quelle est le nom du joueur 2 : '))
            elif bot_level == 2:
                joueur1 = str("botmoyen@")
                joueur2 = str(input('quelle est le nom du joueur 2 : '))
            else:
                joueur1 = str("botimposible@")
                joueur2 = str(input('quelle est le nom du joueur 2 : '))
        else:
            try:
                print('quelle niveau de difficulté du joueur 1 ?')
                print('saisir 1 pour facile')
                print('saisir 2 pour moyen')
                print('saisir 3 pour imposible')
                bot_level1 = int(input())
            except ValueError:
                print("Veuillez saisir un nombre valide.")
                bot_level1 = 0
            while bot_level1 not in [1, 2, 3]:
                try :
                    bot_level1 = int(input())
                except ValueError:
                    print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1, 2 et 3 \033[0m\n")
                while bot_level1 not in [1, 2, 3]:
                    print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1, 2 et 3 \033[0m\n")
                    try:
                        bot_level1 = int(input())
                    except ValueError:
                        print("")
                if bot_level1 == 1:
                    joueur1 = str("botfacile@")
                elif bot_level1 == 2:
                    joueur1 = str("botmoyen@")
                else:
                    joueur1 = str("botimposible@")
                
                try:
                    print('quelle niveau de difficulté du joueur 2 ?')
                    print('saisir 1 pour facile')
                    print('saisir 2 pour moyen')
                    print('saisir 3 pour imposible')
                    bot_level2 = int(input())
                except ValueError:
                    print("Veuillez saisir un nombre valide.")
                    bot_level2 = 0
                while bot_level2 not in [1, 2, 3]:
                    try:
                        bot_level2 = int(input())
                    except ValueError:
                        print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1, 2 et 3 \033[0m\n")
                if bot_level2 == 1:
                    joueur2 = str("botfacile@")
                elif bot_level2 == 2:
                    joueur2 = str("botmoyen@")
                else:
                    joueur2 = str("botimposible@")
    else :
        joueur1 = str(input('quelle est le nom du joueur 1 : '))
        joueur2 = str(input('quelle est le nom du joueur 2 : '))
    
    return joueur1, joueur2


def debut(joueur1:str, joueur2:str):
    '''
    Fonction qui permet de lancer le jeu
    '''
    global nb
    while nb != 5:
        insription()
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