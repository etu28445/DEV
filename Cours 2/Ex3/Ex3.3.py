path = "TableDeMultiplication.txt"
file = open(path, 'w')

base = range(1, 21)

for i in range(2, 31):
    list = [i * j for j in base]
    file.write(" ".join(str(j) for j in list) + "\n")

file.close()

