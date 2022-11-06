#Karib Othman
#300266967

##################################################################
# Question 1
##################################################################
'int()->list() on retourne les diviseurs'
def listeDiviseurs(n):#definition de la fonction


#on initialise la liste
    liste=[] 
#on cree une boucle for
    for i in range(1,n+1):
        #condition 1: si n est positif
        if n>0:
            diviseur=n%i
            #condition 2: si diviseur est nul et i est impair
            if diviseur==0 and i%2==1:
                liste.append(i)
                x=liste
                
                
        else:
            return liste
    #on retourne la liste
    return x
