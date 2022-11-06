#Karib Othman
#300266967

##################################################################
# Question 4
##################################################################
'list()->str() and int() la fonction retourne les caracteres de la listes qui ne sont pas des entiers ainsi que la somme des entiers positifs'
def nonEntiers(listeDeCaracteres): #definition de la liste
#on initialise les variables
    somme=0
    x=" "
    for i in range (len(listeDeCaracteres)):#boucle for qui a pour intervalle la longeure de la liste
       
        #si les elements de la liste sont des entiers postifs:
        if listeDeCaracteres[i].isdigit() and int(listeDeCaracteres[i])>0:
           #
            somme=somme+int(listeDeCaracteres[i])
       

        #si les elements de la listes ne sont pas des entiers:
        elif not listeDeCaracteres[i].isdigit():
            x=x+listeDeCaracteres[i]
            
            
    
    resultat=("Non entiers positifs:"+ str(x)+ "-"+ "Somme entiers positifs: "+ str(somme))      
    #on retourn le resultat
    return resultat
        
            
