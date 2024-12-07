from jouer import joue
import time
from scores import mise_a_jour_scoretxt
win : int
symbole : str
joueur : int
position : str
jouer : int
debut_temp : float
fin_temp : float
score : int

def morpion(joueur1 :str, joueur2:str):
    
    """
    Simulates a game of Tic-Tac-Toe (Morpion) between two players.
    Parameters:
        joueur1 (str): The name of the first player.
        joueur2 (str): The name of the second player.
    The function will prompt the players to choose who starts first and then alternate turns to place their symbols ('X' or 'O') on the board.
    The game continues until one player wins or the board is full resulting in a draw.
    The function also keeps track of the time taken for the game and updates the score accordingly.
    """
    global jouer, fin_temp, debut_temp, win, joueur , symbole, position, temp, score
    jouer = 1
    while jouer == 1 :
        print('quelle joueur commence par jouer ?')
        print('saisir 1 pour que le joueur 1 commence par jouer')
        print('saisir 2 pour que le joueur 2 commence par jouer')   
        try :
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
            ['  1',' ','2',' ','3 '],       #numligne
            ['A',' ','|', ' ','|', ' '],    #1.1 1.3 1.5
            [' ---|---|---'],               #ligne tableau
            ['B',' ','|', ' ','|', ' '],    #3.1 3.3 3.5
            [' ---|---|---'],               #ligne tableau
            ['C',' ','|', ' ','|', ' ']     #5.1 5.3 5.5
        ]
        debut_temp = time.time()

        
        while win != 1 :
            for ligne in tableau_morpion:
                print(" ".join(map(str, ligne)))

            if joueur % 2 == 1:
                symbole = 'X'
            else :
                symbole = 'O'

            position = input('saisir la case ou mettre : ')
            position = position.lower()
            if position == 'a1' and tableau_morpion[1][1] not in ['X', 'O']:
                tableau_morpion[1][1] = symbole
                joueur = joueur + 1

            elif position == 'a2' and tableau_morpion[1][3] not in ['X', 'O']:
                tableau_morpion[1][3] = symbole
                joueur = joueur + 1

            elif position == 'a3' and tableau_morpion[1][5] not in ['X', 'O']:
                tableau_morpion[1][5] = symbole
                joueur = joueur + 1

            elif position == 'b1' and tableau_morpion[3][1] not in ['X', 'O']:
                tableau_morpion[3][1] = symbole
                joueur = joueur + 1

            elif position == 'b2' and tableau_morpion[3][3] not in ['X', 'O']:
                tableau_morpion[3][3] = symbole
                joueur = joueur + 1

            elif position == 'b3' and tableau_morpion[3][5] not in ['X', 'O']:
                tableau_morpion[3][5] = symbole
                joueur = joueur + 1

            elif position == 'c1' and tableau_morpion[5][1] not in ['X', 'O']:
                tableau_morpion[5][1] = symbole
                joueur = joueur + 1

            elif position == 'c2' and tableau_morpion[5][3] not in ['X', 'O']:
                tableau_morpion[5][3] = symbole
                joueur = joueur + 1

            elif position == 'c3' and tableau_morpion[5][5] not in ['X', 'O']:
                tableau_morpion[5][5] = symbole
                joueur = joueur + 1
                
            else:
                print("case deja prise ou n'existe pas")
            
            if (tableau_morpion[1][1] == 'X' and 
                tableau_morpion[1][3] == 'X' and tableau_morpion[1][5] == 'X') or (tableau_morpion[3][1] == 'X' and 
                tableau_morpion[3][3] == 'X' and tableau_morpion[3][5] == 'X') or (tableau_morpion[5][1] == 'X' and 
                tableau_morpion[5][3] == 'X' and tableau_morpion[5][5] == 'X')or (tableau_morpion[1][1] == 'X' and 
                tableau_morpion[3][1] == 'X' and tableau_morpion[5][1] == 'X') or (tableau_morpion[1][3] == 'X' and 
                tableau_morpion[3][3] == 'X' and tableau_morpion[5][3] == 'X') or (tableau_morpion[1][5] == 'X' and 
                tableau_morpion[3][5] == 'X' and tableau_morpion[5][5] == 'X') or (tableau_morpion[1][1] == 'X' and 
                tableau_morpion[3][3] == 'X' and tableau_morpion[5][5] == 'X') or (tableau_morpion[1][5] == 'X' and 
                tableau_morpion[3][3] == 'X' and tableau_morpion[5][1] == 'X'):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print(f'{joueur1} gagner')
                
                score = 20
                mise_a_jour_scoretxt(joueur1, score, "morpions")
            
            elif (tableau_morpion[1][1] == 'O' and 
                tableau_morpion[1][3] == 'O' and tableau_morpion[1][5] == 'O') or (tableau_morpion[3][1] == 'O' and 
                tableau_morpion[3][3] == 'O' and tableau_morpion[3][5] == 'O') or (tableau_morpion[5][1] == 'O' and 
                tableau_morpion[5][3] == 'O' and tableau_morpion[5][5] == 'O')or (tableau_morpion[1][1] == 'O' and 
                tableau_morpion[3][1] == 'O' and tableau_morpion[5][1] == 'O') or (tableau_morpion[1][3] == 'O' and 
                tableau_morpion[3][3] == 'O' and tableau_morpion[5][3] == 'O') or (tableau_morpion[1][5] == 'O' and 
                tableau_morpion[3][5] == 'O' and tableau_morpion[5][5] == 'O') or (tableau_morpion[1][1] == 'O' and 
                tableau_morpion[3][3] == 'O' and tableau_morpion[5][5] == 'O') or (tableau_morpion[1][5] == 'O' and 
                tableau_morpion[3][3] == 'O' and tableau_morpion[5][1] == 'O'):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print(f'{joueur2}  gagner')
                fin_temp = time.time()
                score = int(100 - (fin_temp - debut_temp))
                mise_a_jour_scoretxt(joueur2, score, "morpions")

            elif (tableau_morpion[1][1] in ['X', 'O'] and tableau_morpion[1][3] in ['X', 'O'] and 
                tableau_morpion[1][5] in ['X', 'O'] and tableau_morpion[3][1] in ['X', 'O'] and 
                tableau_morpion[3][3] in ['X', 'O'] and tableau_morpion[3][5] in ['X', 'O'] and 
                tableau_morpion[5][1] in ['X', 'O'] and tableau_morpion[5][3] in ['X', 'O'] and 
                tableau_morpion[5][5] in ['X', 'O']):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print("personne n'a gagné, match nul !")
        jouer = int(joue())

if __name__ == "__main__":
    morpion('joueur1', 'joueur2')