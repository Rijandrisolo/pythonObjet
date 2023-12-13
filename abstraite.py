from abc import ABC, abstractmethod

from encapsulation import Livre, LivreNumerique, LivrePapier


class Sortie(ABC):

    def __init__(self, date: str, livre):
        self.date = date
        self.livre = livre

    @abstractmethod
    def get_montant(self):
        pass

    def __str__(self):
        return f" date de l'emprunt : {self.date} \n livre : {self.livre}"


class Emprunt(Sortie):

    def __init__(self, date: str, livre, duree_emprunt: int):
        super().__init__(date, livre)
        self.duree_emprunt = duree_emprunt

    def __str__(self):
        return f"{super().__str__()} durée : {self.duree_emprunt} \n Coût de l'emprunt : {self.get_montant()}"

    def __repr__(self):
        return f"{super().__str__()} durée : {self.duree_emprunt} \n Coût de l'emprunt : {self.get_montant()} \n"

    def get_montant(self):
        prix_unit = 0
        # if type(self.livre) == LivrePapier:
        #     prix_unit = 0.5
        # elif type(self.livre) == LivreNumerique:
        #     prix_unit = 0.25

        prix_emprunt = self.duree_emprunt *self.livre.prix_unit
        return prix_emprunt


class Achat(Sortie):
    def __init__(self, date, livre, montant_achat):
        super().__init__(date, livre)
        self.montant_achat = montant_achat

    def get_montant(self):
        prix_a_payer = self.montant_achat
        return prix_a_payer


l4 = LivrePapier("Les misérables", "Victor Hugo", "Bon", True)
l5 = LivreNumerique("Germinal", "Emile Zola", "pdf", False)
emprunt = Emprunt("21/21/2023", l4, 10)
emprunt1 = Emprunt("21/21/2023", l5, 5)
print("----------------Liste des livres-----------------")
liste = [l4, l5]

liste_emprunt = [emprunt, emprunt1]
print(liste)
print("----------------Les Emprunts-----------------")
print(emprunt)
print("---------------------------------")
print(emprunt1)
print("----------------Liste Emprunts-----------------")
print(liste_emprunt)
