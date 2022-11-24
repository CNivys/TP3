n = int(input("Saisir un nombre : "))
i = 0
fin = False
tab = []
while not fin:
    i+=1
    tab.append(i)
    tab.sort(reverse=True)
    if i == n :
        break

print(tab)