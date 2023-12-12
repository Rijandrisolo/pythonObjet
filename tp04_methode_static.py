class ChaineUtils:

    @staticmethod
    def est_anagramme(comp1, comp2):
        if len(comp1) != len(comp2):
            return False
        if sorted(comp1.upper()) == sorted(comp2.upper()):
            return True
        else:
           return False

print(ChaineUtils.est_anagramme("chine", "chien"))
