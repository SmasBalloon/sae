# Dimensions du plateau
from scores import mise_a_jour_scoretxt
Nblignes = 6
Nbcoll = 7

def creation_table():
    """Créer un plateau de jeu vide."""
    global Nblignes, Nbcoll
    return [[" " for _ in range(Nbcoll)] for _ in range(Nblignes)]

def print_table(tableau: list[list[str]]):
    """Afficher le plateau de jeu."""
    for row in reversed(tableau):
        print("| " + " | ".join(map(str, row)) + " |")
    print("  " + "   ".join(map(str, range(Nbcoll))))

def emplacement_valid(tableau: list[list[str]], col:int) ->bool:
    """Vérifie si une colonne accepte encore un jeton."""
    if tableau[Nblignes-1][col] == " ":
        return True
    return False

def prochaine_ligne_libre(tableau: list[list[str]], col:int) -> int:
    """Retourne l'indice de la première ligne libre dans une colonne."""
    for row in range(Nblignes):
        if tableau[row][col] == " ":
            return row
    return -1  # Return a default value if no free row is found

def pose_piece(tableau: list[list[str]], row:int, col:int, piece:str):
    """Ajoute un jeton au plateau."""
    tableau[row][col] = str(piece)

def coup_gagnant(tableau: list[list[str]], piece:str):
    """Vérifie si le dernier coup est un coup gagnant."""
    # Vérification des alignements horizontaux
    for row in range(Nblignes):
        for col in range(Nbcoll - 3):
            if all(tableau[row][col + i] == str(piece) for i in range(4)):
                return True

    # Vérification des alignements verticaux
    for col in range(Nbcoll):
        for row in range(Nblignes - 3):
            if all(tableau[row + i][col] == str(piece) for i in range(4)):
                return True

    # Vérification des diagonales montantes
    for row in range(Nblignes - 3):
        for col in range(Nbcoll - 3):
            if all(tableau[row + i][col + i] == str(piece) for i in range(4)):
                return True

    # Vérification des diagonales descendantes
    for row in range(3, Nblignes):
        for col in range(Nbcoll - 3):
            if all(tableau[row - i][col + i] == str(piece) for i in range(4)):
                return True

    return False

def dessiner(tableau: list[list[str]]):
    """Vérifie si le plateau est plein."""
    return all(tableau[Nblignes - 1][col] != " " for col in range(Nbcoll))

def lancer_partie(joueur1 : str, joueur2 : str):
    """Simule un jeu de Puissance 4."""
    tableau : list[list[str]] = creation_table()
    fin_de_partie = False
    player : int = 1
    turn : int = 0

    print("Bienvenue dans Puissance 4 !")
    print_table(tableau)

    while not fin_de_partie:
        # Détermine le joueur actuel
        player = turn % 2 + 1
        if player == 1:
            piece = "\033[0;33;40mO\033[0m"
        else:
            piece = "\033[0;31;40mO\033[0m"

        print(f"\nTour du joueur {player}.")
        
        try:
            col = int(input("Choisissez une colonne (0-6) : "))
            if col < 0 or col >= Nbcoll:
                print("Colonne invalide. Réessayez.")
                continue
        except ValueError:
            print("Entrée invalide. Réessayez.")
            continue

        # Vérifie si le coup est valide
        if emplacement_valid(tableau, col):
            row = prochaine_ligne_libre(tableau, col)
            pose_piece(tableau, row, col, piece)

            if coup_gagnant(tableau, piece):
                print_table(tableau)
                if player == 1:
                    winner = joueur1
                else:
                    winner = joueur2
                    
                print(f"\nFélicitations ! Le joueur {winner} a gagné !")
                print(f"\nLe joueur {winner} remporte 30 points !")
                mise_a_jour_scoretxt(winner, 30, "puissances4")
                fin_de_partie = True
            elif dessiner(tableau):
                print_table(tableau)
                print("\nMatch nul !")
                fin_de_partie = True
            else:
                turn += 1
        else:
            print("Cette colonne est pleine. Essayez une autre.")

        print_table(tableau)

if __name__ == "__main__":
    lancer_partie("joueur1", "joueur2")
