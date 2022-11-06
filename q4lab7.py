#KARIB Othman
#300266967



def move_zeros_v1(liste):
    tmp=[]
    for i in range(len(liste)):
        if liste[i]!=0:
            tmp.append(liste[i])
    for i in range(len(liste)):
        if liste[i]==0:
            tmp.append(liste[i])
    
    return tmp


def move_zeros_v2(liste):
    tmp=[]
    counter=liste.count(0)
    compteur=0
    for i in range(len(liste)):
        if counter>i:
            liste.remove(0)
            tmp.append(0)
    for i in range(len(tmp)):
        liste.append(tmp[compteur])
        compteur+=1
    print( liste)




def move_zeros_v3(liste):
    
    
    for i in range(len(liste)):
        if liste[i]==0:
            liste.append(liste[i])
            liste.remove(liste[i])
    
    print(liste)
            
            
            
    
