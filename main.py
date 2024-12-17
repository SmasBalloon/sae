import os
from allumettes import allumette
from morpions import morpion
from devinettes import devinette
from scores import lire_meilleur
from puissances4 import lancer_partie
from fichierregle import regledevinette, regleallumette, reglemorpion, reglepuissance4
scores : int
nb : float = 0
bot1 : bool = False
bot2 : bool = False

def nettoyer_terminal():
    os.system('cls')

def insription():
    try:
        bot = str(input('Vous voulez jouer contre un bot ou un joueur ? O/N : ')).lower()
    except ValueError:
        print("")
        bot = ''
    while bot not in ['o', 'n']:
        print("\33[0;31;40m Veuillez saisir une lettre valide. \33[0m\n")
        try:
            bot = str(input('Vous voulez jouer contre un bot ou un joueur ? O/N : ')).lower()
        except ValueError:
            print("")

    joueur1, joueur2 = '', ''
    if bot == 'o':
        try:
            combien = int(input('Voulez vous 1 bot ou 2 bots ? : '))
        except ValueError:
            print("\33[0;31;40m Veuillez saisir un nombre valide.\33[0m")
            combien = 0
        while combien not in [1, 2]:
            print("\33[0;31;40m Veuillez saisir un nombre valide. \33[0m")
            try:
                combien = int(input('Combien de bot voulez-vous mettre ? : '))
            except ValueError:
                print("")
        if combien == 1:
            print('quelle niveau de difficulté du joueur 1 ?')
            print('saisir 1 pour facile')
            print('saisir 2 pour moyen')
            print('saisir 3 pour imposible')
            try:
                bot_level = int(input())
            except ValueError:
                bot_level = 0
            while bot_level not in [1, 2, 3]:
                print("\33[0;31;40m Veuillez saisir un nombre valide. \33[0m")
                try :
                    bot_level = int(input())
                except ValueError:
                    bot_level = 0
            
            if bot_level == 1:
                joueur1 = str("botfacile@")
                bot1 : bool = True
                joueur2 = str(input('quelle est le nom du joueur 2 : '))
                bot2 : bool = False
            elif bot_level == 2:
                joueur1 = str("botmoyen@")
                bot1 : bool = True
                joueur2 = str(input('quelle est le nom du joueur 2 : '))
                bot2 : bool = False
            elif bot_level == 3:
                joueur1 = str("botimposible@")
                bot1 : bool = True
                joueur2 = str(input('quelle est le nom du joueur 2 : '))
                bot2 : bool = False

        elif combien == 2:
            print('quelle niveau de difficulté du joueur 1 ?')
            print('saisir 1 pour facile')
            print('saisir 2 pour moyen')
            print('saisir 3 pour imposible')
            try:
                bot_level1 = int(input())
            except ValueError:
                print("\33[0;31;40m Veuillez saisir un nombre valide. \033[0m\n")
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
                bot1 : bool = True
            elif bot_level1 == 2:
                joueur1 = str("botmoyen@")
                bot1 : bool = True
            else:
                joueur1 = str("botimposible@")
                bot1 : bool = True
                
            print('quelle niveau de difficulté du joueur 2 ?')
            print('saisir 1 pour facile')
            print('saisir 2 pour moyen')
            print('saisir 3 pour imposible')
            try:
                bot_level2 = int(input())
            except ValueError:
                print("\33[0;31;40m Veuillez saisir un nombre valide. \33[0m")
                bot_level2 = 0
            while bot_level2 not in [1, 2, 3]:
                try:
                    bot_level2 = int(input())
                except ValueError:
                    print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1, 2 et 3 \033[0m\n")
            if bot_level2 == 1:
                joueur2 = str("botfacile@")
                bot2 : bool = True
            elif bot_level2 == 2:
                joueur2 = str("botmoyen@")
                bot2 : bool = True
            else:
                joueur2 = str("botimposible@")
                bot2 : bool = True
    else :
        joueur1 = str(input('quelle est le nom du joueur 1 : '))
        bot2 : bool = False
        joueur2 = str(input('quelle est le nom du joueur 2 : '))
        bot2 : bool = False
    
    return joueur1, joueur2, bot1, bot2



def jeux(joueur1 : str, joueur2 : str , bot1 : bool, bot2 : bool):
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
        print("\33[0;31;40m Veuillez saisir un nombre valide.\33[0m")
        return
    nettoyer_terminal()
    if nb == 1:
        regledevinette()
        nettoyer_terminal()
        lire_meilleur('devinette')
        nettoyer_terminal()
        devinette(joueur1, joueur2, bot1, bot2)
    elif nb == 2:
        regleallumette()
        nettoyer_terminal()
        lire_meilleur('allumette')
        nettoyer_terminal()
        allumette(joueur1, joueur2, bot1, bot2)
    elif nb == 3:
        reglemorpion()
        nettoyer_terminal()
        lire_meilleur('morpion')
        nettoyer_terminal()
        morpion(joueur1, joueur2, bot1, bot2)
    elif nb == 4:
        reglepuissance4()
        nettoyer_terminal()
        lire_meilleur('puissance')
        nettoyer_terminal()
        lancer_partie(joueur1, joueur2, bot1, bot2)
    elif nb == 5:
        print("Merci d'avoir joué !")
    else:
        print("Veuillez saisir un nombre entre 1 et 5.")

def debut():
    '''
    Fonction qui permet de lancer le jeu
    '''
    joueur1 : str = ''
    joueur2 : str = ''
    global nb
    while nb != 5:
        insription()
        jeux(joueur1, joueur2 , bot1, bot2)

if __name__ == "__main__" :
    debut()