import main

def display_chessboard_grains():
    grain = 1
    total = 0
    exponent = 0

    format_number = lambda n: f"{n:>22,}"
    format_scientific = lambda n: f"{n: .2e}"

    for row in range(1, 9):
        for col in range(1, 9):
            print(f"Ligne {row}, Colonne {col} : 2^{exponent:<2} = {format_number(grain)} grain(s)")
            total += grain
            grain *= 2
            exponent += 1
    print("\nTotal de grains de riz sur l’échiquier :", format_number(total))
    print("Ce qui équivaut à environ :", format_scientific(total), "grains")

display_chessboard_grains()