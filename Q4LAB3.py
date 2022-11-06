def nombresqrt(a,b,c):
    if ((b**2)-4*a*c)==0:
        return 1
    elif ((b**2)-4*a*c)>0:
        return  2

a= int(input("entrez la valeur de a:"))
b= int(input("entrez la valeur de b:"))
c= int(input("entrez la valeur de c:"))

resultat=nombresqrt(a,b,c)
if resultat==1:
    print("le nombre de racines est 1")
elif resultat==2:
    print("le nombre de racines est 2")
else:
    print("il n'ya aucune racine")
