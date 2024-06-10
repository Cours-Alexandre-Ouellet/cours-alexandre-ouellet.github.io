from numpy import sqrt, pi

def distance(p0, p1):
    """Calcule la distance entre deux points (longueur d'un segment) et la retourne.

    Keywords arguments:
    p0 -- le premier point du segment.
    p1 -- le second point du segment.
    """
    return sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)


def aire_carre(p0, p1):
    """Calule l'aire d'un carré à partir de deux points consécutifs
    
    Keywords arguments:
    p0 -- un premier point du carré
    p1 -- un second point du carré, adjacent au premier
    """
    return distance(p0, p1)**2


def perimetre_carre(p0, p1):
    """Calule le périmètre d'un carré à partir de deux points consécutifs
    
    Keywords arguments:
    p0 -- un premier point du carré
    p1 -- un second point du carré, adjacent au premier
    """
    return 4.0 * distance(p0, p1)


def aire_rectangle(p0, p1, p2):
    """Calule l'aire d'un rectangle à partir de trois points consécutifs
    
    Keywords arguments:
    p0 -- un premier point du rectangle
    p1 -- un second point du reangle, adjacent au premier
    p2 -- un troisième point du reangle, adjacent au second et différent du premier
    """
    return distance(p0, p1)*distance(p1, p2)


def perimetre_rectangle(p0, p1, p2):
    """Calule le perimetre d'un rectangle à partir de trois points consécutifs
    
    Keywords arguments:
    p0 -- un premier point du rectangle
    p1 -- un second point du reangle, adjacent au premier
    p2 -- un troisième point du reangle, adjacent au second et différent du premier
    """
    return 2 * (distance(p0, p1) + distance(p1, p2))


def aire_disque(centre, p0):
    """Calule l'aire d'un disque à partir du centre et d'un point sur la circonférence
    
    Keywords arguments:
    centre -- le point au centre du disque
    p0 -- un point situé sur la circonférence
    """
    return distance(centre, p0)**2 * pi


def circonférence_disque(centre, p0):
    """Calule la circonférence d'un disque à partir du centre et d'un point sur la circonférence
    
    Keywords arguments:
    centre -- le point au centre du disque
    p0 -- un point situé sur la circonférence
    """
    return distance(centre, p0)* 2 * pi