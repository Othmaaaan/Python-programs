#300266967 KARIB Othman
#300220488 BENJELLOUN Meryem

def compte_pos(x): #definition de la fonction
     '''(list)->int
      Retourne le nombre d'elements positifs
      '''
     compteur=0 #on initialise le compte 
     for k in range(len(x)):#création d'une boucle
          if x[k]>0:
               compteur=compteur+1
          else: 
               compteur=compteur
          
     
     
     return compteur #retourne le nombre d'element positifs
#programme principale
liste=[] #on initialise la liste
y=input("Veuillez entrer une liste de valeurs séparées par des virgules: ")
a=''
chaine=''

for i in range(len(y)):
     if y[i]!=',':
          a=a+y[i]
          chaine=chaine+y[i]
     elif y[i]==',':
          liste.append(float(a))
          chaine=''
          a=''
liste.append(float(chaine))
     
     
     
     
     
print(compte_pos(liste)) #affiche le nombre d'elements positifs




    


