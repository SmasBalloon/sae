import os
from typing import List, Tuple
score_t1 : int
score_t2 : int


def mise_a_jour_scoretxt(joueur_w: str, point: int, jeu: str):
    fichiers_scores = {
        "allumettes": os.path.join("fictxt", "score_allumette.txt"),
        "morpions": os.path.join("fictxt", "score_morpions.txt"),
        "devinettes": os.path.join("fictxt", "score_devinette.txt"),
        "puissances4": os.path.join("fictxt", "score_puissance.txt")
    }

    if jeu in fichiers_scores:
        chemin = fichiers_scores[jeu]

        with open(chemin, "a") as fichier:
            fichier.write(f"{joueur_w} : {point} pts\n")
            fichier.close()
        trier_scores_par_points(chemin)
    else:
        print("Jeu invalide. Veuillez choisir parmi 'allumettes', 'morpions', 'devinettes', 'puissances4'.")

def lire_meilleurs(nb: int):
    fichiers_scores = {
        1: os.path.join("fictxt", "score_devinette.txt"),
        2: os.path.join("fictxt", "score_allumette.txt"),
        3: os.path.join("fictxt", "score_morpions.txt"),
        4: os.path.join("fictxt", "score_puissance.txt")
    }

    if nb in fichiers_scores:
        chemin = fichiers_scores[nb]
        


        with open(chemin, "r") as fichier:
            contenu = fichier.readline()
            print(contenu)
            fichier.close()
    else:
        print("Numéro invalide. Veuillez choisir un nombre entre 1 et 4.")

def trier_scores_par_points(fichier: str):
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