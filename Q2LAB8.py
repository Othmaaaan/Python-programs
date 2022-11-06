#KARIB OTHMAN
#300266967

def  somme_matrices(m1,m2):
    i=0
    somme=[]
    somme2=[]
    while i<len(m1) and i<len(m2):
        c=0
        
        while c<len(m1[i]) and c<len(m2[i]):
            somme.append(m1[i][c]+m2[i][c])
            c+=1
        somme2.append(somme)
        somme=[]
            
        i+=1

    return somme2
