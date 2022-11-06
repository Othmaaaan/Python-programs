#300266967
#KARIB OTHMAN

def transpose(L):
    
    L1=[]
    L2=[]


    i=0
    while i<len(L):
        c=0
        while c<len(L[i]):
            if i!=(len(L)-1):
                L1.append(L[i][c])
                L2.append(L1)
                L1=[]
            elif i==(len(L)-1):
                L2[c].append(L[i][c])

            c+=1
        i+=1
    return L2

            
