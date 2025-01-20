def diffbot(joueur1: str, joueur2: str, bot1: bool, bot2: bool):
    '''
    Fonction qui permet de demander à l'utilisateur de choisir la difficulté des bots
    Args:
        joueur1 (str): Le nom du premier joueur.
        joueur2 (str): Le nom du deuxième joueur.
        bot1 (bool): Indicateur si le premier joueur est un bot.
        bot2 (bool): Indicateur si le deuxième joueur est un bot.
    Returns:
        Tuple[str, str, bool, bool]: Les noms des joueurs et les indicateurs des bots.
    '''
    bots = ["botfacile", "botimpossible"]

    def get_difficulty():
        '''
        Demande à l'utilisateur de choisir la difficulté du bot.
        Returns:
            int: La difficulté du bot.
        '''
        print('1 facile')
        print('2 impossible')
        try:
            difficulte = int(input().strip())
        except ValueError:
            difficulte = 0
        while difficulte not in [1, 2, 3]:
            print("\33[0;31;40m erreur : veuillez saisir un nombre entre 1 et 2 \033[0m\n")
            try:
                difficulte = int(input().strip())
            except ValueError:
                difficulte = 0
        return difficulte

    def definir_difficulter(joueur : str):
        '''
        Demande à l'utilisateur de choisir la difficulté du bot.
        Args:
            joueur (str): Le nom du bot.
        Returns:
            str: Le nom du bot avec la difficulté.
        '''
        difficulte = get_difficulty()
        if difficulte == 1:
            return "botfacile"
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