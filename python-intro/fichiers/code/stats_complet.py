import numpy as np
import pandas as pd
import scipy.stats as stats


def statistiques_descriptives(serie):
    """Dresse la statistique descriptive (min, max, somme, moyenne, écrat-type, médiane et nombre d'observations)

    keywords arguments:
    serie -- la série surlaquelle réaliser l'analyse
    """
    return {
        "n": len(serie),
        "min": min(serie),
        "max": max(serie),
        "mediane": np.median(serie),
        "Q1": np.quantile(serie, 0.25),
        "Q3": np.quantile(serie, 0.75),
        "moyenne": np.mean(serie),
        "ecart-type": np.std(serie),
    }


def importer_donnees():
    "Importe le jeu de données sur les températures"
    donnees = pd.read_excel(
        "C:\\Projets\\notes-cours\\python-intro\\docs\\fichiers\\code\\Quebec_temp.xlsx"
    )

    return donnees


def intervalle_confiance(serie, niveau_confiance=0.95):
    """Calcule l'intervalle de confiance autour d'une moyenne

    keywords arguments:
    serie -- les données pour lesquelles calculer l'intervalle de confiance
    niveau_confiance -- le niveau de confiance de l'intervalle
    """
    erreur_standard = (
        stats.norm.ppf(niveau_confiance) * np.std(serie) / np.sqrt(len(serie))
    )
    moyenne = np.mean(serie)

    return (moyenne - erreur_standard, moyenne + erreur_standard)


def calculer_variation(serie):
    """Calcul les variations entre deux éléments de la série. Retourne une liste de longueur N - 1 avec N la longueur de la série

    keywords arguments:
    serie -- les données pour lesquelles calculer les variations
    """
    variations = []
    for i in range(len(serie) - 1):
        variations.append(serie[i + 1] - serie[i])

    return variations


def main():
    "Fonction principale du programme"
    donnees = importer_donnees()

    # Analyse de statistiques descriptives
    for colonne in donnees:
        print(colonne)
        print(statistiques_descriptives(donnees[colonne]))

    # Tests d'hypothèses
    # ttest_ind_from_stats en cas d'indépendance
    print(
        "Test d'hypothèse avec les températures. p-value :",
        stats.ttest_rel(
            donnees["temp_moyenne_2022"], donnees["temp_moyenne_2023"]
        ).pvalue,
    )
    print(
        "Test d'hypothèse avec la neige au sol. p-value :",
        stats.ttest_rel(
            donnees["neige_au_sol_2022"], donnees["neige_au_sol_2023"]
        ).pvalue,
    )

    # Intervalle de confiance
    print(
        "Intervalle de confiance de la température en 2023 :",
        intervalle_confiance(donnees["temp_moyenne_2023"]),
    )

    # Calcul de la corrélation
    print(
        "Corrélation entre la température et la neige : ",
        np.corrcoef(
            calculer_variation(donnees["temp_moyenne_2022"]),
            calculer_variation(donnees["neige_au_sol_2022"]),
        ),
    )

    # Histogramme
    # Par stats


if __name__ == "__main__":
    main()
