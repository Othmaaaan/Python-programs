#Karib Othman
#300266967

def verifieDonnees(buts, aides, penalites, matchs, annees):#definition de la fonction
    if buts>=20 or aides>=25 or penalites<25: 
        print("le joueur est qualifié pour le programme de prime")
        #attribution des codes de primes
        if annees>=5 and matchs>55: 
            return 3
        if annees>=5 and matchs<=55:
            return 2
        if annees<5:
            return 1
    elif buts<20 or aides<25 or penalites>=25:
        print("le joueur n'est pas qualifié pour le programme de prime")
        return 0

def collecteDonnees():#defintion de la deuxieme fonction
    # application des conditions pour obtenir les codes de primes selon le nombre de buts d'aides de penalités de matchs joués ainsi que le nombre d'années
    butsinput=int(input("entrez le nombre de buts:"))
    if butsinput<0:
        print("Erreur")
        print("0")
    
    aidesinput=int(input("entrez le nombre d'aides:"))
    if aidesinput<0:
        print("Erreur")
        print("0")
    penalitesinput= int(input("entrez le nombre de penalites:"))
    if penalitesinput<0:
        print("Erreur")
        print("0")
    matchsinput=int(input("entrez le nombre de matchs joues:"))
    if matchsinput<0:
        print("Erreur")
        print("0")
    anneesinput= int(input("entrez le nombre d'annees:"))
    if anneesinput<0:
        print("Erreur")
        print("0")
    codeprime= verifieDonnees(butsinput, aidesinput, penalitesinput, matchsinput, anneesinput)
    return codeprime
    
    
    
    
    
    
    
