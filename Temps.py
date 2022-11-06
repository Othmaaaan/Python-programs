#KARIB Othman
#300266967

class Temps:
  '''classe temporelle'''

  def __init__(self, h=12, m=0, s=0):
    '''(Temps)-> None'''
    self.heure = h
    self.minute = m
    self.seconde = s

  def setTemps(self, h, m=0, s=0):
    '''(Temps)-> None'''        
    self.heure = h 
    self.minute = m
    self.seconde = s

    if self.heure>=24:
      self.heure-=24

    if self.minute>=60:
      self.heure+=1
      self.minute-=60

    if self.seconde>=60:
      self.minute+=1
      self.seconde-=60

  def estAvant(self,t2):
    resultat=False
    if self.heure<t2.heure:
      resultat=True
    elif self.heure==t2.heure and self.minute<t2.minute:
      resultat=True
    elif self.heure==t2.heure and self.minute==t2.minute and self.seconde<t2.seconde:
      resultat=True

    return resultat

  def durée(self,t2):

    if self.estAvant(t2)==True:
      
      he=abs(self.heure-t2.heure)
      mi=abs(self.minute-t2.minute)
      se=abs(self.seconde-t2.seconde)

      print(str(he)+':'+str(mi)+':'+str(se))




  def affiche_heure(self):
    '''(Temps)-> None'''
    print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde)) 

  def __repr__(self):
    '''(Temps)-> str'''
    return (str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))

  def __eq__(self, autre):
    '''(Temps)-> bool'''
    return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde
  
temps1=Temps(1,2,3)

