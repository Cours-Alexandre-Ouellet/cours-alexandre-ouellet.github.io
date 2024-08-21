import geometrie as geo

def saisir_point():
    """Demande une coordonnée en 2 dimension et retourne le tuple (X, Y)."""
    print("Entrez la coordonnée en X du point.")
    x = float(input())
    
    print("Entrez la coordonnée en Y du point.")
    y = float(input())
    
    return (x, y)


def info_carree():
    """Demande deux points consécutifs d'un carré puis retourne un dictionnaire d'informations sur le carré saisi."""
    print("Entrez un des coins du carré.")
    p0 = saisir_point()
     
    print("Entrez un coin adjancent au précédent.")
    p1 = saisir_point()
     
    return {"forme" : "carré",
            "aire" : geo.aire_carre(p0, p1),
            "périmètre" : geo.perimetre_carre(p0, p1)}


def info_rectangle():
    """Demande trois points consécutifs d'un rectangle puis retourne un dictionnaire d'informations sur le carré saisi."""
    print("Entrez un des coins du carré.")
    p0 = saisir_point()
     
    print("Entrez un coin adjancent au précédent.")
    p1 = saisir_point()
    
    print("Entrez un coin adjancent au précédent (opposé au premier).")
    p2 = saisir_point()
     
    return {"forme" : "rectangle",
            "aire" : geo.aire_rectangle(p0, p1, p2),
            "périmètre" : geo.perimetre_rectangle(p0, p1, p2)}


def info_cercle():
    """Demande le centre et un point sur la circonférence d'un disque et retourne un dictionnaire d'informations sur le disque
    saisie.
    """
    print("Entrez le centre du disque.")
    centre = saisir_point()
     
    print("Entrez un point sur la circonférence du disque.")
    point = saisir_point()
        
    return {"forme" : "disque",
            "rayon" : geo.distance(centre, point),
            "aire" : geo.aire_disque(centre, point),
            "circonférence" : geo.circonférence_disque(centre, point)}



def main():
    """Menu principal du programme"""
    continuer = True
    
    while continuer:
        print("Pour quelle forme souhaitez-vous obtenir les informations\n1) Carré\n2) Rectangle\n3) Cercle\n0) Quitter")
        choix = int(input())
        
        if choix == 0:
            continuer = False
        elif choix == 1:
            print(info_carree())
        elif choix == 2:
            print(info_rectangle())
        elif choix == 3:
            print(info_cercle())
        else:
            print("La valeur n'est pas valide")

if __name__ == "__main__":
    main()