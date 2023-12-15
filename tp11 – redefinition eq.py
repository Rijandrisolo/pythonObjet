class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Personne):
            return self.nom == other.nom and self.age == other.age
        return False


pers1 = Personne("Coco", 32)
pers2 = Personne("Coco", 32)

resultat_apres_redefinition = pers1 == pers2
print(f"Après redéfinition: Les instances sont-elles égales? {resultat_apres_redefinition}")
