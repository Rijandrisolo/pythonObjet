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
        return f" date:{self.date} livre : {self.livre}"


class Emprunt(Sortie):

    def __init__(self, date: str, livre, duree_emprunt: int):
        super().__init__(date, livre)
        self.duree_emprunt = duree_emprunt

    def get_montant(self):
        prix_unit = 0
        if type(self.livre) == LivrePapier:
            prix_unit = 0.5
        elif type(self.livre) == LivreNumerique:
            prix_unit = 0.25

        prix_emprunt = self.duree_emprunt * prix_unit
        return prix_emprunt

    def __str__(self):
        return f"{super().__str__()} durée : {self.duree_emprunt} Prix {self.get_montant()}"


class Achat(Sortie):
    def __init__(self, date, livre, montant_achat):
        super().__init__(date, livre)
        self.montant_achat = montant_achat

    def get_montant(self):
        prix_a_payer = self.montant_achat
        return prix_a_payer


l4 = LivrePapier("Zo", "Randza Razanamihoatra", "Bon", True)
l5 = LivreNumerique("Dinitra", "Rado", "pdf", False)
liste = [l4, l5]
emprunt = Emprunt("21/21/2023", l4, 10)
print(liste)
print(emprunt)
