import locale
import numpy as np


def est_triangulaire(matrice):
    """Détermine si une matrice est triangulaire. Aucune distinction n'est faite entre supérieure et inférieure

    keywords arguments:
    matrice -- la matrice pour laquelle tester la triangularité
    """
    dimension = np.shape(matrice)

    if dimension[0] != dimension[1]:
        return False

    est_triangulaire_superieure = True
    est_triangulaire_inferieure = True

    # Parcours de la matrice
    for i in range(dimension[0]):
        for j in range(dimension[1]):
            # On vérifie la présence d'un élément non nul. Dès qu'il y en a un, alors on met le test à False
            # Si aucun n'est non nul, alors à la fin du parcours la variable du test est toujours à True
            if i > j and not np.isclose(matrice[i, j], 0.0):
                est_triangulaire_inferieure = False
            elif j > i and not np.isclose(matrice[i, j], 0.0):
                est_triangulaire_superieure = False

    return est_triangulaire_inferieure or est_triangulaire_superieure


def analyse_matrice(matrice):
    """Réalise l'analyse d'un matrice et retourne les informations sur celle-ci

    keywords arguments:
    matrice -- la matrice à analyser
    """
    dimension = np.shape(matrice)
    est_carree = dimension[0] == dimension[1]
    determinant = np.linalg.det(matrice) if est_carree else None
    est_inversible = determinant is not None and not np.isclose(determinant, 0.0)

    return {
        "matrice": matrice,
        "dimension": dimension,
        "rang": (
            np.linalg.matrix_rank(matrice)
        ),
        "est_singuliere": not est_inversible,
        "est_triangulaire": (
            est_triangulaire(matrice)
            if est_carree
            else "La triangularité n'est pas définie pour les matrices quelconques"
        ),
        "est_carree": est_carree,
        "trace": (
            np.trace(matrice)
            if est_carree
            else "Trace non définie pour les matrices quelconques"
        ),
        "determinant": (
            determinant
            if determinant is not None
            else "Déterminant non défini pour les matrices quelconques"
        ),
        "inverse": (
            np.linalg.inv(matrice)
            if est_inversible
            else "La matrice n'est pas inversible"
        ),
        "orthogonale": (
            np.allclose(np.linalg.inv(matrice), np.transpose(matrice))
            if est_inversible
            else "Une matrice singulière ne peut pas être orthogonale"
        ),
    }


def main():
    """Fonction principale du programme"""

    # Système d'équation
    equations = [(2, -1.5, 7), (3.4, 7.1, -9), (2, 0, 4)]
    # 2x_1 -1.5x_2 + 7x_3 // 3.4x_1, 7.1x_2 -9x_3 // 2x_1 + 4x_3

    matrice = np.mat(equations)
    info_matrice = analyse_matrice(matrice)

    print("Information sur la matrice du système\n", info_matrice)

    # Valeur recherchée pour le système d'équation
    valeurs = (5, 8, -2)

    if not info_matrice["est_singuliere"]:
        solution = np.linalg.solve(matrice, valeurs)
        print("Solution ", solution)

    # Représentation dans une autre base
    base = np.mat([(1, 1, 0), (0, 0.5, 1), (1, -1, -1)])
    info_base = analyse_matrice(base)

    matrice_nouvelle_base = base @ matrice
    print("Nouvelle base ", matrice_nouvelle_base)

    matrice_originale = info_base["inverse"] @ matrice_nouvelle_base
    print("Matrice originale base ", matrice_originale)


if __name__ == "__main__":
    locale.setlocale(
        locale.LC_ALL, "fr_CA"
    )  # Paramètre de langue locale français Canada. Utilise des , pour les décimales
    main()
