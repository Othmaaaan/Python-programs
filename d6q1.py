#KARIB Othman
#300266967

##############################
# Classe Personne
##############################
class Personne():
    '''classe qui definit les attributs et methodes reliés a une personne donnée.
    '''
    def __init__(self,nom,age):#On initiliase la classe
        self.nom=nom
        self.age=age
    def set_nom(self,nom):#affectation du nom
        self.nom=nom
    def set_age(self,age):#affectation de lage
        self.age=age
    def age_diff(self,p1):#on affiche la difference dage entre deux personnes
        print( str(abs(self.age-p1.age))+" ans de difference")
    
         


#################################
## Classe herite de la classe parent
#################################
class Etudiant(Personne):
    '''classe qui herite de la classe Personne et qui en plus definit les attributs et methodes
    specifiques a un etudiants donné.
    '''
    def __init__(self,nom,age,amis=[]):#On initiliase la classe
        Personne.__init__(self,nom,age)
        self.amis=amis
        
    def ajoute_ami(self,etudiantx):#cette methode ajoute une personne a une liste d'amis
        if etudiantx not in self.amis:
            self.amis.append(etudiantx)
    def __repr__(self):#retourne le nom et lage d'un etudiant 
        return "Etudiant"+":"+str(self.nom)+":"+str(self.age)
    def affiche_amis(self):#affiche les amis d'un etudiant
        print("Voici les amis de: ", str(self))
        friends=" "
        
        i=0
        while i<len(self.amis):
            friends=friends+ str(self.amis[i])+" - "
            i+=1
        print(friends)




