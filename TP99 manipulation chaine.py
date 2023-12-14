from entites import Salarie

chaine = "Durand;Marcel;2 523.5"
print("--------------la chaîne----------------")
print("la chaine est ", chaine)
print("--------------Premier caractère de la chaîne----------------")
premier_caractere = chaine[0]
print("Premier caractère: " + premier_caractere)
print("--------------Longueur de la chaîne----------------")
print("la longueur de la chaîne de caractère est de : ", len(chaine))
print("--------------L'index du premier ,----------------")
for car in chaine:
    if car == ";":
        print("L'index du premier ; est : ", chaine.index(car))
print("--------------Extraction chaine de caractère ,----------------")

index_debut = 0
index_fin = 8

print(chaine[index_debut:index_fin])


print("--------------Extraction nom----------------")
for car in chaine:
    if car == "D":
       index_deb = chaine.index(car)
    if car == "d":
       index_end = chaine.index(car)+1

nom = chaine[index_debut:index_end]

print( "le nom extrait : ", nom)

print("le nom extrait en majuscule: ", nom.upper())
print("le nom extrait en minuscule: ", nom.lower())

print("--------------Split----------------")

mots = chaine.split(";")
nom = mots[0]
prenom = mots[1]
chiffre = mots[2]
chiffre = chiffre.replace(" ", "")
chiffre = float(chiffre)
print(nom, prenom, chiffre)
liste=[{nom, prenom, chiffre}]
print("Chiffre est de : ", type(chiffre))
print(liste)
sal = Salarie(nom, prenom, chiffre)


