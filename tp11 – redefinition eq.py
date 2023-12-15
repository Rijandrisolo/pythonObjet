class Personne:
   def __init__(self, nom, age):
        self.nom = nom
        self.age = age


   def __eq__(self, other):
        if isinstance(other, Personne):
            return self.nom == other.nom and self.age == other.age
        return False


personne1 = Personne("Coco", 32)
personne2 = Personne("Coco", 32)


resultat_apres_redefinition = personne1 == personne2
print(f"Après redéfinition: Les instances sont-elles égales? {resultat_apres_redefinition}")