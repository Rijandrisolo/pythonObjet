class PersonneException(Exception):
    pass


class Personne:
    def __init__(self, nom, prenom, service):
        self.nom = nom
        self.prenom = prenom
        self.service = service


pers1 = Personne(nom="DUPONT", prenom="Antoine", service="DSI/JAVA")
pers2 = Personne(nom="CASA", prenom="", service="DSI/PHP")
pers3 = Personne(nom="OUASSA", prenom="Fatima", service="")
pers4 = Personne(nom="AC", prenom="Cassian", service="DSI/PYTHON")
pers5 = Personne(nom="M", prenom="Ha", service="")
pers6 = Personne(nom="PIC", prenom="A", service="DSI/JAVA")


class PersonneService:
    @staticmethod
    def valider(personne):
        try:
            if not personne.nom or len(personne.nom.strip()) < 2:
                raise PersonneException("Le nom est manquant.")

            elif not personne.prenom or len(personne.prenom.strip()) < 2:
                raise PersonneException("Le prénom est manquant.")

            elif not personne.service:
                raise PersonneException("Le service doit être renseigné.")
        except PersonneException as e:
            print(f"Erreur de validation pour {personne.nom} {personne.prenom}: {str(e)}")
        else:
            print(f"Validation réussie pour {personne.nom} {personne.prenom}.")


PersonneService.valider(pers1)
