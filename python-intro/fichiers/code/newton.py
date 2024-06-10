x = -5500.0			# Point de la solution
ecart = 1.0		# Écart entre les deux dernières solutions

while ecart > 0.0001 or ecart < -0.0001:
    # ecart verifie l'avancement vers la solution
    fonction = x**3-3*x**2+4*x-4
    derivee = 3*x**2-6*x+4
    
    # Gere les erreurs de division par 0
    if(derivee == 0.0):
        ecart = 0
        print("Division par 0. Impossible d'evaluer avec la valeur intiale " + str(x))
    else:
        terme = x - fonction / derivee
        # Calcule la différence entre les deux derniere solution
        ecart = terme - x
        # Le changement de x par la nouvelle valeur (terme) prepare pour la prochaine iteration
        x = terme
    
print(str(x))

# La seule racine réelle est 2