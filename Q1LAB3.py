#KARIB Othman
#300266967

def ageFunction(age):
    if age>= 18 and age<= 55:
        return True
    else:
        return False

age= int(input("entrez votre âge svp: "))
resultat= ageFunction(age)

if resultat==True:
    print("Transaction acceptée")
elif resultat==False:
    print("Transaction refusée")

