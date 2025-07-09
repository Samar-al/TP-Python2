#soit la liste d'élèves suivante
eleves = [
    "Thomas", "Bertrand", "Marie", "Etienne", "Jean", "Arnaud", "Bertrand", "Xavier", "Martin", "Jeanne",
    "David", "Rodolphe", "Genevieve", "Pierre", "Karim", "Ines", "Adrien", "Magalie", "Romaric", "Antoine",
    "Karim", "Ines", "Adrien", "Sofia", "Mehdi", "Clara", "Julien", "Amira", "Lucas", "Sarah", "Nicolas",
    "Leïla", "Thomas", "Amina", "Hugo", "Lina", "Yassine", "Emma", "Maxime", "Nawel", "Romain", "Chloé",
    "Antoine", "Samira", "Bastien", "Lila", "Quentin", "Jade", "Yanis", "Camille", "Alexandre", "Hana",
    "Théo", "Myriam", "Enzo", "Salma", "Victor", "Zoé", "Ayoub", "Manon"
]

# compte le nombre d'élèves
# en utilisant filter, crée un liste avec les élèves dont le prénom contient un a
# en utilisant filter, crée un liste avec les élèves dont le prénom contient plus de 7 caractère
# en utilisant filter, crée un liste avec les élèves dont le prénom fini par un d

student_count = len(eleves)
print(f"Student count : {student_count}")

names_with_a = list(filter(lambda eleve: 'a' in eleve.lower(), eleves))
print("\nPrénoms contenant 'a' :")
for name in names_with_a:
    print("-", name)

more_than_7 = list(filter(lambda eleve: len(eleve) > 7, eleves))
print("\nPrénoms de plus de 7 caractères :")
for name in more_than_7:
    print("-", name)

ends_with_d = list(filter(lambda eleve: eleve.lower().endswith('d'), eleves))
print("\nPrénoms finissant par la lettre 'd' :")
for name in ends_with_d:
    print("-", name)