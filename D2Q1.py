#Karib Othman
#300266967

def calculPrix(article, quantite):#defintion de la fonction
    #constantes
    bureau= 50.9 
    chaise= 65.7 
    imprimante= 32.5 
    scanneur= 28.0 
    #formule du prix
    prix=(article)*int(quantite)
    
    chainebureau="bureau"
    chainescanneur="scanneur"
    chainechaise= "chaise"
    chaineimprimante="imprimante"
    if article==(chainebureau): #condition1: si l'article est un bureau
        prix= bureau*int(quantite)
        return prix

    elif article== (chainechaise):#condition2: si l'article est une chaise
        prix= chaise*int(quantite)
        return prix


    elif article==(chaineimprimante):#condition3: si l'article est une imprimante
        prix=imprimante*int(quantite)
        return prix

    elif article==(chainescanneur):#condition4: si l'article est un scanneur
        prix=scanneur*int(quantite)
        return prix

    elif article!=((chainebureau) or (chainescanneur) or (chaineimprimante) or (chainechaise)):
        prix=0
        return prix



def calculTotal(article1, quantite1, article2, quantite2, article3, quantite3):
    #prix totale de tous les articles multipliés à leurs quantités
    prixtotale= calculPrix(article1, quantite1)+calculPrix(article2, quantite2)+calculPrix(article3, quantite3)
    return prixtotale 

def lireArticles():

    a= str(input("entrez le premier article:"))
    if a=="bureau" or a== "chaise" or a== "imprimante" or a=="scanneur":
        b= int(input("entrez la quantité de " +a))
    elif a!="bureau" or a!= "chaise" or a!= "imprimante" or a!="scanneur":
        b= 0    

    c=(input("entrez le deuxieme article:"))
    if c=="bureau" or c== "chaise" or c== "imprimante" or c=="scanneur":
        d=int(input("entrez la quantité de "+c))
    elif c!="bureau" or c!= "chaise" or c!= "imprimante" or c!="scanneur":
        d=0   

    e=input("entrez le troisieme article:")
    if e=="bureau" or e== "chaise" or e== "imprimante" or e=="scanneur":
        f=int(input("entrez la quantité de " +e))
    elif e!="bureau" or e!= "chaise" or e!= "imprimante" or e!="scanneur":
        f=0

    totaleprix=calculTotal(a,b,c,d,e,f)
    return totaleprix

#programme principal
prix=lireArticles()
print("le prix total de votre commande est de: $",prix, ",merci pour votre achat")
   

  
    
    

    
