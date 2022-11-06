#Karib Othman
#300266967

##################################################################
# Question 3
##################################################################
'list()->int()'
def compteEntiers(listeEntiers):
    #on intitialise la variable R qui compte le nombre d'entiers dans la listes
    R=0
    #boucle for qui a pour intervalle la longueur de la liste
    for i in range(len(listeEntiers)):
        #si l'entier est positif:
        if listeEntiers[i]>0:
            R=R+1
        #si l'entier est négatif 
        elif listeEntiers[i]<0:
            R=R-1
            
       #si l'entier est nul     
        elif listeEntiers[i]==0:
            R=R
    #on retourne R    
    return R
