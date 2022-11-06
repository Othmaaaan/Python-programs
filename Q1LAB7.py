#300266967
#KARIB Othman

def histogramme(chaine):
    
    dictionnaire={}
        
    for l in chaine:
        dictionnaire[l]= dictionnaire.get(l,0)+1
    dictionnaire=list(dictionnaire.items())
    dictionnaire.sort()
    dictionnaire=dict(dictionnaire)
    return dictionnaire



chaine=(input("entrez une chaine de caractere: "))

print(histogramme(chaine))
