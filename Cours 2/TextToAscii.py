phrase = input("Entrer votre phrase ici : ")
letter = phrase.split()

for letter in phrase:
    print(ord(letter), end=' ')
