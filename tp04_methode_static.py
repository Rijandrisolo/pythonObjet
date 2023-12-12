class ChaineUtils:

    @staticmethod
    def est_anagramme(comp1, comp2):
        if len(comp1) != len(comp2):
            return False
        if sorted(comp1.upper()) == sorted(comp2.upper()):
            return True
        else:
            return False

    @staticmethod
    def comptage(chaine1, souschn):
        return chaine1.count(souschn)


print(ChaineUtils.est_anagramme("chine", "chien"))
print(ChaineUtils.est_anagramme("manoir", "minora"))
print("la chaine revient ", ChaineUtils.comptage("marine","mari"), "fois")
