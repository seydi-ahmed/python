class Date_de_naissance:

    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def ToString(self):
        date = str(self.jour) + "/" + str(self.mois) + "/" + str(self.annee)
        return date

class Personne(Date_de_naissance):

    def __init__(self, nom, prenom, date_de_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance

    def Afficher(self):
        print("je m'appelle {} {} et je suis né le {}".format(self.prenom, self.nom, self.date_de_naissance.ToString()))


class Employe(Personne):

    def __init__(self, nom, prenom, date_de_naissance, salaire):
        Personne.__init__(self, nom, prenom, date_de_naissance)
        self.salaire = salaire

    def Afficher(self):
        Personne.Afficher(self)
        print("j'ai un salaire de {}".format(self.salaire))



d2 = Date_de_naissance(2, 12, 1999)
p2 = Employe("Faye", "Birame Penda Wagane", d2, 20000)
p2.Afficher()