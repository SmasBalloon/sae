jouer : int = 1
def joue():
    print("----------------------------------")
    print()
    print()
    print("saisir 1 pour continuer a jouer")
    print("saisir 2 pour quitter")
    print()
    print()
    print("----------------------------------")
    try :
        jouer = input()
    except ValueError :
        jouer = 2
    return jouer
