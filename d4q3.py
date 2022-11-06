#300266967 KARIB Othman
#300220488 BENJELLOUN Meryem
def sequenceMax(x):#definition de la fonction
     '''(list)-> int
     cette fonction prend une liste de nombres et retourne
     la longueur de la plus longue séquence d'éléments consécutifs égaux 
      '''
     l=1  
     L=1 
     #creation de la boucle
     for k in range(len(x)-1):
          #conditions
          if x[k]==x[k+1]:
               l=l+1
               
          else:
               
               if l>L:
                    L=l
                    l=0
     
               else:
                    L=L
     if x[len(x)-1]==x[len(x)-2] and l>=L:
          L=L+1
          
               
     return L
     
     
               
               

          
               
          
               
               
     
          
               

              
         

               
     
  #programme principal        
liste=[]#initialisation de la liste
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
     
     
     
     
#affichage de la longueur de la plus longue sequence d'elements consecutifs egaux
print(sequenceMax(liste))



