import os
from scores import update_scoretxt1
from scores import update_scoretxt2


def clear_terminal():
    if os.name == 'nt':  # Pour Windows
        os.system('cls')

def devinette(joueur1:str , joueur2:str):
    choix : int
    choix = int(input('Voulez vous deviner(1) ou faire deviner(2)? : '))
    while choix != 3:
        if choix == 1 :
            Joueur1Maitre(joueur2)
        if choix == 2 :
            Joueur2Maitre(joueur1)
        else:
            print('veuillez entre une option valide')
        choix = int(input('Voulez vous deviner(1) ou faire deviner(2)? : '))
    print('A bientôt!')


def Joueur1Maitre(joueur2:str):
    score:int
    nbadeviner:int
    reponse:int
    reponse=0
    nbadeviner = int(input('Quel chiffre le joueur 2 doit-il deviner? Le chiffre doit être compris entre 0 et 1000.'))
    while not 0<nbadeviner<1000:
        print ("Ce nombre n'est pas valide")
        nbadeviner = int(input('Quel chiffre le joueur 2 doit-il deviner? Le chiffre doit être compris entre 0 et 1000.'))
    clear_terminal()
    gess = 2000
    while gess!=nbadeviner :
        gess = int(input("Quel est votre proposition ?"))
        reponse+=1
        print(input('Le joueur 2 est-il trop haut ou trop bas ?'))
    print ("Bravo!!! Tu as devine en ",reponse,"essaies")
    score = int(100/reponse)
    print ("le joueur 2 remporte donc ",score," points !")
    update_scoretxt2(joueur2 , score)
    

def Joueur2Maitre(joueur1:str):
    score:int
    nbadeviner:int
    reponse:int
    reponse=0
    nbadeviner = int(input('Quel chiffre le joueur 1 doit-il deviner? Le chiffre doit être compris entre 0 et 1000.'))
    while not 0<nbadeviner<1000:
        print ("Ce nombre n'est pas valide")
        nbadeviner = int(input('Quel chiffre le joueur 1 doit-il deviner? Le chiffre doit être compris entre 0 et 1000.'))
    clear_terminal()
    gess = 2000
    
    while gess!=nbadeviner :
        gess = int(input("Quel est votre proposition ? :"))
        reponse+=1
        print(input('Le joueur 1 est-il trop haut, trop bas ou bon ? :'))
    print ("Bravo!!! Tu as devine en ",reponse,"essaies")
    score = int(100/reponse)
    print ("le joueur 1 remporte donc ",score," points !")
    update_scoretxt1(joueur1 , score)

