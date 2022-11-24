i = 0
nb10 = 0
nb15 = 0
nb20 = 0
while i != 10:
    n = int(input("Saisir un nombre entre 0 20 : "))
    if 0 <= n <= 20 :
        i += 1
        if n < 10:
            nb10 += 1
        elif 10 <= n < 15 :
            nb15 += 1
        elif 15 <= n:
            nb20 += 1

    else:
        print("nombre non valide")

print("Le nombre de valeur inférieur à 10 est de : {}".format(nb10))
print("Le nombre de valeur comprise entre 10 et 15 est de : {}".format(nb15))
print("Le nombre de valeur supérieur à 15 est de : {}".format(nb20))