# soit la liste suivante
from functools import reduce

taux_interets = [1.2, 1.4, 2.5, 3.6, 4.7, 1.8, 2.9, 2.0]
# qui représente les taux d'intérets fictifs pour un dépot de 1000€ en banque
# utilisez l'opérateur reduce avec une lambda pour calculer le montant de ces 1000€ après ces 8 années

montant_initial = 1000

montant_final = reduce(lambda acc, taux: acc * (1 + taux / 100), taux_interets, montant_initial)

print(f"Montant final après 8 ans : {montant_final:.2f} €")