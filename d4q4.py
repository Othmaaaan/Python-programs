#300220488 BENJELLOUN MERYEM
#300266967 KARIB OTHMAN



# Jeu de cartes.

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

#ces premieres fonctions sont deja completees pour vous, ne les changez pas

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'a ce que l'usager appuie Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente toutes les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)
    
#######################################################################################
#Les fonctions precedentes sont deja completees
#Completez les fonctions apres ce commentaire
#######################################################################################
    
def donne_cartes(p):                                                    #on definit la fonction donne_cartes qui prend pour parametre p
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]             #On initialise les listes donneur et autre     
     autre=[]
     for i in range(len(p)):                                 #Si l'indice est pair on ajoute a la liste vide 'autre' l'element de la liste p
         if i%2==0:
             autre.append(p[i])
         else:
             donneur.append(p[i])                            #Si l'indice est impair on ajoute a la liste vide 'donneur' l'element de la liste p
                                                             #Cette fonction permet de distribuer les cartes du paquet de maniere a ce que l'autre recoit la premiere carte
             
        
     


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

     
     return (donneur, autre) #La fonction retourne les listes donneur et autre


def elimine_paires(l):  #On definit la fonction elemine_paires qui prend pour parametre une liste l
    '''
     (list of str)->list of str

     Retourne une copie de la liste l avec toutes les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[] 
    l.sort()
    string=''
    for f in range(len(l)):    #On utilise une boucle for pour convertir la liste en chaine de caracteres
       string=string+l[f]
    
    s=''
    


    #Dans cette chaine de caracteres on separe les nombres ou les lettres des cartes de leurs couleurs: Pour ce faire on utilise la boucle for
    for x in range(len(string)):
        if string[x]== '1' or string[x]== '2' or string[x]== '3' or string[x]== '4'or string[x]== '5' or string[x]== '6' or string[x]== '7'or string[x]== '8' or string[x]== '9' or string[x]== 'A'or string[x]== 'K' or string[x]== 'Q' or string[x]== 'J'or string[x]== '0':
           s=s+string[x]
        elif string[x]== '♠' or string[x]== '♢' or string[x]== '♡' or string[x]== '♣':
           s=s+" "+string[x]+" "





    liste=[]    #On initialise la liste 'liste'
    b=''      
    chaine2=''
    for f in range(len(s)):   #Dans cette liste on ajoute les nombres ou les lettres des cartes dans des elements differents des couleurs pour pouvoir ainsi determiner les paires 
       if s[f]!=' ':
            b=b+s[f]
            chaine2=chaine2+s[f]
       elif s[f]==' ':
            liste.append(b)
            chaine2=''
            b=''


    




    LISTE=[]

        
    for i in range(0,(len(liste)-4),2): #Dans cette boucle on ajoute a la liste vide "LISTE" les elements de la liste en eleminant les pairs
        if liste.count(liste[i])%2==0:
           LISTE=LISTE
        elif liste.count(liste[i])==1 : 
           LISTE.append(liste[i])
           LISTE.append(liste[i+1])
        elif liste[i]==liste[i+2]==liste[i+4]:
           LISTE.append(liste[i])
           LISTE.append(liste[i+1])

    chaine=''                            #On convertit cette liste en chaine de caracteres afin qu'on puisse attribuer la couleur et le numero ou la lettre de la carte au meme element de cette liste
    for j in range(0,(len(LISTE)-1),2):
        chaine=chaine+LISTE[j]+LISTE[j+1]+' '
    

    a=''
    chaine3=''
    for k in range(len(chaine)):  #On convertit cette chaine de caracteres en liste
        if chaine[k]!=' ':
           a=a+chaine[k]
           chaine3=chaine3+chaine[k]
        elif chaine[k]==' ':
           resultat.append(a)
           chaine3=''
           a=''
    if liste[len(liste)-4]!=liste[len(liste)-2]:
       P=liste[len(liste)-4]+liste[len(liste)-3]
       resultat.append(P)
       p=liste[len(liste)-2]+liste[len(liste)-1]
       resultat.append(p)
    

        
  
        
        



    return resultat   #La fonction retourne la liste resulat



              
    
                        
        
            
              

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    
     
    

    random.shuffle(resultat)
    return resultat


def affiche_cartes(p): #On definit la fonction affiche_cartes(p) qui a pour parametre p
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    chaine=''                 #On convertit cette liste en chaine de caracteres
    for i in range(len(p)):
        chaine=chaine+p[i]+' '
    print(chaine) #On affiche cette chaine
   

    

def entrez_position_valide(n): #On definit la fonction entrez_position_valide(n) qui a pour parametre n
     '''
     (int)->int
     Retourne un entier lu au clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas entre 1 et n
     
     Précondition: n>=1
     '''
     s=int(input("Svp entrez un entier de 1 à "+str(n)+": ")) #On demande au joueur d'entrer au clavier un entier de 1 au nombre de cartes
     if s>n: #Tant qu'il ne satisfait pas cette condition on redemande au joueur de rerentrer un entier qui la satifait
          while s > n:
            s=int(input("Position invalide. Svp entrez un entier de 1 à "+str(n)+": "))
    
         

    
        
     return s #La fonction retourne cet entier
     
         
    
    
     

def joue(): #On definit la fonction joue() qui a pour parametre n
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet() #Cette fonction fait appel a plusieurs fonctions definies precedemment 
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     print("*********************************************")
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)
     while len(donneur)>0 and len(humain)>0: #Tant que ses conditions ne sont pas satisfaites, on ne sort pas de la boucle
     
     
           string=''
           s=''

           for f in range(len(humain)): #On convertit la liste humain en chaine de caracteres 
               string=string+humain[f]

         
           for l in range(len(string)):
                if string[l]== '1' or string[l]== '2' or string[l]== '3' or string[l]== '4'or string[l]== '5' or string[l]== '6' or string[l]== '7'or string[l]== '8' or string[l]== '9' or string[l]== 'A'or string[l]== 'K' or string[l]== 'Q' or string[l]== 'J'or string[l]== '0':
                    s=s+string[l]
                elif string[l]== '♠' or string[l]== '♢' or string[l]== '♡' or string[l]== '♣':
                    s=s+string[l]+" "
           print(s) #On affiche cette chaine de caracteres

           print("J'ai" ,len(donneur), " cartes. Si 1 est la position de ma première carte et",len(donneur)," la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
           print(len(donneur))

    
           

     

           print("vous avez demandé ma ", entrez_position_valide(len(donneur)),"-ème carte.")
           chaine=''

           liste1=['A','2','3','4','5','6','7','8','9','10','K','Q','J'] #On cree une liste contenant tout les numeros et lettres possibles pour des cartes

           chaine=chaine+liste1[random.randint(0,len(liste1)-1)] #On prend aleatoirement un de ces elements grace a la fonction random

           liste2=['♡','♠','♣','♢'] #On cree une liste contenant toutes les couleurs possibles pour des cartes
           chaine=chaine+liste2[random.randint(0,len(liste2)-1)] #On prend aleatoirement un de ces elements grace a la fonction random
     
           print("La voila. c'est un ",chaine)
           humain.append(chaine)
           s=s+chaine #On cree une chaine de caracteres contenant ces deux elements selectionnees precedement de maniere aleatoire 
           print("avec ",chaine,' ajouté, votre main est:,',s)
     

           print("Apres avoir defaussé toutes les paires et mélanger les cartes, votre main est:")
     
           melange_paquet(humain)
           x=elimine_paires(humain)
           string2=''
           s2=''
           for i in range(len(x)): #On convertit la liste x en chaine de caracteres
               string2=string2+x[i]

         
           for j in range(len(string2)):
                if string2[j]== '1' or string2[j]== '2' or string2[j]== '3' or string2[j]== '4'or string2[j]== '5' or string2[j]== '6' or string2[j]== '7'or string2[j]== '8' or string2[j]== '9' or string2[j]== 'A'or string2[j]== 'K' or string2[j]== 'Q' or string2[j]== 'J'or string2[j]== '0':
                    s2=s2+string2[j]
                elif string2[j]== '♠' or string2[j]== '♢' or string2[j]== '♡' or string2[j]== '♣':
                    s2=s2+string2[j]+" "
           print(s2) #On affiche cette chaine
           attend_le_joueur()
           print("*********************************************")
           print("Mon tour.")
           x=entrez_position_valide(len(humain))
           print("J'ai pris votre",x,"ieme carte.")
           
           HUMAIN=[] #On enleve la carte prise par l'autre joueur dans la main de l'humain
           for m in range(len(humain)):
               if humain[m]!=humain[x]:
                        HUMAIN.append(humain[m])
               elif humain[m]==humain[x]:
                        HUMAIN=HUMAIN
           humain=HUMAIN
           
                                
          
           attend_le_joueur()
           print("*********************************************")
           
     if len(donneur)==0 : #Si le robot n'a plus de cartes c'estlui qui a gagne
          print("J'ai terminé toutes les cartes.")
          print("Vous avez perdu! Moi, Robot, j'ai gagné.")

     elif len(humain)==0: #Si j'ai plus de cartes c'est moi qui ai gagne
          print("Vous avez terminé toutes les cartes.")
          print("Félicitations! Vous, vous avez gagné.")

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
    

	 
# programme principale deja completé
joue()


##################################################################################################################
'''
Un exemple de partie gagnee par Humain:
---------------------------------------

