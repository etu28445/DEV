text = input("Entrer votre chaine ici : ")
longueur = len(text)
c = 0
d = 0
while c < longueur:
   charactere = text[c]
   if (charactere == "e"):
       print("ok")
       d += 1
   c += 1
print(d)