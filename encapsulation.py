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

    def affiche_infos(self):
        print(f"Titre : {self._titre} - Auteur : {self._auteur} - Achetable : {self._achetable}")


class LivrePapier(Livre):
    def __init__(self, titre, auteur, etat, achetable, prix_unit=0.5):
        super().__init__(titre, auteur, achetable=False)
        self._achetable = achetable
        self._etat = etat
        self.prix_unit = prix_unit

    def __str__(self):
        return f" {super().__str__()} Etat : {self._etat} \n"

    def __repr__(self):
        return f" {super().__repr__()} Etat : {self._etat} \n"


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, formats, achetable, prix_unit=0.25):
        super().__init__(titre, auteur, achetable=False)
        self._achetable = achetable
        self._formats = formats
        self.prix_unit = prix_unit

    def __str__(self):
        return f"{super().__str__()} Format : {self._formats} \n"

    def __repr__(self):
        return f"{super().__repr__()} Format : {self._formats} \n"


if __name__ == "__main__":

    l1 = Livre("La recette", "Francis Navarre")
    l2 = Livre("Le jardin", "Jacques Pourcel", False)
    l3 = Livre("Les Misérables", "Victor Hugo", True)
    l4 = LivrePapier("Zo", "Randza Razanamihoatra", "Bon", True)
    l5 = LivreNumerique("Dinitra", "Rado", "pdf", False)

    print("----------------- Affiche_infos ------------------")
    l4.affiche_infos()
    l5.affiche_infos()
    print("----------------- str ------------------")
    print(l1, l2, l3)
    print("----------------- LivrePapier ------------------")
    print(type(l4))
    print("----------------- LivreNumerique ------------------")
    print(l5)
    print("-----------------après setter ------------------")
    liste = [l1, l2, l3, l4, l5]
    l1.auteur = "Laurent Pourcel"
    print(l1, l2, l3)
    print("----------------- Liste ------------------")
    print(liste)
    for l in liste:
        print(l)
