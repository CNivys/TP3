hdeb = 0
hfin = 0
j = 0
h = 0
phaut = 0
fin = False
while not fin:
    hdeb = int(input("Donnez l'heure de début de la location (un entier) : "))
    hfin = int(input("Donnez l'heure de fin de la location (un entier) : "))
    if hdeb == hfin:
        print(" Attention ! l’heure de fin est identique à l’heure de début.")
    elif hdeb > hfin:
        print("Attention ! le début de la location est après la fin ...")
    elif 0 <= hdeb < 24 and 0 <= hfin < 24:
        htotal = hfin - hdeb
        for i in range(htotal+1):
            if hdeb >= 7 and hdeb < 17:
                hdeb += 1
                j += 1
            else:
                h += 1
                hdeb = hdeb + 1
            ab = True
        if ab == True:
            h -= 1
            phaut += 2 * j
            ptotal = phaut + h
            print("Vous avez loué votre vélo pendant")
            print("{} heure(s) au tarif horaire de 1.0 euro(s)".format(h))
            print("{} heure(s) au tarif horaire de 2.0 euro(s)".format(j))
            print("Le montant total à payer est de {} euro(s).".format(ptotal))
            fin = True
    else:
        print("Les heures doivent être comprises entre 0 et 24 !")


