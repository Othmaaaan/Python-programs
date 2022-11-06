#Karib Othman
#300266967

def elections(vote): #definjtion de la fonction

    total=vote.count("oui")+vote.count("non")+vote.count("abstention")
    pctgoui=(int(vote.count("oui"))*100)/(total-vote.count("abstention")) #calcul du pourcentage de oui (nombre de oui * 100)/nombre total de votes
    return float(pctgoui)

vote= str(input("entrez les votes(oui, non, ou abstention) séparés par des espaces, et à la fin appuyez sur entrer:")) #entree de l'utilisateur
x=elections(vote)    

if x==100: #premiere condition: si tous les votes sont des oui, sans compter les abstentions
    print("unanimité")
    
elif x>=(2/3) * 100 and x<100:#deuxieme conditon: si au moins deux tiers des votes sont des oui
    print("majorité claire")
    
elif x>=(1/2)*50 and x<(2/3) * 100:#troisieme condition: si au moins la moitié  et au plus les deux tiers des votes sont des oui 
    print("majorité simple")
            
elif x<1/2*50: # condition appliquée dans le cas où aucune des conditions precedentes n'est respectée
    print("la motion ne passe pas")
  
