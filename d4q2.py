#300266967 KARIB Othman
#300220488 BENJELLOUN Meryem

def sequenceDesDeux(x): #definition de la fonction
     '''(list)-> bool
      Retourne true s’il y a au moins une séquence de deux
      éléments consécutifs égaux, et False sinon
      '''
     compteur=0 #initialisation du compteur
     for k in range(len(x)): #creation de la boucle
          if x[k]==x[k+1]:
               #retourne la boolenne
               return True
          else:
               compteur=compteur+1
          if compteur==(len(x)-1):
               #retourne la boolenne
               return False
          
            
     
     
     
              
          





#programme principal

liste=[]
y=input("Veuillez entrer une liste de valeurs séparées par des virgules: ")
a=''
chaine=''
#creation de la boucle
for i in range(len(y)):
     if y[i]!=',':
          a=a+y[i]
          chaine=chaine+y[i]
     elif y[i]==',':
          liste.append(float(a))
          chaine=''
          a=''
liste.append(float(chaine))
#affiche le resultat
print(sequenceDesDeux(liste))
     
     
