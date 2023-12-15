class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f" Personne  : {self.nom} - âge: {self.age} "

    def __repr__(self):
        return f" Personne  : {self.nom} - âge: {self.age} "

    def __eq__(self, other):
        if isinstance(other, Personne):
            return self.nom == other.nom and self.age == other.age
        return False

    def __hash__(self):
        return hash((self.nom, self.age))

    def __lt__(self, other):
        return self.nom < other.nom


pers1 = Personne("Coco", 32)
pers2 = Personne("Toto", 25)
pers3 = Personne("Jaco", 45)
liste = [pers1, pers2, pers3]
def tri_age(personne):
    return personne.age
def tri_nom(personne):
    return personne.nom


tri_liste = sorted(liste, key=tri_age)
for liste in tri_liste:
    print(liste)
