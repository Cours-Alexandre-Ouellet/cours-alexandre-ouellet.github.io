import time
import numpy as np 

def exectuer_fonction(liste, nombre_a_conserver, fonction):
    temps_depart = time.time_ns()
    fonction(liste, nombre_a_conserver)
    temps_fin = time.time_ns()

    return temps_fin - temps_depart

def approche1(liste, nombre_a_conserver):
    resultat = liste[nombre_a_conserver::-1]
    return resultat
    
def approche2(liste, nombre_a_conserver):
    resultat = liste[:nombre_a_conserver][::-1]
    return resultat

def approche3(liste, nombre_a_conserver):
    resultat = []
    for i in range(nombre_a_conserver, -1, -1):
        resultat.append(liste[i])
    return resultat

def tester_approches(nombre_repetitions, taille, nombre_a_conserver, approches):
    resultats = {}  
    liste = np.random.rand(taille)
    
    for approche in range(len(approches)) :
        resultat_configuration = []

        for _ in range(nombre_repetitions):
            resultat_configuration.append(exectuer_fonction(liste, nombre_a_conserver, approches[approche]))

        configuration = "Approche " + str(approche + 1)
        resultats[configuration] = resultat_configuration

    return resultats

def decrire(resultats):
    description = {}
    for identifiant, resultats_bruts in resultats.items():
        description[identifiant] = {
            "n" : len(resultats_bruts),
            "moyenne" : np.mean(resultats_bruts),
            "écart-type" : np.std(resultats_bruts),
            "minimum" : np.min(resultats_bruts),
            "maximum" : np.max(resultats_bruts),
        }
    return description

def main():
    nombre_repetition = 50          # Nombre fois que l'on effectue le test
    taille = 10000000               # Taille de la liste
    nombre_a_conserver = 700000     # Nombre d'éléments à conserver
    approches = [approche1, approche2, approche3]

    resultats = tester_approches(nombre_repetition, taille, nombre_a_conserver, approches)
    print(resultats["Approche 1"])

    stat_descriptives = decrire(resultats)
    print(stat_descriptives)

if __name__ == "__main__":
    main()
