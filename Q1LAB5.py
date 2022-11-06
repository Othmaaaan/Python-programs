#Karib Othman
#300266967

def cacluleMoyenne(x):
    liste=list(eval(x))
    print(liste)
    somme=0
    for i in range(len(liste)):
        somme=somme+liste[i]
        
    return somme/len(liste)



x=(input("Entrez une liste de valeurs separees par une virgule: "))


print("La moyenne de la liste donnée est: ", cacluleMoyenne(x))

   
