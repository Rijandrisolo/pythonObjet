class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population

    def __str__(self):
        return self.nom

    def __repr__(self):
        return "Ville(nom='{}', population='{}')".format(self.nom, self.population)


class AdressePostale:
    def __init__(self, num_rue: int, nom_rue: str, code_postal: str, ville: str):
        self.num_rue = num_rue
        self.nom_rue = nom_rue
        self.code_postal = code_postal
        self.ville = ville

    def __str__(self):
        return f"{self.num_rue} {self.nom_rue} {self.code_postal} {self.ville}"


class Personne:
    def __init__(self, nom: str, prenom: str, adresse: AdressePostale):
        self.prenom = prenom
        self.nom = nom
        self.adresse = adresse

    def __str__(self):
        return self.nom + " " + self.prenom + " " + self.adresse

    def majuscule(self):
        print("Je m'appelle " + self.nom.upper() + " " + self.prenom)

    def set_nom(self, nom: str):
        self.nom = nom

    def set_prenom(self, prenom: str):
        self.prenom = prenom

    def set_adresse(self, adresse: AdressePostale):
        self.adresse = adresse

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_adresse(self):
        return self.adresse

    def afficher(self):
        print(self.nom, self.prenom, self.adresse.num_rue, self.adresse.nom_rue, self.adresse.code_postal,
              self.adresse.ville)


ville01 = Ville(nom="Montpellier", population=500000)
ville02 = Ville(nom="Lyon", population=345000)

adresse01 = AdressePostale(1, "Cour Lou Terral", "34080", ville01)
adresse02 = AdressePostale(2, "Avenue des Lilas", "69000", ville02)

pers01 = Personne(nom="Dupont", prenom="André", adresse=adresse01)

print("la ville de : ", str(ville01))
print("La ville en repr : ", repr(ville02))
print("adresse01 : ", adresse01)
print("adresse02 : ",adresse02)

print(pers01.nom, pers01.prenom, pers01.adresse)
pers01.majuscule()
pers01.set_nom("Coco")
pers01.majuscule()
pers01.afficher()
