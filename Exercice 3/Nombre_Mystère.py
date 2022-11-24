import random

n = random.randint(0, 100)
i = 0
fin = False
while not fin:
    x = int(input("Saisir un nombre entre 0 et 100 : "))
    i+=1
    if x > n :
        print("Le nombre est plus petit")
    elif n > x:
        print("Le nombre est plus grand")
    else:
        print("Le nombre {} a été trouvé en {} tentative".format(x, i))
        break