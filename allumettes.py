from jouer import joue
import random
import time
from scores import mise_a_jour_score
allumettes: int = 0
soustraction: int = 0
joueur: int = 0
jouer: int = 1
score1: int = 0
score2: int = 0


def allumette(joueur1: str, joueur2: str):
    '''
    Simule un jeu d'allumettes entre deux joueurs.
    Le jeu commence avec 20 allumettes. Les joueurs retirent à tour de rôle 1, 2 ou 3 allumettes.
    Le joueur qui retire la dernière allumette perd la partie.
    Args:
        joueur1 (str): Le nom du premier joueur.
        joueur2 (str): Le nom du deuxième joueur.
    Variables globales:
        jouer (int): Indicateur pour continuer ou arrêter le jeu.
        score1 (int): Score du joueur 1.
        score2 (int): Score du joueur 2.
        joueur (int): Indicateur du joueur actuel (1 ou 2).
    Le jeu continue tant que `jouer` est égal à 1. Les scores sont mis à jour et sauvegardés
    à la fin de chaque partie.
    '''

    global jouer, score1, score2, joueur
    while jouer != 2:
        print('quelle joueur commence par jouer ?')
        print('saisir 1 pour que le joueur 1 commence par jouer')
        print('saisir 2 pour que le joueur 2 commence par jouer')
        try:
            joueur = int(input().strip())
        except ValueError:
            joueur = 0
        print()
        while joueur not in [1, 2]:
            print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 2 \033[0m\n")
            print('quelle joueur commence par jouer ?')
            print('saisir 1 pour que le joueur 1 commence par jouer')
            print('saisir 2 pour que le joueur 2 commence par jouer')
            try:
                joueur = int(input().strip().lower())
            except ValueError:
                joueur = 0
            print()
        allumettes = 20
        print('la possition de depart')
        print()
        print('|' * allumettes)
        print()

        while allumettes > 0:
            if joueur % 2 == 1:
                print(f"{joueur1} à toi de jouer")
            else:
                print(f"{joueur2} à toi de jouer")

            try:
                soustraction = int(input("combien d'allumette veux tu enlever : ").strip())
            except ValueError:
                soustraction = 0

            while soustraction not in [1, 2, 3]:
                print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 3 \033[0m\n")
                "\033[0;31;40mO\033[0m"
                try:
                    soustraction = int(input("combien d'allumette veux tu enlever : ").strip().lower())
                except ValueError:
                    soustraction = 0
            
            if 0 < soustraction < 4:
                allumettes = allumettes - soustraction
            else:
                print('error')

            if allumettes > 0:
                print()
                print('il reste:')
                print('|' * allumettes)
                print()
            joueur = joueur + 1

            if allumettes <= 0:
                if joueur % 2 == 1:
                    joueur = 1
                else:
                    joueur = 2
                print()
                print(f"\033[0;32;40m player {joueur} win \033[0m\n")
                print()

                if joueur == 1:
                    score1 = score1 + 20
                else:
                    score2 = score2 + 20

                print(f"joueur 1 à {score1} points")
                print(f"joueur 2 a {score2} points")
                try:
                    jouer = int(joue())
                except ValueError:
                    jouer = 1
                while jouer not in [1, 2]:
                    print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 2 \033[0m\n")
                    jouer = int(joue())

                nom : str = "allumettes"
                if jouer == 2:
                    mise_a_jour_score(joueur1, score1, nom)
                    mise_a_jour_score(joueur2, score2, nom)
                    from main import jeux
                    jeux(joueur1, joueur2)

def botfacile():
    '''
    Simule un jeu d'allumettes entre un joueur et un bot.
    Le bot retire aléatoirement entre 1 et 3 allumettes.
    '''
    time.sleep(1)
    choix = random.randint(1, 3)
    return choix

def botmoyen(allumettes: int):
    '''
    Simule un jeu d'allumettes entre un joueur et un bot.
    Le bot retire aléatoirement entre 1 et 3 allumettes.'''

def botimposible(allumettes: int):
    '''
    Simule un jeu d'allumettes entre un joueur et un bot.
    Le bot retire aléatoirement entre 1 et 3 allumettes.'''
    

if __name__ == '__main__':
    allumette("joueur1", "joueur2")