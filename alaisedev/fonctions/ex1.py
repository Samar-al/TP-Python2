# Pour un logiciel de gestion rh d'une agence d'interim
# complétez la fonction suivante sui calcule le salaire journalier
# d'un intérimaire
# après 8 heures de travail, les heures sont majorées de 25%, après 11heures de 50%

def calcul_salaire_journalier(nb_heures, salaire_horaire):
    salary = 0
    sup_hours = 0
    if nb_heures <= 8:
        salary =  nb_heures * salaire_horaire
    else:
        salary = 8 * salaire_horaire
        sup_hours = nb_heures - 8
        if sup_hours <= 3:
            salary += sup_hours * salaire_horaire * 1.25
        else:
            salary += 3 * salaire_horaire * 1.25
            salary += (sup_hours - 3) * salaire_horaire * 1.5
    print(f"salaire : {salary} € par jour", f"heures-sup: {sup_hours} heure(s)")
    return salary


calcul_salaire_journalier(9, 12)
