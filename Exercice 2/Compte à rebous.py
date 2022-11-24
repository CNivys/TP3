n = int(input("Saisir un nombre"))
tab = []
for i in range(n+1):
    tab.append(i)
    tab.sort(reverse=True)

print(tab)