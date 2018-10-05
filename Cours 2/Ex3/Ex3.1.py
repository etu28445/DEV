path = "mon_fichier.txt"

file = open(path, 'w')

file.write("Yo la famille !\n")

for i in range(1, 5):
    file.write("Ceci est la ligne " + str(i) + "\n")

file.close()

file = open(path)

for line in file:
    print(line, end='')

file.close()