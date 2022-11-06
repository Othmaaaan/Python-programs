#KARIB Othman
#300266967

class Voiture ():
    
    def __init__(self,marque='Ford',couleur='Rouge'):
        self.marque=marque
        self.couleur=couleur
        self.conducteur='personne'
        self.acceleration=0

    def choix_conducteur(self,nom):
        self.conducteur=nom


    def accelerer(self,taux,duree):
        if self.conducteur=='personne':
            print("Cette voiture n'a pas de chauffeur")
        else:
            self.accelererion=taux*duree
            
        
    def affiche_tout(self):
        print(self.marque)
        print(self.couleur)
        print(self.conducteur)
        print(str(self.acceleration)+" m/s")
        
        
    def __repr__(self):
        return self.couleur+" "+self.marque
    def __eq__(self,autre):
        return self.marque==autre.marque and self.couleur==autre;couleur
