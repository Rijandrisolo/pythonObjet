class Theatre:

    def __init__(self, nom_theatre: str, capacite: int, nb_clients: int, recette: int):
        self.nom_theatre = nom_theatre
        self.capacite = capacite
        self.nb_clients = nb_clients
        self.recette = recette

    def __str__(self):
        return f" Théâtre : {self.nom_theatre} - capacité : {self.capacite} - Nombre Clients : {self.nb_clients} - Recette : {self.recette}"

    def __repr__(self):
        return f" Théâtre : {self.nom_theatre} - capacité : {self.capacite} - Nombre Clients : {self.nb_clients} - Recette : {self.recette}\n"

    def set_nom_theatre(self, nom_theatre: str):
        self.nom_theatre = nom_theatre

    def set_nb_clients(self, nb_clients: int):
        self.nb_clients = nb_clients

    def set_recette(self, recette: int):
        self.recette = recette

    def get_nom_theatre(self):
        return self.nom_theatre

    def get_capacite(self):
        return self.capacite

    def get_nb_clients(self):
        return self.nb_clients

    def get_recette(self):
        return self.recette

    def inscrire(self, nb, prix):
        print(f" Votre demande : {nb} places")
        if self.nb_clients + nb <= self.capacite:
            clients = self.nb_clients + nb
            chiffre = self.recette + prix
            print("nom théâtre : ", self.nom_theatre)
            self.nb_clients = clients
            self.recette = chiffre
            print(f" Votre réservation de {nb} places est enregistrée ")
            print(f"Il reste {self.capacite - self.nb_clients} places pour {self.nom_theatre}")
        else:
            print(f" Désolé, il ne reste que {self.capacite-self.nb_clients} places pour {self.nom_theatre}, vous avez demandé {nb}")

t1 = Theatre("Alexandre Burma", 60, 0, 0)
t2 = Theatre("Marcel Pagnol", 30, 0, 0)
liste = [t1, t2]
print(liste)
t1.inscrire(20, 200)
print(liste)
t1.inscrire(15, 200)
print(liste)
t1.inscrire(30, 200)

print(liste)
