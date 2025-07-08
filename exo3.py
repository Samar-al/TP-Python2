import main

grain = 1
total = 0
exponent = 0

for row in range(1, 9):
    for col in range(1, 9):
        print(f"Ligne {row}, Colonne {col} : 2^{exponent:<2} = {grain:>22,} grain(s)")
        total += grain
        grain *= 2
        exponent += 1
print("\nTotal de grains de riz sur l’échiquier :", total)
print(f"Ce qui équivaut à environ : {total:.2e} grains")