def diffbot(joueur1: str, joueur2: str, bot1: bool, bot2: bool):
    bots = ["botfacile", "botmoyen", "botimpossible"]

    def get_difficulty():
        print('1 facile')
        print('2 moyen')
        print('3 impossible')
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
        return difficulte

    def definir_difficulter(joueur : str):
        difficulte = get_difficulty()
        if difficulte == 1:
            return "botfacile"
        elif difficulte == 2:
            return "botmoyen"
        else:
            return "botimpossible"

    if bot1 and joueur1 in bots:
        print('voulez vous changer la difficulté du bot 1 ? O/N')
        choix = input().lower()
        while choix not in ["o", "n"]:
            print("\33[0;31;40m erreur : veuillez saisir soit O soit N \033[0m\n")
            choix = input().lower()
        if choix == "o":
            print('quelle difficulté voulez vous mettre pour le bot 1?')
            joueur1 = definir_difficulter(joueur1)

    if bot2 and joueur2 in bots:
        print('voulez vous changer la difficulté du bot 2 ? O/N')
        choix = input().lower()
        while choix not in ["o", "n"]:
            print("\33[0;31;40m erreur : veuillez saisir soit O soit N \033[0m\n")
            choix = input().lower()
        if choix == "o":
            print('quelle difficulté voulez vous mettre pour le bot 2?')
            joueur2 = definir_difficulter(joueur2)

    return(joueur1, joueur2 , bot1, bot2)

if __name__ == "__main__":
    diffbot("botfacile", "botimpossible", True, True)

