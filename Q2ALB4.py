#Karib Othman
#300266967
def statistiques(l1):
    
    somme=0
    
    maximum=0
    minimum=l1[0]
    resultat=[]
    for i in range(len(l1)):
        somme=somme+l1[i]
        moyenne=somme/len(l1)   
    resultat.append(moyenne)
    for i in l1:
        if i>maximum:
            maximum=i
    resultat.append(maximum)
    for i in l1:
        if i<minimum:
            minimum=i
    resultat.append(minimum)
    return resultat
    
chaine=input("entrez une liste de valeurs separees par une virgule: ")

a=list(eval(chaine))
print("les statistiques sont:", statistiques(a))
    
