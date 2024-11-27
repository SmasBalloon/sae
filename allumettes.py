from jouer import joue
from scores import mise_a_jour_scoretxt


allumettes:int 
soustraction:int
joueur1:int
joueur2:int
jouer : int = 1
score1 : int = 0
score2 : int = 0
joueur : int

def allumette(joueur1:str , joueur2:str):
    global jouer, score1, score2, joueur
    while jouer == 1 :
        
        print('quelle joueur commence par jouer ?')
        print('saisir 1 pour que le joueur 1 commence par jouer')
        print('saisir 2 pour que le joueur 2 commence par jouer')
        joueur = int(input())
        print()
        if joueur == 3:
            print('quelle joueur commence par jouer ?')
            print('saisir 1 pour que le joueur 1 commence par jouer')
            print('saisir 2 pour que le joueur 2 commence par jouer')
            joueur = int(input())
            print()
        allumettes = 20
        print('la possition de depart')
        print()
        print('|'*allumettes)
        print()


        while allumettes > 0 :
            if joueur%2 == 1:
                    print(f"{joueur1} à toi de jouer")
            else:
                print(f"{joueur2} à toi de jouer")

            soustraction = int(input("combien d'allumette  veux tu enlever : "))

            if 0 < soustraction < 4 :
                allumettes = allumettes - soustraction
            else :
                print('error')

            if allumettes > 0:
                print()
                print('il reste:')
                print('|'*allumettes)
                print()
            joueur = joueur + 1

            if allumettes <= 0 :
                if joueur%2 == 1:
                    joueur = 1
                else:
                    joueur = 2
                print()
                print('player',joueur,'win')
                print()

                if joueur == 1:
                    score1 = score1 + 20
                else :
                    score2 = score2 + 20
                
                print(f"joueur 1 à {score1} points")
                print(f"joueur 2 a {score2} points")
                

        jouer = int(joue())

        if jouer != 1 :
            mise_a_jour_scoretxt(joueur1 , score1, "allumettes")
            mise_a_jour_scoretxt(joueur2 , score2, "allumettes")