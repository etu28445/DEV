path = input("Entrer le nom de votre fichier : ")


choix = input("Voulez vous lire ou créer un nouveau fichier (Lire=r / Creer=a) : ")

if choix == 'a':
    file = open(path, choix)

    line = input("Entrer une nouvelle ligne : ")
    while line != "":
        file.write(line+"\n")
        line = input("Entrer une nouvelle ligne : ")


else:
    file = open(path, choix)
    for line in file:
        print(line, end='')
