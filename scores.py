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
    conn = sqlite3.connect("scorejeux.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS score_{jeu}(
                    nom_joueur varchar(255),
                    score int
                    )""".format(jeu=jeu))
    cursor.execute("INSERT INTO score_{jeu} (nom_joueur, score) VALUES (?, ?)".format(jeu=jeu), (joueur, point))
    conn.commit()
    cursor.close()
    conn.close()



def lire_meilleur(jeu : str):
    """
    Lit les meilleurs scores pour un jeu donné.
    Args:
        jeu (str): Le nom du jeu pour lequel les meilleurs scores doivent être lus. 
                Doit être l'un des suivants: 'allumettes', 'morpions', 'devinettes', 'puissances4'.
    """
    conn = sqlite3.connect("scorejeux.db")
    cursor = conn.cursor()
    cursor.execute("select * from score_{jeu} order by score ASC".format(jeu=jeu))
    print(cursor.fetchall())
    cursor.close()
    conn.close()

if __name__ == "__main__":
    mise_a_jour_score("botfacile", 5, "morpions")
    mise_a_jour_score("botmoyen", 10, "morpions")
    mise_a_jour_score("botimpossible", 15, "morpions")
    lire_meilleur("morpions")