#KARIB Othman
#3002669667

def somme_de_trois(x):
    for i in range(len(x)):
        if x[i]+x[i+1]+x[i+2]==0:
            return True
        else:
            return False