Bonjour. Je m'appelle Robot et je distribue les cartes.
Votre main est:
7♡ 4♠ 9♣ 5♣ 9♠ Q♡ A♠ 10♢ J♠ 5♡ 7♢ 6♢ 10♠ Q♢ 4♡ Q♣ J♡ 7♠ 6♡ 6♠ 3♠ 3♢ 8♠ 10♣ K♢ 6♣ 
Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.
Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ 
J'ai 7 cartes. Si 1 est la position de ma première carte et
7 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 7: 6
Vous avez demande ma 6ème carte.
La voila. C'est un A♣
Avec A♣ ajouté, votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ A♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ Q♣ 10♣ 7♢ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2ème carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ 10♣ 7♢ K♢ 
J'ai 5 cartes. Si 1 est la position de ma première carte et
5 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 5: 3
Vous avez demande ma 3ème carte.
La voila. C'est un 10♡
Avec 10♡ ajouté, votre main est:
8♠ 10♣ 7♢ K♢ 10♡ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
7♢ 8♠ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ K♢ 
J'ai 3 cartes. Si 1 est la position de ma première carte et
3 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 3: 1
Vous avez demande ma 1ère carte.
La voila. C'est un K♣
Avec K♣ ajouté, votre main est:
8♠ K♢ K♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
J'ai terminé toutes les cartes.
Felicitations! Vous, Humain, vous avez gagné.
>>> 
'''

##################################################################################################################
'''
Un exemple de partie gagnee par Robot:
---------------------------------------

