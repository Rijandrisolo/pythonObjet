class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population

    def __str__(self):
        return "La ville est "+self.nom +", avec "+ str(self.population)+" d'habitants"

    def __repr__(self):
        return "Ville(nom='{}', population='{}')".format(self.nom, self.population)

ville01 = Ville(nom="Montpellier", population=500000)
print(str(ville01))
print(repr(ville01))


