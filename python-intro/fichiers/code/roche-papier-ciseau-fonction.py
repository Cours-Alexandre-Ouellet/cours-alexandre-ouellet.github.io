def saisir_symbole(numero_joueur):
    """Permet la saisie par une personne du symbole à jouer.

    Keywords arguments:
    numero_joueur -- le numéro du joueur qui saisie son symbole à jouer
    """
    print("Symbole de la personne " + str(numero_joueur) + " (1 = roche, 2 = papier, 3 = ciseau)")
    return int(input())


def tour():
    """Réalise un tour du jeu du roche-papier-ciseau. Retourne le numéro de la personne gagnante
    ou la valeur 0 si personne n'a gagné.
    """
    symbole1 = saisir_symbole(1)
    symbole2 = saisir_symbole(2)
    
    if symbole1 == symbole2:
        return 0
    elif symbole2 % 3 == symbole1 - 1:
        return 1
    else:
        return 2


def main():
    """Fonction principale du jeu"""
    vainqueur = False
    
    # On recommence la saisie tant qu'il n'y a pas de vainqueur
    while not vainqueur:
        resultat = tour()
        
        if resultat == 0:
            print("Il y a égalité, on recommence !")
        else:
            vainqueur = True
        
    print("La personne " + str(resultat) + " a gagné !")
    
    
if __name__ == "__main__":
    main()
