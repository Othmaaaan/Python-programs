def estdivisible(x):
    if x%2==0 and x%3==0:
        return 1
    elif x%2==0 or x%3==0:
        return 2
    elif  x%2!=0  and x%3!=0:
        return 0
    



x= int(input("entrez un nombre x: "))
resultat=estdivisible(x)
if resultat==1:
    print(x,"est divisible par 2 et par 3")
elif resultat==2:
    print(x,"est divisivle par 2 ou par 3")
elif resultat==0:
    print(x,"est divisble ni par 2 ni par 3")
