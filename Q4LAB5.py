#Karib Othman
#300266967

    



from math import *
def ecart_type(x):

    liste=list(eval(str(x)))
    
    somme=0
    for i in range(len(liste)):
        somme=somme+liste[i]
    a= somme/len(liste)


    ecart =0
    for s in range(len(x)):
        ecart=ecart+((x[s]-a)**2)
    ecart=ecart/(len(x)-1)
    ecart=sqrt(ecart)


    return ecart

v=input("entrez une liste de valeurs separees par des virgules: ")
z=ecart_type(list(eval(v)))
print("l'ecart type est: ", z)
