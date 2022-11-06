#KARIB Othman
#300266967

def verifieElement(A,n):

    if A[n-1]>=0 and A[n-1]<=9:
        if n==2 and (A[n-1]>=0 and A[n-1]<=9) and (A[n-2]>=0 and A[n-2]<=9):
            rep=True
        else:
            rep=verifieElement(A,n-1)
    else:
        rep=False
    return rep
