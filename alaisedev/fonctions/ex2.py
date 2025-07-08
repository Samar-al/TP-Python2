# créez une fonction qui prend en paramètre une suite de longueur indéterminée de int
# et qui renvoi la valeur en bit de la multiplication de ceux ci

def multiply_in_bits(*args):
    if not args:
        return "0"

    product = 1
    for arg in args:
        product *= arg

    binary = bin(product)[2:]
    print(product, binary, end=' ')
    return binary

multiply_in_bits(56, 76, 2, 5)
multiply_in_bits(2,3,4)