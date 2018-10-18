dico={}
dico["computer"] = "ordinateur"
dico["mouse"] ="souris"
dico["keyboard"] ="clavier"
print(dico)
invent ={"pommes": 430, "bananes": 312, "oranges" : 274, "poires": 137}
print(invent)
del invent["pommes"]
print(invent)
print(len(invent))
if "pommes" in invent:
    print("Nous avons des pommes")
else:
    print("Pas de pommes. Sorry")
    print('\n'); print(dico.keys())
for k in dico.keys():
    print("cle :", k, "−−−valeur : ", dico[k])
for k in dico:
    print("cle :", k, "−−−valeur : ", dico[k])
for clef, valeur in dico.items():
    print(clef, valeur)
    print('\n')
    print(list(dico.keys()))
    print(tuple(dico.keys()))
    print(dico.items())
    print(list(dico.items()))
    print('\n')
arb ={}
arb[(1,2)] = "Peuplier"
arb[(3,4)] = "Platane"
arb[6,5] = "Palmier"
arb[5,1] = "Cycas"
arb[7,3] = "Sapin"
print(arb)
print(arb[(6,5)])