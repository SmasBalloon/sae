win : int
symbole : str
joueur : int
possition : int
jouer : int

def puissance4():
    global win, joueur , tableau_morpion, symbole, possition, jouer
    while jouer == 1 :
            print('quelle joueur commence par jouer ?')
            print('saisir 1 pour que le joueur 1 commence par jouer')
            print('saisir 2 pour que le joueur 2 commence par jouer')   
            joueur = int(input())
            print()

            win = 0
            tableau_morpion = [
                ['  1',' ','2',' ','3 ','  4',' ','5',' ','6 ',' ','7'],       
                [' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' '],    
                [' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' '],               
                [' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' '],    
                [' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' '],               
                [' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' '],
                [' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' ','|', ' ']     
            ]

        