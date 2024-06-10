def main():
    print("Symbole de la personne 1 (1 = roche, 2 = papier, 3 = ciseau)")
    symbole1 = int(input())
    
    print("Symbole de la personne 2 (1 = roche, 2 = papier, 3 = ciseau)")
    symbole2 = int(input())
    
    if symbole1 == symbole2:
        print("Égalité")
    elif symbole2 % 3 == symbole1 - 1:
        print("Personne 1 gagne")
    else:
        print("Personne 2 gagne")
        
if __name__ == "__main__":
    main()
