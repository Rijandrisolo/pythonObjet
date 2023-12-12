class Zoo:
    liste_animaux = []
    nbr_total = 0

    @classmethod
    def ajouter_animaux(cls, animal, nombre):
        if animal not in cls.liste_animaux:
            cls.liste_animaux.append(animal)
        cls.nbr_total += nombre

    @classmethod
    def afficher_animaux(cls):
        print(cls.liste_animaux)
        print(cls.nbr_total)


mon_zoo = Zoo()
Zoo.ajouter_animaux("Antilope", 3)
Zoo.ajouter_animaux("Caïman", 10)
Zoo.ajouter_animaux("Tigre", 4)
Zoo.ajouter_animaux("Lion", 2)
Zoo.ajouter_animaux("Caïman", 2)
Zoo.afficher_animaux()

Zoo.afficher_animaux()
Zoo.ajouter_animaux(animal="Lion", nombre=25)
