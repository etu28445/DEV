file = open("mon_fichier.txt")
file2 = open("result.txt", "w")

for line in file:
    file2.write(line.replace(" ", "   "))

file.close()
file2.close()