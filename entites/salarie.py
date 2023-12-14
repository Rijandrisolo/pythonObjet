class Salarie:
    def __init__(self, nom: str, prenom: str, salaire: float):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def __str__(self):
        return f" Nom : {self.nom} Prénom : {self.nom} Salaire : {self.salaire}"

    def __repr__(self):
        return f" Nom : {self.nom} Prénom : {self.nom} Salaire : {self.salaire}"
