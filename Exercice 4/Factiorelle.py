n = int(input("Entrez un nombre à factorialiser :"))
type = input("Saisir une boucle for ou while")
if type == "for":
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        print(fact)
    print("{}! = {}".format(n, fact))
elif type == "while":
    fact = 1
    nb = n
    while nb>= 1:
        fact = fact * nb
        nb = nb - 1
        print(fact)
    print("{}! = {}".format(n, fact))

