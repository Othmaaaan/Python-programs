#On definit la fonction

def analyseNombre():
    n=int(input("entrez n:"))               
#On extrait chque chiffre du nombre n
    n1= (n//1000)%10
    n2= (n//100)%10
    n3= (n//10)%10
    n4= (n)%10

    n_1= (n1)%2
    n_2= (n2)%2
    n_3= (n3)%2
    n_4= (n4)%2


    return (n_1==0 and n_2==0 and n_3==0 and n_4==0) or (n1==7 or n2==7 or n3==7 or n4==7)




    
