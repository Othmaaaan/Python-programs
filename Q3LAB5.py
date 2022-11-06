#Karib Othman
#300266967
from math import *
def calculDistances(v):
    distance=[]
    for i in range(0,100,10):
        distance.append((2*int(v)**2)*cos(pi*i/180)*sin(pi*i/180)/9.8)
    return distance
    






v=float(input("entrez la vitesse en m/s: "))

distance=calculDistances(v)

for a in range (0,100,10):
    print("pour l'angle", a,"degres", "la balle parcourt", distance[a//10]," metres")
