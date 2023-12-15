class Animal:
    def __init__(self, nom, categorie, comportement):
        self.nom = nom
        self.categorie = categorie
        self.comportement = comportement

class Zone:
    def __init__(self, nom):
        self.nom = nom
        self.animaux = []

    def get_quant_nourriture(self):
        pass

class SavaneAfricaine(Zone):
    def get_quant_nourriture(self):
        return len(self.animaux) * 100

class FermeReptiles(Zone):
    def get_quant_nourriture(self):
        return len(self.animaux) * 0.1

class Aquarium(Zone):
    def get_quant_nourriture(self):
        return len(self.animaux) * 1

class ZoneCarnivore(Zone):
    def get_quant_nourriture(self):
        return len(self.animaux) * 10

class ZoneVoliere(Zone):
    def get_quant_nourriture(self):
        return len(self.animaux) * 0.25

class Zoo:
    def __init__(self, nom):
        self.nom = nom
        self.zones = []

    def ajouter_animal(self, animal):
        if animal.categorie == "Poisson":
            zone = Aquarium("Zone Aquarium")
        elif animal.categorie == "Reptile":
            zone = FermeReptiles("Ferme Reptiles")
        elif animal.categorie == "Oiseau":
            zone = ZoneVoliere("Zone Volière")
        elif animal.comportement == "carnivore" and animal.categorie == "Mammifere":
            zone = ZoneCarnivore("Zone Carnivore")
        else:
            zone = SavaneAfricaine("Savane Africaine")

        zone.animaux.append(animal)
        self.zones.append(zone)

    def get_quant_nourriture(self):
        total_nourriture = 0
        for zone in self.zones:
            total_nourriture += zone.get_quant_nourriture()
        return total_nourriture

    def afficher_infos(self):
        for zone in self.zones:
            print(f"---------------------{zone.nom} -----------------------")
            for animal in zone.animaux:
                print(f"   - {animal.nom} ({animal.categorie}, {animal.comportement}) ")
            print("\n")


zoo = Zoo("Mon Zoo")

animal1 = Animal("Lion", "Mammifere", "carnivore")
animal2 = Animal("Gazelle", "Mammifere", "végétarien")
animal3 = Animal("Requin", "Poisson", "carnivore")
animal4 = Animal("Serpent", "Reptile", "carnivore")
animal5 = Animal("Perroquet", "Oiseau", "omnivore")

zoo.ajouter_animal(animal1)
zoo.ajouter_animal(animal2)
zoo.ajouter_animal(animal3)
zoo.ajouter_animal(animal4)
zoo.ajouter_animal(animal5)

print(f"Quantité de nourriture nécessaire : {zoo.get_quant_nourriture()} kg")
print("\n------------------- Animaux par zone ----------------------\n")
zoo.afficher_infos()