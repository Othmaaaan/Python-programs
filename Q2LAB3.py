def activitesottawa(temp):
    if temp>=80.0:
        return 1
    elif 60.0<=temp and temp<80.0:
        return 2
    elif 40.0<=temp and temp<60.0:
        return 3
    elif temp<40.0:
        return 4
temp=float(input("entrez la temperature: "))
resultat= activitesottawa(temp)
if resultat==1:
    print("natation")
elif resultat==2:
    print("soccer")
elif resultat==3:
    print("volleyball")
elif resultat==4:
    print("ski")
