import os
import random
import time
from scores import mise_a_jour_score 


def clear_terminal():
    os.system('cls')

def devinette(joueur1:str , joueur2:str, bot1:bool, bot2:bool):
    """
    Fonction pour jouer à un jeu de devinettes entre deux joueurs.
    Parameters:
        joueur1 (str): Le nom du premier joueur.
        joueur2 (str): Le nom du deuxième joueur.
    Description:
        Le jeu permet à deux joueurs de choisir entre deviner ou faire deviner une devinette. 
        Le joueur peut choisir de deviner (option 1) ou de faire deviner (option 2). 
        Le jeu continue jusqu'à ce que le joueur entre l'option 3 pour quitter.
        Les fonctions `Joueur1Maitre` et `Joueur2Maitre` sont appelées en fonction du choix du joueur.
    """

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
    """
    Permet au joueur 1 de définir un nombre à deviner pour le joueur 2 et gère le processus de devinette.
    Args:
        joueur2 (str): Le nom du joueur 2.
    Le joueur 1 choisit un nombre entre 0 et 1000 que le joueur 2 doit deviner.
    Le joueur 2 fait des propositions jusqu'à ce qu'il trouve le bon nombre.
    Le programme indique si la proposition est trop haute ou trop basse.
    Une fois le nombre deviné, le programme affiche le nombre d'essais et calcule le score du joueur 2.
    Le score est mis à jour dans un fichier texte.
    Returns:
        None
    """

    
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
    mise_a_jour_score(joueur2 , score, 'devinettes')
    

def Joueur2Maitre(joueur1:str):
    """
    Permet au joueur 2 de définir un nombre que le joueur 1 doit deviner, puis gère le processus de devinette.
    Args:
        joueur1 (str): Le nom du joueur 1.
    Le joueur 2 choisit un nombre entre 0 et 1000 que le joueur 1 doit deviner. Le joueur 1 propose des nombres jusqu'à ce qu'il trouve le bon.
    Le programme indique si la proposition est trop haute, trop basse ou correcte. Le nombre de tentatives est compté et un score est calculé en fonction du nombre de tentatives.
    Le score est ensuite mis à jour dans un fichier de score.
    Returns:
        None
    """

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
    mise_a_jour_score(joueur1 , score, 'devinettes')



def botfacile(statue:int):
    '''
    Simule un jeu d'allumettes entre un joueur et un bot.
    Le bot retire aléatoirement entre 1 et 3 allumettes.
    '''
    ChoixPossible=[0,100,200,300,400,500,600,700,800,900,1000,250,750]
    if statue == 1:
        time.sleep(1)
        choix = random.randint(0, 12)
        Adeviner=ChoixPossible[choix]
        print(Adeviner)
        
    else :
        time.sleep(1)
        choix = random.randint(0,1000)
        return choix

def botmoyen(statue:int):
    '''
    Simule un jeu d'allumettes entre un joueur et un bot.
    Le bot retire aléatoirement entre 1 et 3 allumettes.'''
    if statue == 1:
        choix = random.randint(0, 1000)
        return choix
    else :
        print("hello world")

def botimposible(statue:int):
    '''
    Simule un jeu d'allumettes entre un joueur et un bot.
    Le bot retire aléatoirement entre 1 et 3 allumettes.'''
    if statue == 1:
        choix = random.randint(0, 1000)
        return choix
    else :
        print("hello world")


def untrucfacile():
    resultat:int=100
    choix:int=randint(1,455)
    reponse:str=input("untruc")
    turn=0

    while resultat!=choix:
        if reponse == "trop haut":
            choix=randint(0,choix)
            turn+=1
            return choix
        else:
            choix=randint(choix,1000)
            turn+=1
            return choix 



def untrucmoyen():
    resultat:int=randint(0,1000)
    choix:int=500
    reponse:str=input("untruc")
    turn=0
    var:int=250

    while resultat!=choix:
        if reponse == "trop haut":
            choix=int(choix-var)
        else:
            choix=int(choix+var) 
        var=int(var/2)
        turn+=1
        print(choix)

def untrucimpossible():
    resultat:int=randint(0,1000)
    print(resultat)
    