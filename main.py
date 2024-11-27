import os
from allumettes import allumette
from morpions import morpion
from devinettes import devinette
from scores import lire_meilleurs

scores : int
nb:int = 0




def clear_terminal():
    os.system('cls')

def main():
    global nb
    while nb != 5 :
        joueur1 = str(input('quelle est le nom du joueur 1 : '))
        joueur2 = str(input('quelle est le nom du joueur 2 : '))
        while nb != 5 :
            print('|----------------------------------------------------------------------------|')
            print('|                                                                            |')
            print('| -saisir 1 pour jouer au devinnette ;                                       |')
            print('| -saisir 2 pour jouer au allumettes ;                                       |')
            print('| -saisir 3 pour jouer au morpion ;                                          |')
            print('| -saisir 4 pour jouer au puissance 4 ;                                      |')
            print('| -saisir 5 pour quitter ;                                                   |')
            print('|                                                                            |')
            print('|----------------------------------------------------------------------------|')
            nb = int(input('saisir quel jeux vous voulez jouer : '))
            clear_terminal()
            if nb == 1:
                lire_meilleurs(nb)
                devinette(joueur1 , joueur2)
            elif nb == 2:
                lire_meilleurs(nb)
                allumette(joueur1 , joueur2)
            elif nb == 3:
                lire_meilleurs(nb)
                morpion(joueur1 , joueur2)
            elif nb == 4:
                print('hello world')

if __name__ == "__main__" :
    main() 
    