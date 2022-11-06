#KARIB Othman
#300266967

def pgcd(x,y):
    if x==0:
        return y
    if y==0:
        return x
    if x==y:
        return x
 
    if x>=y and x%y==0:
        return y
    if x<y:
        return pgcd(y,x)
    if x%y==0:
        return y

    else:
        return pgcd(y,x%y)
    
   
