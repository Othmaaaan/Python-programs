#KARIB Othman
#300266967

class CompteBancaire():

    def __init__(self,nom='Dupont',solde=1000):
        self.solde=solde
        self.nom=nom

    def depot(self,somme):
        self.solde+=somme
        
    def retrait (self,somme):
        #appel=depot(self,somme)
        self.solde-=somme
        
    def affiche(self):
        titulaire=print("Letitulaire du compte bancaire est: ",self.nom)
        soldecompte=print("Son solde est: ",self.solde)
