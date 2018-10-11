fileA = open("fileA.txt")
fileB = open("fileB.txt")
fileC = open("fileC.txt", "w")

for lineA, lineB in zip(fileA, fileB):
    fileC.write(lineA)
    fileC.write(lineB)


fileA.close()
fileB.close()
fileC.close()