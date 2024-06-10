from numpy.linalg import norm, det
import numpy as np

def info_parallelogramme(p1, p2, p3):
    """Retourne les informations sur le parallélogramme formé par les vecteurs p2 --> p1 et p2 --> p3
    
    Keywords arguments:
    p1 -- le premier point du parallélogramme
    p2 -- le coin commun aux deux vecteurs
    p3 -- le troisième point du parallélogramme
    """
    vecteur1 = np.subtract(p1, p2)
    vecteur2 = np.subtract(p3, p2)
    
    # Angle du parallelogramme
    angle = np.arccos(np.dot(vecteur1, vecteur2) / (norm(vecteur1) * norm(vecteur2))) * 180 / np.pi
    
    # Aire du parallélogramme
    matrice_parallelogramme = np.mat([vecteur1, vecteur2])	# Crée la matrice par ligne
    aire = np.abs(det(matrice_parallelogramme))
    
    return {
        'p4' : p2 + vecteur1 + vecteur2,
        'angle' : [angle, 180.0 - angle],
        'matrice' : matrice_parallelogramme,
        'aire' : aire
    }

def main():
    print(info_parallelogramme((1.5, 6), (0.25, -1.2), (3.85, 2)))

if __name__ == "__main__":
    main()