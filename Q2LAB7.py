#KARIB Othman
#300266967



def histo_n(x):
    
    dico={}
    for c in x:
        dico[c]=dico.get(c,0)+1
    liste=list(dico.items())
    return liste



x=tuple(eval(input("Entrez la liste des entiers: ")))

resultat=histo_n(x)
resultat.sort()
print(resultat)
