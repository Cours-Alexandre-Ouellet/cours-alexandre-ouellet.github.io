def main():
    # Saisie des informations
    print("Entrez le premier nombre a multiplier :")
    operande_gauche = int(input())

    print("Entrez le second nombre a multiplier :")
    operande_droite = int(input())

    # Calcul et affichage
    produit = operande_gauche * operande_droite
    print("Le produit est : " + str(produit))

if __name__ == "__main__":
    main()