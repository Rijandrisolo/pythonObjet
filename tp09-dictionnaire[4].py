from collections import Counter


class Salarie():
    def __init__(self, nom_salarie, matricule, service):
        self.nom_salarie = nom_salarie
        self.matricule = matricule
        self.service = service

    def __str__(self):
        return f" salarié : {self.nom_salarie} - matricule : {self.matricule} - service : {self.service}"

    def __repr__(self):
        return f"  {self.nom_salarie}  {self.matricule}  {self.service}"


salarie1 = Salarie(nom_salarie="Antoine Dupont", matricule="127", service="DSI/JAVA")
salarie2 = Salarie(nom_salarie="Berthe Casa", matricule="238", service="DSI/PHP")
salarie3 = Salarie(nom_salarie="Fatima Ouassa", matricule="478", service="DSI/JAVA")
salarie4 = Salarie(nom_salarie="Cassian Andor", matricule="156", service="DSI/PYTHON")
salarie5 = Salarie(nom_salarie="Hassan Missen", matricule="096", service="DSI/PYTHON")
salarie6 = Salarie(nom_salarie="Aurélien PIC", matricule="889", service="DSI/JAVA")

liste = [salarie1, salarie2, salarie3, salarie4, salarie5, salarie6]

liste_service = []
compte_service = {}

for essai in enumerate(liste):
    # print(essai[1].service)
    liste_service.append(essai[1].service)
    print(liste_service)
for service in liste_service:
    # print(service, liste_service.count(service))
    compte_service.update({service: liste_service.count(service)})

print("Liste service", compte_service)
