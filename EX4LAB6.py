#KARIB OTHMAN
#300266967

s=input("entrez la chaine de caractère s: ")
def compte(s,c):
    c=s.count(c)
    return c
print(compte(s,"a"))

def compte2(s,c):
    compteur=0
    for i in range(len(s)):
        if s[i]=='a':
            compteur+=1
    return compteur
print(compte2(s,"a"))

