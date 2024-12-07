import os
from typing import List, Tuple
score_t1 : int
score_t2 : int


def mise_a_jour_scoretxt(joueur_w: str, point: int, jeu: str):
    """
    Met à jour le fichier de score pour un jeu donné avec le score d'un joueur.
    Args:
        joueur_w (str): Le nom du joueur gagnant.
        point (int): Le nombre de points gagnés par le joueur.
        jeu (str): Le nom du jeu pour lequel le score doit être mis à jour. 
                Doit être l'un des suivants: 'allumettes', 'morpions', 'devinettes', 'puissances4'.
    Raises:
        ValueError: Si le nom du jeu fourni n'est pas valide.
    """

    fichiers_scores = {
        j: os.path.join("fictxt", f"score_{j}.txt")
        for j in ["allumettes", "morpions", "devinettes", "puissances4"]
    }

    if jeu in fichiers_scores:
        chemin = fichiers_scores[jeu]

        with open(chemin, "a") as fichier:
            fichier.write(f"{joueur_w} : {point} pts\n")
            fichier.close()
        trier_scores_par_points(chemin)
    else:
        print("Jeu invalide. Veuillez choisir parmi 'allumettes', 'morpions', 'devinettes', 'puissances4'")



def lire_meilleurs(nom : str):
    """
    Lit et affiche le meilleur score pour un jeu donné.
    Args:
        nom (str): Le nom du jeu pour lequel lire le score. 
                Les valeurs possibles sont 'devinette', 'allumette', 'morpion', et 'puissance'.
    Raises:
        FileNotFoundError: Si le fichier de score pour le jeu spécifié n'existe pas.
        KeyError: Si le nom du jeu spécifié n'est pas dans la liste des jeux supportés.
    """

    fichiers_scores = {
        'devinette': os.path.join("fictxt", "score_devinette.txt"),
        'allumette': os.path.join("fictxt", "score_allumette.txt"),
        'morpion': os.path.join("fictxt", "score_morpions.txt"),
        'puissance': os.path.join("fictxt", "score_puissance.txt")
    }

    if nom in fichiers_scores:
        chemin = fichiers_scores[nom]
        
        with open(chemin, "r") as fichier:
            contenu = fichier.readline()
            print(contenu)
            input("")
            fichier.close()

def trier_scores_par_points(fichier: str):
    """
    Trie les scores dans un fichier par ordre décroissant de points.
    Le fichier doit contenir des lignes au format "nom : score pts".
    Les scores sont extraits, triés et réécrits dans le fichier dans l'ordre décroissant.
    Args:
        fichier (str): Le chemin du fichier contenant les scores à trier.
    Raises:
        ValueError: Si le format d'une ligne dans le fichier est incorrect.
    """
    
    with open(fichier, "r") as f:
        lignes: List[str] = f.readlines()  
        f.close()
    scores: List[Tuple[str, int]] = []
    for ligne in lignes:
        nom, score_texte = ligne.split(" : ")
        score = int(score_texte.replace(" pts", "").strip()) 
        scores.append((nom, score))
        
    scores_triees: List[Tuple[str, int]] = sorted(scores, key=lambda x: x[1], reverse=True)
    with open(fichier, "w") as f:
        for nom, score in scores_triees:
            f.write(f"{nom} : {score} pts\n")
            f.close()



if __name__ == "__main__":
    mise_a_jour_scoretxt("joueur1", 20, "morpions")