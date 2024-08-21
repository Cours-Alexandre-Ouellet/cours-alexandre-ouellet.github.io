import sympy as sym
import sympy.calculus.util as utils


def appliquer_methode_numerique(
    fonction,
    borne_inferieure,
    borne_superieure,
    nombre_echantillons,
    hauteur_intervalle,
):
    """Applique une méthode d'intégration numérique sur une fonction

    keywords arguments:
    fonction -- la fonction à intégrer
    borne_inferieure -- la borne inférieure de l'intervalle à intégrer
    borne_supérieure -- la borne supérieure de l'intervalle à intégrer
    nombre_echantillons -- le nombre de division de l'intervalle d'intégration
    hauteur_intervalle -- une fonction qui retourne une hauteur prise sur l'intervalle
    """
    pas = (borne_superieure - borne_inferieure) / nombre_echantillons
    min_intervalle = borne_inferieure
    max_intervalle = borne_inferieure + pas
    valeur_integrale = 0.0

    # Applique la méthode de collecte sur chaque intervalle
    for i in range(nombre_echantillons):
        intervalle = sym.Interval(min_intervalle, max_intervalle)
        hauteur = hauteur_intervalle(fonction, intervalle)
        valeur_integrale += hauteur * pas

        # Mise à jour de l'intervalle
        min_intervalle = max_intervalle
        max_intervalle = min_intervalle + pas

    return valeur_integrale


def integration_numerique_rectangles_inscrits(
    fonction, borne_inferieure, borne_superieure, nombre_echantillons
):
    return appliquer_methode_numerique(
        fonction,
        borne_inferieure,
        borne_superieure,
        nombre_echantillons,
        calculer_point_minimum,
    )


def calculer_point_minimum(fonction, intervalle):
    """Calcule le point minimal d'une fonction sur un intervalle

    keywords arguments:
    fonction -- la fonction sur laquelle calculer le minimum
    intervalle -- l'intervalle sur lequel calculer le minimum
    """
    return utils.minimum(fonction, sym.Symbol("x"), domain=intervalle).evalf(8)


def calculer_point_milieu(fonction, intervalle):
    """Calcule le point milieu d'une fonction sur un intervalle

    keywords arguments:
    fonction -- la fonction sur laquelle calculer le point milieu
    intervalle -- l'intervalle sur lequel calculer le point milieu
    """
    return fonction.subs("x", (intervalle.start + intervalle.end) * 0.5).evalf(8)


def calculer_point_maximum(fonction, intervalle):
    """Calcule le point maximal d'une fonction sur un intervalle

    keywords arguments:
    fonction -- la fonction sur laquelle calculer le maximum
    intervalle -- l'intervalle sur lequel calculer le maximum
    """
    return utils.maximum(fonction, sym.Symbol("x"), domain=intervalle).evalf(8)


def calculer_hateur_trapeze(fonction, intervalle):
    """Calcule la "hauteur" d'un trapèze sur un intervalle. Correspond à la moitié de la grande base additionnée à la petite base.

    keywords arguments:
    fonction -- la fonction sur laquelle calculer la hauteur du trapèze
    intervalle -- l'intervalle sur lequel calculer la hauteur du trapèze
    """
    maximum = utils.maximum(fonction, sym.Symbol("x"), domain=intervalle)
    minimum = utils.minimum(fonction, sym.Symbol("x"), domain=intervalle)

    return 0.5 * (maximum + minimum).evalf(8)


def integration_exacte(fonction, borne_inferieure, borne_superieure):
    """Calcule l'intégrale exacte de la fonction entre deux bornes définies

    keywords arguments:
    fonction -- la fonction à intégrer
    borne_inferieure -- la borne inférieure de l'intervalle à intégrer
    borne_supérieure -- la borne supérieure de l'intervalle à intégrer
    """
    integrale = sym.integrate(fonction, ("x", borne_inferieure, borne_superieure))
    return integrale.evalf(8)


def main():
    """Fonction principale du programme. Elle définie les paramètres puis retourne les différentes valeurs d'intégration."""
    # Paramètres de la recherche
    borne_inferieure = 1
    borne_superieure = 4
    nombre_echantillons = 20

    # Fonction étudiée
    x = sym.Symbol("x")
    fonction = x**3 * sym.ln(x / 2)
    
    integrale = sym.integrate(fonction)
    print(integrale)

    integrations = {
        "rect inscrits": appliquer_methode_numerique(
            fonction,
            borne_inferieure,
            borne_superieure,
            nombre_echantillons,
            calculer_point_minimum,
        ),
        "rect milieu": appliquer_methode_numerique(
            fonction,
            borne_inferieure,
            borne_superieure,
            nombre_echantillons,
            calculer_point_milieu,
        ),
        "rect circonscrits": appliquer_methode_numerique(
            fonction,
            borne_inferieure,
            borne_superieure,
            nombre_echantillons,
            calculer_point_maximum,
        ),
        "trapeze": appliquer_methode_numerique(
            fonction,
            borne_inferieure,
            borne_superieure,
            nombre_echantillons,
            calculer_hateur_trapeze,
        ),
        "valeur exacte": integration_exacte(
            fonction, borne_inferieure, borne_superieure
        ),
    }

    print(integrations)


if __name__ == "__main__":
    main()
