#Ecosystème
import random
a1 = "animal1"
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
    print(row)

# niveau 2

def create_ecosystem(n):
    return [[random.randint(1,3) for i in range(n)] for j in range(n)]

food_chain = {
    1: 2,
    2: 3,
    3: 1
}

def get_neighbors(ecosystem, x, y):
    neighbors = []
    n = len(ecosystem)
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if 0 <= i < n and 0 <= j < n and (i != x or j != y):
                neighbors.append(ecosystem[i][j])
    return neighbors

