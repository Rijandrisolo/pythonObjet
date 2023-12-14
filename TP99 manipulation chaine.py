chaine = "Durand;Marcel;2 523.5"
print("la chaine est ", chaine)
premier_caractere = chaine[0]
print("Premier caractère: " + premier_caractere)
print("la longueur de la chaîne de caractère est de : ", len(chaine))
for car in chaine:
    if car == ";":
        print("L'index du premier ; est : ", chaine.index(car))
