from jouer import joue
import random
import time
from demandebot import diffbot
from scores import mise_a_jour_score

win: int
symbole: str
joueur: int
position: str
jouer: int
debut_temp: float
fin_temp: float
score: int
possible = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
retirer = []
posibilité = {
    'a1': [1, 1],
    'a2': [1, 3],
    'a3': [1, 5],
    'b1': [3, 1],
    'b2': [3, 3],
    'b3': [3, 5],
    'c1': [5, 1],
    'c2': [5, 3],
    'c3': [5, 5]
}

def check_winner(sym: str, tableau_morpion: list[list[str]]) -> bool:
    return (
        (tableau_morpion[1][1] == sym and tableau_morpion[1][3] == sym and tableau_morpion[1][5] == sym) or
        (tableau_morpion[3][1] == sym and tableau_morpion[3][3] == sym and tableau_morpion[3][5] == sym) or
        (tableau_morpion[5][1] == sym and tableau_morpion[5][3] == sym and tableau_morpion[5][5] == sym) or
        (tableau_morpion[1][1] == sym and tableau_morpion[3][1] == sym and tableau_morpion[5][1] == sym) or
        (tableau_morpion[1][3] == sym and tableau_morpion[3][3] == sym and tableau_morpion[5][3] == sym) or
        (tableau_morpion[1][5] == sym and tableau_morpion[3][5] == sym and tableau_morpion[5][5] == sym) or
        (tableau_morpion[1][1] == sym and tableau_morpion[3][3] == sym and tableau_morpion[5][5] == sym) or
        (tableau_morpion[1][5] == sym and tableau_morpion[3][3] == sym and tableau_morpion[5][1] == sym)
    )

def morpion(joueur1: str, joueur2: str, bot1: bool, bot2: bool):
    global jouer, fin_temp, debut_temp, win, joueur, symbole, position, temp, score, possible, posibilité, retirer
    diffbot(joueur1, joueur2, bot1, bot2)
    jouer = 1
    while jouer == 1:
        print('quelle joueur commence par jouer ?')
        print('saisir 1 pour que le joueur 1 commence par jouer')
        print('saisir 2 pour que le joueur 2 commence par jouer')
        try:
            joueur = int(input().strip().lower())
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

        win = 0
        tableau_morpion = [
            ['  1', ' ', '2', ' ', '3 '],  # numligne
            ['A', ' ', '|', ' ', '|', ' '],  # 1.1 1.3 1.5
            [' ---|---|---'],  # ligne tableau
            ['B', ' ', '|', ' ', '|', ' '],  # 3.1 3.3 3.5
            [' ---|---|---'],  # ligne tableau
            ['C', ' ', '|', ' ', '|', ' ']  # 5.1 5.3 5.5
        ]
        debut_temp = time.time()

        while win != 1:
            for ligne in tableau_morpion:
                print(" ".join(map(str, ligne)))

            if joueur % 2 == 1:
                symbole = 'X'
                if bot1:
                    if joueur1 == 'botfacile':
                        position = botfacile()
                    elif joueur1 == 'botimpossible':
                        position = botfacile()
                else:
                    position = input('saisir la case ou mettre : ').lower()
            else:
                symbole = 'O'
                if bot2:
                    if joueur2 == 'botfacile':
                        position = botfacile()
                    elif joueur2 == 'botimpossible':
                        position = botimpossible(tableau_morpion, symbole)
                else:
                    position = input('saisir la case ou mettre : ').lower()

            if position in possible:
                possible.remove(position)
                tableau_morpion[posibilité[position][0]][posibilité[position][1]] = symbole
                joueur = joueur + 1
            else:
                print("case deja prise ou n'existe pas")

            if check_winner('X', tableau_morpion):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print(f'{joueur1} gagne')
                fin_temp = time.time()
                score = int(100 - (fin_temp - debut_temp))
                mise_a_jour_score(joueur1, score, "morpions")

            elif check_winner('O', tableau_morpion):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print(f'{joueur2} gagne')
                fin_temp = time.time()
                score = int(100 - (fin_temp - debut_temp))
                mise_a_jour_score(joueur2, score, "morpions")

            elif all(tableau_morpion[i][j] in ['X', 'O'] for i in [1, 3, 5] for j in [1, 3, 5]):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print("Personne n'a gagné, match nul !")

                jouer = int(joue())

def botfacile():
    global possible
    position = random.choice(possible)
    print(f'le bot a choisi la position {position}')
    return position

def botimpossible(tableau_morpion: list[list[str]], symbole: str) -> str:
    # Implémentation d'un bot impossible à battre
    # Pour simplifier, nous allons utiliser une stratégie de base pour le bot impossible
    for pos in possible:
        # Vérifier si le bot peut gagner
        tableau_morpion[posibilité[pos][0]][posibilité[pos][1]] = symbole
        if check_winner(symbole, tableau_morpion):
            tableau_morpion[posibilité[pos][0]][posibilité[pos][1]] = ' '
            return pos
        tableau_morpion[posibilité[pos][0]][posibilité[pos][1]] = ' '

    # Vérifier si l'adversaire peut gagner au prochain coup et bloquer
    adversaire_symbole = 'O' if symbole == 'X' else 'X'
    for pos in possible:
        tableau_morpion[posibilité[pos][0]][posibilité[pos][1]] = adversaire_symbole
        if check_winner(adversaire_symbole, tableau_morpion):
            tableau_morpion[posibilité[pos][0]][posibilité[pos][1]] = ' '
            return pos
        tableau_morpion[posibilité[pos][0]][posibilité[pos][1]] = ' '

    # Sinon, choisir une position aléatoire
    return random.choice(possible)

if __name__ == "__main__":
    morpion("botfacile", "botimpossible", True, True)