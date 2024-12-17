import sqlite3
score_t1 : int
score_t2 : int


def mise_a_jour_score(joueur: str, point: int, jeu: str):
    """
    Met à jour le fichier de score pour un jeu donné.
    Args:
        joueur_w (str): Le nom du joueur ayant gagné la partie.
        point (int): Le nombre de points à ajouter au score du joueur.
        jeu (str): Le nom du jeu pour lequel le score doit être mis à jour. 
                Doit être l'un des suivants: 'allumettes', 'morpions', 'devinettes', 'puissances4'.
    """
    cursor = sqlite3.connect("scorejeux.db").cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS score_{jeu}(
                    nom_joueur varchar(255),
                    score int
                    )""".format(jeu=jeu))
    cursor.execute("INSERT INTO score_{jeu} (nom_joueur, score) VALUES (?, ?)".format(jeu=jeu), (joueur, point))



def lire_meilleurs(jeu : str):
    """
    Lit les meilleurs scores pour un jeu donné.
    Args:
        jeu (str): Le nom du jeu pour lequel les meilleurs scores doivent être lus. 
                Doit être l'un des suivants: 'allumettes', 'morpions', 'devinettes', 'puissances4'.
    Returns:
        list: Une liste de tuples contenant le nom du joueur et son score.
    """
    cursor = sqlite3.connect("scorejeux.db").cursor()
    cursor.execute("select * from score_{jeu} order by score ASC".format(jeu=jeu))
    print(cursor.fetchall())

if __name__ == "__main__":
    lire_meilleurs("morpions")