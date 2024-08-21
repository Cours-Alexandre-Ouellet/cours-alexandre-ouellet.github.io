import locale
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import scipy.stats as stats


def lire_donnees(nom_fichier):
    """Lit la feuille nommée "données" dans un fichier excel

    keywords arguments:
    nom_fichier -- le nom du fichier qui contient les données
    """
    # https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
    donnees = pd.read_excel(
        nom_fichier,
        sheet_name="donnees",
        header=0,
        decimal=",",
        # thousands
    )

    return donnees


def nettoyer_donnees(donnees):
    """Nettoie les données en retirant les non disponibles

    keywords arguments:
    donnees -- un dataframe de données à nettoyer
    """
    # Option de retirer les doublons
    # donnees = donnees.drop_duplicates()

    # Option de supprimer les lignes avec NaN
    donnees = donnees.dropna(axis=0, how="any")

    # Option de supprimer une ligne
    donnees = donnees.drop(index=17, axis=0)

    for colonne in donnees:
        donnees[colonne] = donnees[colonne].astype("float")

    return donnees


def calculer_regression(donnees, variable_indep, variable_dep):
    """Calcule une régression linéaire entre deux colonnes et retourne les principales informations

    keywords arguments:
    donnees -- les données pour lesquelles calculer les régressions
    variable_indep -- nom de la colonne de la variable indépendante
    variable_dep -- nom de la colonne de la variable dépendante
    """
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html#scipy.stats.linregress
    regression = stats.linregress(
        donnees.loc[:, variable_indep], donnees.loc[:, variable_dep]
    )

    # Résultat de la régression
    print(regression)

    # On fait du ménage et on conserve que ce qui est utile
    return {
        "pente": regression.slope,
        "ordonnee_origine": regression.intercept,  # La bibliothèque ne permet pas de la forcer à 0 :(
        "coefficient_determination": regression.rvalue**2,
    }


def definir_graphique(max_x, max_y, titre, titre_axe_x, titre_axe_y):
    """Défini un nouveau graphique avec les paramètres indiqués

    keywords arguments:
    max_x -- plus grande valeur de l'axe des X
    max_y -- plus grande valeur de l'axe des Y
    titre -- titre donné au graphique
    titre_axe_x -- titre de l'axe des x
    titre_axe_y -- titre de l'axe des y
    """
    graphique, axes = plt.subplots()
    axes.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.4n}"))
    axes.yaxis.set_major_formatter(
        ticker.StrMethodFormatter("{x:.2n}")
    )  # n utilise le paramètre local de langue comme séparateur de décimale
    # https://docs.python.org/3/library/string.html#format-specification-mini-language

    # Paramètre du graphique
    axes.set_title(titre)

    # Paramètres des axes
    axes.set_xlim(0, 2)
    axes.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
    axes.set_xlabel(titre_axe_x)

    axes.set_ylim(0, 20)
    axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
    axes.set_ylabel(titre_axe_y)

    # Grille
    axes.grid(color="#bbb", linestyle="--", linewidth=0.5, which="major")
    axes.grid(color="#ddd", linestyle="dotted", linewidth=0.25, which="minor")

    return (graphique, axes)


def modeliser(axes, donnees, regression=None):
    """Ajouter les données sur un graphique existant

    keywords arguments:
    axes -- l'axe du graphique sur lequel ajouter les données
    valeurs_x -- les valeurs des points sur l'axe des X
    valeurs_y -- les valeurs des points sur l'axe des Y
    regression -- les données de la régression utilsée
    """
    axes.plot(
        donnees["temps"],
        donnees["vitesse"],
        linestyle="None",
        marker=".",
        markersize=10,
        clip_on=False,
        c="#00f",
    )
    axes.errorbar(
        donnees["temps"],
        donnees["vitesse"],
        linestyle="None",
        xerr=donnees["incertitude_temps"],
        yerr=(
            donnees["incertitude_vitesse_negative"],
            donnees["incertitude_vitesse_positive"],
        ),
        c="#000",
    )

    # Affiche la régression seulement is elle est définie
    if regression:
        axes.plot(
            [0, 5.5],
            [
                regression["ordonnee_origine"],
                regression["pente"] * 5.5 + regression["ordonnee_origine"],
            ],
            linewidth=0.5,
            color="k",
        )

        axes.text(
            4,
            0.2,
            f'{formatter_equation_regression(regression)}\n$R^2$ = {regression["coefficient_determination"]:.4n}',
        )

    plt.show()


def formatter_equation_regression(regression):
    """Formatte une équation de regression linéaire. Utilise la notation tex pour afficher les symboles.

    Keywords arguments:
    regression -- le dictionnaire qui contient les données de régression
    """
    pente = f'{regression["pente"]:.3n}x'
    ordonnee_origine = f'{abs(regression["ordonnee_origine"]):.3n}'
    symbole = "+" if regression["ordonnee_origine"] > 0 else "-"

    return f"${pente} {symbole} {ordonnee_origine}$"


def main():
    """Fonction principale du programme"""
    nom_fichier = "C:\\Projets\\notes-cours\\python-intro\\docs\\fichiers\\code\\donnees_physique.xlsx"
    donnees = lire_donnees(nom_fichier)

    print("Données avant nettoyage\n" + str(donnees))
    donnees = nettoyer_donnees(donnees)
    print("Données après nettoyage\n" + str(donnees))
    print(donnees.dtypes)
    regression = calculer_regression(donnees, "temps", "vitesse")
    print(regression)

    # Défini un graphique
    graphiques, axes = definir_graphique(
        max(donnees["temps"]) + 0.5,
        max(donnees["vitesse"]) + 0.1,
        "Vitesse de chute d'un objet",
        "Temps (s)",
        "Vitesse (m/s)",
    )
    modeliser(axes, donnees)


if __name__ == "__main__":
    locale.setlocale(
        locale.LC_ALL, "fr_CA"
    )  # Paramètre de langue locale français Canada. Utilise des , pour les décimales
    main()
