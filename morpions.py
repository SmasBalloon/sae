from jouer import joue
from scores import mise_a_jour_scoretxt
win : int
symbole : str
joueur : int
possition : int
jouer : int

def morpion(joueur1 :str, joueur2:str):
    global jouer
    jouer = 1
    while jouer == 1 :
        print('quelle joueur commence par jouer ?')
        print('saisir 1 pour que le joueur 1 commence par jouer')
        print('saisir 2 pour que le joueur 2 commence par jouer')   
        joueur = int(input())
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

        
        while win != 1 :
            for ligne in tableau_morpion:
                print(" ".join(map(str, ligne)))

            if joueur % 2 == 1:
                symbole = 'X'
            else :
                symbole = 'O'

            possition = input('saisir la case ou mettre : ')
            possition = possition.lower()
            if possition =='a1' and tableau_morpion[1][1] != ('X' or 'O'):
                tableau_morpion[1][1] = symbole
                joueur = joueur +1

            elif possition == 'a2'and tableau_morpion[1][3] != ('X' or 'O'):
                tableau_morpion[1][3] = symbole
                joueur = joueur +1

            elif possition == 'a3'and tableau_morpion[1][5] != ('X' or 'O'):
                tableau_morpion[1][5] = symbole
                joueur = joueur +1

            elif possition == 'b1'and tableau_morpion[3][1] != ('X' or 'O'):
                tableau_morpion[3][1] = symbole
                joueur = joueur +1

            elif possition == 'b2'and tableau_morpion[3][3] != ('X' or 'O'):
                tableau_morpion[3][3] = symbole
                joueur = joueur +1

            elif possition == 'b3'and tableau_morpion[3][5] != ('X' or 'O'):
                tableau_morpion[3][5] = symbole
                joueur = joueur +1

            elif possition == 'c1'and tableau_morpion[5][1] != ('X' or 'O'):
                tableau_morpion[5][1] = symbole
                joueur = joueur +1

            elif possition == 'c2'and tableau_morpion[5][3] != ('X' or 'O'):
                tableau_morpion[5][3] = symbole
                joueur = joueur +1

            elif possition == 'c3' and tableau_morpion[5][5] != ('X' or 'O'):
                tableau_morpion[5][5] = symbole
                joueur = joueur +1
                
            else:
                print("case deja prise ou n'existe pas")
            
            if (tableau_morpion[1][1] == 'X' and tableau_morpion[1][3] == 'X' and tableau_morpion[1][5] == 'X') or (tableau_morpion[3][1] == 'X' and tableau_morpion[3][3] == 'X' and tableau_morpion[3][5] == 'X') or (tableau_morpion[5][1] == 'X' and tableau_morpion[5][3] == 'X' and tableau_morpion[5][5] == 'X')or (tableau_morpion[1][1] == 'X' and tableau_morpion[3][1] == 'X' and tableau_morpion[5][1] == 'X') or (tableau_morpion[1][3] == 'X' and tableau_morpion[3][3] == 'X' and tableau_morpion[5][3] == 'X') or (tableau_morpion[1][5] == 'X' and tableau_morpion[3][5] == 'X' and tableau_morpion[5][5] == 'X') or (tableau_morpion[1][1] == 'X' and tableau_morpion[3][3] == 'X' and tableau_morpion[5][5] == 'X') or (tableau_morpion[1][5] == 'X' and tableau_morpion[3][3] == 'X' and tableau_morpion[5][1] == 'X'):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print('joueur 1 gagner')
                mise_a_jour_scoretxt(joueur1, 20, 'morpions')
            elif (tableau_morpion[1][1] == 'O' and tableau_morpion[1][3] == 'O' and tableau_morpion[1][5] == 'O') or (tableau_morpion[3][1] == 'O' and tableau_morpion[3][3] == 'O' and tableau_morpion[3][5] == 'O') or (tableau_morpion[5][1] == 'O' and tableau_morpion[5][3] == 'O' and tableau_morpion[5][5] == 'O')or (tableau_morpion[1][1] == 'O' and tableau_morpion[3][1] == 'O' and tableau_morpion[5][1] == 'O') or (tableau_morpion[1][3] == 'O' and tableau_morpion[3][3] == 'O' and tableau_morpion[5][3] == 'O') or (tableau_morpion[1][5] == 'O' and tableau_morpion[3][5] == 'O' and tableau_morpion[5][5] == 'O') or (tableau_morpion[1][1] == 'O' and tableau_morpion[3][3] == 'O' and tableau_morpion[5][5] == 'O') or (tableau_morpion[1][5] == 'O' and tableau_morpion[3][3] == 'O' and tableau_morpion[5][1] == 'O'):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print('joueur 2  gagner')
                mise_a_jour_scoretxt(joueur2, 20, 'morpions')

            elif (tableau_morpion[1][1] in ['X', 'O'] and tableau_morpion[1][3] in ['X', 'O'] and tableau_morpion[1][5] in ['X', 'O'] and tableau_morpion[3][1] in ['X', 'O'] and tableau_morpion[3][3] in ['X', 'O'] and tableau_morpion[3][5] in ['X', 'O'] and tableau_morpion[5][1] in ['X', 'O'] and tableau_morpion[5][3] in ['X', 'O'] and tableau_morpion[5][5] in ['X', 'O']):
                win = 1
                for ligne in tableau_morpion:
                    print(" ".join(map(str, ligne)))
                print("personne n'a gagné, match nul !")
        jouer = int(joue())