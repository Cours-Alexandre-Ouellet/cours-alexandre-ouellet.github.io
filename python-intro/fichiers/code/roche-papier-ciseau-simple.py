def main():
    print("Symbole de la personne 1 (1 = roche, 2 = papier, 3 = ciseau)")
    symbole1 = int(input())
    
    print("Symbole de la personne 2 (1 = roche, 2 = papier, 3 = ciseau)")
    symbole2 = int(input())
    
    if symbole1 == symbole2:
        print("Égalité")
    elif (symbole1 == 2 and symbole2 == 1) or (symbole1 == 3 and symbole2 == 2) or (symbole1 == 1 and symbole2 == 3):
        print("Personne 1 gagne")
    else:
        print("Personne 2 gagne")
        
if __name__ == "__main__":
    main()