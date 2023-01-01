class compteBanquaire:

    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def Versement(self, versement):
        self.solde = self.solde + versement

    def Retrait(self, retrait):
        if retrait > self.solde:
            print("solde insuffisant!!!")
        else:
            self.solde = self.solde - retrait

    def Agios(self):
        self.solde = self.solde - (self.solde*5)/100

    def Afficher(self):
        print("Nom : {}\nNumero de compte : {}\nSolde : {} ".format(self.nom, self.numeroCompte, self.solde))


b1 = compteBanquaire(1, "Diouf", 10000000)
b1.Versement(3000)
b1.Retrait(2000)
b1.Agios()
b1.Afficher()