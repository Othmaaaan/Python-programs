#KARIB OTHMAN
#300266967
def coder(s):
    ch=""
    
    for i in range(0,len(s),2):
        if len(s)%2==0:
       
            ch=ch+s[i+1]+s[i]
            
        



        elif len(s)%2==1:

            ch=ch+s[i+1]+s[i] 
            
            ch=ch.strip()
        
    return ch

