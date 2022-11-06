
def calculeFact():
    factoriel=1
    for i in range(1,n+1):
        factoriel= i*factoriel
    return factoriel
n=int(input("entrer un nombre: "))  
while n<0:
    print("Il ne faut pas rentrez de nombre négatif, réessayez")
    n=int(input("entrer un nombre: "))
if n==0:
    print("1")
if n>0:
    print(calculeFact())