Bonjour. Je m'appele Robot et je donne les cartes.
Votre main de cartes est:
3♣ 6♣ 2♢ 10♡ 10♠ 8♢ 5♣ Q♣ 4♡ 8♠ 5♠ J♢ 3♢ A♠ 7♡ 3♠ A♣ 9♡ 3♡ 9♣ 8♣ 6♠ 7♣ 6♢ K♠ Q♠ 
Ne vous inquitez pas, je ne peux pas voir votres cartes ou leur ordre.
Maintenant defaussez toutes les paires de votre main. Je vais faire ca aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ 
J'ai 5 cartes. Si 1 est la position de ma premiere carte et
5 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 5: 5
Vous avez demande ma 5-eme carte.
La voila. C'est un K♣
Avec K♣ ajoute, votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ K♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 6♣ 8♣ 4♡ 2♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
J♢ 8♣ 4♡ 2♢ 
J'ai 3 cartes. Si 1 est la position de ma premiere carte et
3 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 3: 3
Vous avez demande ma 3-eme carte.
La voila. C'est un 8♡
Avec 8♡ ajoute, votre main est:
J♢ 8♣ 4♡ 2♢ 8♡ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
4♡ 2♢ J♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ J♢ 
J'ai 1 cartes. Si 1 est la position de ma premiere carte et
1 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 1: 1
Vous avez demande ma 1-ere carte.
La voila. C'est un 4♣
Avec 4♣ ajoute, votre main est:
4♡ J♢ 4♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 
Appuyez Enter pour continuer. 
J'ai terminé toutes les cartes.
Vous avez perdu! Moi, Robot, j'ai gagné.
>>> 
'''
##################################################################################################################
