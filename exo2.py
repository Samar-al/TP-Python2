import main
def primary_numbers(limit):
    primes = []

    for number in range(2, limit + 1):
        is_premier = True
        for diviseur in range(2, int(number ** 0.5) + 1):
            if number % diviseur == 0:
                is_premier = False
                break
        if is_premier:
            primes.append(number)

    print(f"\nNombre total de nombres premiers trouvés : {len(primes)}")
    return primes

primes = primary_numbers(7919)
print("\nListe des nombres premiers :")
print(primes)
