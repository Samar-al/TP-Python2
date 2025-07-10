#Ecosystème
import random
"""a1 = "animal1"
a2 = "animal2"
a3 = "animal3"

ecosystem = [[a1,a3,a2], [a1,a2,a1],[a3, a2, a1]]
prey = ecosystem[1][1]
food_chain = {
    a1: a2,
    a2: a3,
    a3: a1
}
predator = [key for key, value in food_chain.items() if value == prey][0]
neighbors = [
    ecosystem[0][0], ecosystem[0][1], ecosystem[0][2],
    ecosystem[1][0],                  ecosystem[1][2],
    ecosystem[2][0], ecosystem[2][1], ecosystem[2][2]
]

predators = neighbors.count(predator)
preys = neighbors.count(food_chain[prey])
others = 8 - preys - predators

if predators > max(preys, others):
    ecosystem[1][1] = predator
elif predators > 0 and preys > 0 and predators == preys:
    if random.random() < 0.5:
        ecosystem[1][1] = predator
elif predators > 0 and others > preys:
    ecosystem[1][1] = predator

for row in ecosystem:
    print(row)"""

# niveau 2
# je crée la grille de l'ecosysteme de taille où chaque case contient aléatoirement 1, 2 ou 3.
def create_ecosystem(n):
    return [[random.randint(1,3) for i in range(n)] for j in range(n)]
# je définis qui mange qui
food_chain = {
    1: 2,
    2: 3,
    3: 1
}

# je renvoi  les 8 voisins d'une cellule en position x et y, d'un ecosysteme que je fournis.
def get_neighbors(ecosystem, x, y):
    neighbors = []
    n = len(ecosystem)
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if 0 <= i < n and 0 <= j < n and (i != x or j != y):
                neighbors.append(ecosystem[i][j])
    return neighbors

#je mets à jour la cellule en fonction de sa valeur (l'animal), du nombre de prédateur et du nombre de proie qui l'entour.
def update_cell(value, neighbors, food_chain):
    predator = [k for k, v in food_chain.items() if v == value][0]
    prey = food_chain[value]
    count_predator = neighbors.count(predator)
    count_prey = neighbors.count(prey)
    others = len(neighbors) - count_predator - count_prey

    if count_predator > max(count_prey, others):
        return predator
    elif count_predator == count_prey and count_predator > 0:
        return predator if random.random() < 0.5 else value
    elif count_predator > 0 and others > count_prey:
        return predator
    else:
        return value
# je mets à jour toute l'ecosysteme.
def update_ecosystem(ecosystem, food_chain):
    n = len(ecosystem)
    new_ecosystem = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            neighbors = get_neighbors(ecosystem, i, j)
            new_ecosystem[i][j] = update_cell(ecosystem[i][j], neighbors, food_chain)
    return new_ecosystem

#test
n = 10
ecosystem = create_ecosystem(n)

print("Avant :")
for ligne in ecosystem:
    print(ligne)

ecosystem = update_ecosystem(ecosystem, food_chain)

print("\nAprès :")
for ligne in ecosystem:
    print(ligne)