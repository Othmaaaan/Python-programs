#KARIB OTHMAN
#300266967
def produit_matrices(m1,m2):
    somme=[]
    
    for i in range(len(m1)):
        matrice=[]
        for j in range (len(m2[0])):
            elem=0
            for c in range(len(m1[0])):
                elem=elem+ (m1[i][c]*m2[c][j])
            matrice.append(elem)
        somme.append(matrice)
    return somme

m=produit_matrices([[1,2,3],[4,5,6]], [[1,2],[3,4],[5,6]])
print(m)
