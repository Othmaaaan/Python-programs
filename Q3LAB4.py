#Karib Othman
#300266967
import random
def devine(nombre):
    
    compteur=0
    while n!=nombre:
        compteur+=1
        if n<nombre:
            print("trop bas")
            nombre=int(input("devine le nombre"))
        elif n>nombre:
            print("trop haut")
            nombre=int(input("devine le nombre"))
            
    if n==nombre:
        print("bravo vous avez trouvé !!! Le nombre de tentatives est: ",compteur)
        return compteur
nombre=int(input("devine le nombre"))
n=random.randrange(1,11)
devine(nombre)
