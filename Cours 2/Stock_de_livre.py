class Livre:
    titre = "L'autre"
    prenom_auteur = "Jean-Paul"
    nom_auteur = "Mercenier"
    nb_page = 400
    date_sortie = "10 mai 2001"
    prix = 65

livre1 = Livre()
livre2 = Livre()

livre2.titre = "Le Suivant"
livre2.nb_page = 320
livre2.prix = 80

if max(livre1.prix, livre2.prix) == livre1.prix:
    print("Le livre le plus cher est : ", livre1.titre)
else:
    print("Le livre le plus cher est : ", livre2.titre)

livre1.prix = livre2.prix

if livre1.prix > 70:
    livre1.prix = (livre1.prix / 2) + 10
    print("Le prix étant suppérieur à 70 euros, vous bénéficier d'une promo !")
    print("Le prix est donc maintenant de : ", livre1.prix)
else:
    print("Le prix n'a pas changé !")

livre1.date_sortie_1 = livre1.date_sortie.split()
print(livre1.date_sortie_1[2])
print("\nEn ", livre1.date_sortie_1[2], livre1.prenom_auteur, livre1.nom_auteur, "à sorti le livre \"", livre1.titre, "\"")

