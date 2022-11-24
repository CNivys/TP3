x = int(input("Saisir un nombre : "))
n = 0
fin = False
i = 0
while not fin:
    i += 1
    n += i
    if n > x:
        break

print("Le nombre recherché est {}".format(i-1))