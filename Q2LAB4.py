#Karib Othman
#300266967

def bouclefor(n):
    
    for i in range(1,n+1):
        print(i)


def bouclewhile(n):
    counter= 1
    while counter<=n:
        print(counter)
        counter+=1
        
    
n= int(input("entrez la valeur de n:"))
a=bouclefor(n)
b=bouclewhile(n)
