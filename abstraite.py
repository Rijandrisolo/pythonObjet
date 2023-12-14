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
        #prix_unit = 0
        # if type(self.livre) == LivrePapier:
        #     prix_unit = 0.5
        # elif type(self.livre) == LivreNumerique:
        #     prix_unit = 0.25

        prix_emprunt = self.duree_emprunt *self.livre.prix_unit
        return prix_emprunt


class Achat(Sortie):
    def __init__(self, date, livre):
        super().__init__(date, livre)
        self.montant_achat = self.get_montant()
    def __str__(self):
        return f"{super().__str__()} date : {self.date} \n Montant achat : {self.get_montant()}"

    def get_montant(self):
        prix_a_payer = 0
        print("test")
        if self.livre._achetable:
            montant_achat = self.livre.prix_achat
            return montant_achat
       # return f"on ne peut pas acheter ce livre"


l4 = LivrePapier("Les misérables", "Victor Hugo", "Bon", True, 10, 0.5)
l5 = LivreNumerique("Germinal", "Emile Zola", "pdf", False, 5, 0.2)
emprunt = Emprunt("21/11/2023", l4, 10)
emprunt1 = Emprunt("21/12/2023", l5, 5)
achat1 = Achat("21/12/2023", l4)

liste = [l4, l5]

liste_emprunt = [emprunt, emprunt1]
print("----------------Liste des livres-----------------")
print(liste)
print("----------------Les Emprunts-----------------")
print(emprunt)
print("---------------------------------")
print(emprunt1)
print("----------------Liste Emprunts-----------------")
print(liste_emprunt)
print("----------------Achat-----------------")
print(achat1)