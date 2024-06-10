# Salut Copilot ! Peux-tu générer un code python qui permet de faire l'analyse du mouvement rectiligne uniformément accéléré (MRUA) pour n'importe quels paramètres. L'analyse doit indiquer les points où l'objet est au repos et s'il revient sur sa position de départ. Aussi, le code doit présenter des évaluations de la position pour un intervalle de temps donné avec une fréquence d'échantillion donnée en paramètres. Utilise seulement la bibliothèque numpy comme dépendance externe.

from numpy.polynomial import Polynomial
import numpy as np

def retirer_valeurs_negatives(liste):
    """Retourne une liste contenant que les éléments non négatif de la liste

    Keywords arguments:
    liste -- la liste de laquelle retirer les valeurs négatives
    """
    indices_valeurs_negatives = []
    for i in range(len(liste)):
        if liste[i] < 0:
            indices_valeurs_negatives.append(i)
    
    liste = np.delete(liste, indices_valeurs_negatives)
        
    return liste

def mouvement_uniformement_accelere(position_depart, vitesse_initiale, acceleration, temps_observe = 10, intervalle = 1):
    """Calcule à partir de l'équation du mouvement rectiligne uniformément accéléré la position\
    d'un objet après un temps écoulé. Extrait diverses informations sur le déplacement
    
    Keywords arguments:
    position_depart -- la position de départ 
    vitesse_initiale -- la vitesse de l'objet au début de l'observation
    acceleration -- l'accélération appliquée sur l'objet
    temps_observe -- durée de l'observation
    intervalle -- la différence de temps entre les observations
    """
    # Équation du MRUA : x_0 + v_i * t + 0.5 * a * t**2
    position_temps = Polynomial([position_depart, vitesse_initiale, 0.5 * acceleration])
    
    # Calcule la progression dans le temps du mouvement
    positions = {}
    for t in range(0, temps_observe + intervalle, intervalle):
        positions[t] = position_temps(t)
    
    # Détermine quand l'objet revient a sa position initiale
    temps_position_initiale = (position_temps - Polynomial(position_depart)).roots()
    temps_position_initiale = retirer_valeurs_negatives(temps_position_initiale)

    # Détermine quand la vitesse est nulle
    variation_vitesse = position_temps.deriv()
    vitesse_nulle = variation_vitesse.roots()
    vitesse_nulle = retirer_valeurs_negatives(vitesse_nulle)
    
    return {
        'equation' : str(position_temps),
        'positions' : positions,
        'retour position initiale' : list(temps_position_initiale),
        'vitesse nulle' : list(vitesse_nulle)
    }
    
def main():
    info_mouvement= mouvement_uniformement_accelere(5, 6, 2)
    print(info_mouvement)
    
if __name__ == "__main__":
    main()