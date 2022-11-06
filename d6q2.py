#KARIB Othman
#300266967
#################################
## Classe Animal 
#################################
class Animal():
    '''classe qui definit les attributs et methodes d'un animal donné
    '''
    def __init__(self,aAge,aType=""):#On innitilaise la classe
        self.age=aAge
        self.type=aType
    def set_type(self,type_):#affectation du type
        self.type_=type_
    def set_age(self,age):#affectation de l'age
        self.age=age
    def get_type(self,type_):#on retourne le type
        return self.type_
    def get_age(self,age):#on retourne l'age
        return self.age
    
    

#################################
## Classe herite de la classe parent 'Animal'
#################################
class Felin(Animal):
    '''classe qui herite de la classe Animal et qui en plus definit les attributs et methodes
    specifiques a un felin donné
    '''
    def __init__(self,aAge,aType="",vitesse=0):#on initialise la classe
        Animal.__init__(self,aAge,aType)
        self.vitesse=vitesse
        
    def set_vitesse(self,vitesse):#affectation de la vitesse
        self.vitesse=vitesse
    def get_vitesse(self):#on retourne la vitesse
        return self.vitesse
    def __repr__(self):#cette methode permet de retourner le type, lage, et la vitesse d'un felin
        return("Felin"+":"+str(self.type_)+" - "+str(self.age)+" - "+str(self.vitesse)+"km/h")
    def compareRapidite(self,t1):#on compare la vitesse de deux felins
        if self.get_vitesse() > t1.get_vitesse():
            print("Le felin le plus rapide est:",str(self))
        elif self.get_vitesse()<t1.get_vitesse():
            print("Le felin le plus rapide est:",str(t1))
        else:
            print("Les deux felins ont la même vitesse")
        
####################################
#N'ecrivez--rien-- dans le programme principal 
####################################

