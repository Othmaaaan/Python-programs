#Definition de la fonction

def moyennePonderee():
    a=int(input("entrez la premiere note:"))
    b=int(input("entrez le poids de la premiere note:"))
    c=int(input("entrez la deuxieme note:"))
    d=int(input("entrez le poids de la deuxieme note:"))
    resultat=((a*b)+(c*d))

    return(resultat)
