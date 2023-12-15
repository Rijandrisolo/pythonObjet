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


pers1 = Personne("Coco", 32)
pers2 = Personne("Coco", 32)
liste = {pers1, pers2}
for list in liste:
    print(list)
