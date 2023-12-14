# exo 01

dicoVilles = {13: "Marseille", 34: "Montpellier", 44: "Nantes", 75: "Paris"}
print("--------------exo 01 ----------------")
for key in dicoVilles.keys():
    print(f"Les clés : {key}, Les valeurs :  {dicoVilles[key]}")
print("La taille du dico", len(dicoVilles))


# exo 02
def func_exo2(v: []):
    p1 = len(v[0])
    p2 = len(v[1])
    dicoList2 = {v[0]: p1, v[1]: p2}
    print("--------------exo 02 ----------------")
    print(dicoList2)


func_exo2(["coucou", "hi"])

print("--------------exo 03 ----------------")
# exo 03
def func_exo3(v: []):
    dicoList3 = {}
    for essai in v:
        print(essai, v.count(essai))
        dicoList3.update({essai: v.count(essai)})


    print("La liste", v)
    print(dicoList3)


func_exo3(["Ananas", "Banane", "Orange", "Ananas", "Banane"])
