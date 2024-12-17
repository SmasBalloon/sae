def diffnot(joueur1 : str , joueur2 : str):
    if ((joueur1 == "botfacile@" or "botmoyen@" or "botimposible@") and (joueur2 != "botfacile@" or "botmoyen@" or "botimposible@")):
        print('voulez vous changer la difficulté du bot ? O/N')
        try :
            choix = str(input().lower())
        except ValueError:
            choix = ""
        while choix not in ["o", "n"]:
            print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 3 \033[0m\n")
            try:
                choix = str(input().lower())
            except ValueError:
                choix = ""

        if choix == "o":
            print('quelle difficulté voulez vous mettre ?')
            print('1 facile')
            print('2 moyen')
            print('3 imposible')
            try:
                difficulte = int(input().strip())
            except ValueError:
                difficulte = 0
            while difficulte not in [1, 2, 3]:
                print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 3 \033[0m\n")
                try:
                    difficulte = int(input().strip())
                except ValueError:
                    difficulte = 0
            if difficulte == 1:
                joueur1 = "botfacile@"
            elif difficulte == 2:
                joueur1 = "botmoyen@"
            else: 
                joueur1 = "botimposible@"
    
    elif joueur2 and joueur1 == "botfacile@" or "botmoyen@" or "botimposible@":
        print('voulez vous changer la difficulté des bot ? O/N')
        try :
            choix = str(input().lower())
        except ValueError:
            choix = ""
        while choix not in ["o", "n"]:
            print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 3 \033[0m\n")
            try:
                choix = str(input().lower())
            except ValueError:
                choix = ""

        if input() == "O":
            print('quelle difficulté voulez vous mettre pour le bot 1?')
            print('1 facile')
            print('2 moyen')
            print('3 imposible')
            try:
                difficulte = int(input().strip())
            except ValueError:
                difficulte = 0
            while difficulte not in [1, 2, 3]:
                print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 3 \033[0m\n")
                try:
                    difficulte = int(input().strip())
                except ValueError:
                    difficulte = 0
            if difficulte == 1:
                joueur1 = "botfacile@"
            elif difficulte == 2:
                joueur1 = "botmoyen@"
            else:
                joueur1 = "botimposible@"

            print('quelle difficulté voulez vous mettre pour le bot 2?')
            print('1 facile')
            print('2 moyen')
            print('3 imposible')
            try:
                difficulte2 = int(input().strip())
            except ValueError:
                difficulte2 = 0
            while difficulte2 not in [1, 2, 3]:
                print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 3 \033[0m\n")
                try:
                    difficulte2 = int(input().strip())
                except ValueError:
                    difficulte2 = 0
            if difficulte2 == 1:
                joueur2 = "botfacile@"
            elif difficulte2 == 2:
                joueur2 = "botmoyen@"
            else:
                joueur2 = "botimposible@"

if __name__ == "__main__":
    diffnot("botfacile@" , "botmoyen@")