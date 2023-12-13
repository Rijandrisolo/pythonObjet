class Livre:

    def __init__(self, titre, auteur, achetable=False):
        self._titre = titre
        self._auteur = auteur
        self._achetable = achetable

    def __str__(self):
        if self._achetable:
            return f" Titre : {self._titre} - Auteur : {self._auteur} - Achetable \n"
        else:
            return f" Titre : {self._titre} - Auteur : {self._auteur} \n"

    def __repr__(self):

        return f" Titre : {self._titre} - Auteur : {self._auteur} - Achetable : {self._achetable}"

    @property
    def titre(self):
        return self.titre

    @property
    def auteur(self):
        return self.auteur

    @property
    def achetable(self):
        return self.achetable

    @titre.setter
    def titre(self, newtitre):
        self._titre = newtitre

    @auteur.setter
    def auteur(self, newauteur):
        self._auteur = newauteur

    @achetable.setter
    def achetable(self, newachetable):
        self._achetable = newachetable


l1 = Livre("La recette", "Francis Navarre")
l2 = Livre("Le jardin", "Jacques Pourcel", False)
l3 = Livre("Les Misérables", "Victor Hugo", True)
print("----------------- str ------------------")
print(l1, l2, l3)
print("-----------------après setter ------------------")
liste = (l1, l2, l3)
l1.auteur = "Laurent Pourcel"
print(l1, l2, l3)
print("----------------- Liste ------------------")
print(liste)
