def numMonnaies(n):
    cents= float(n*100)
    a= int(cents//25)
    b= int(cents -(a*25))//10
    c= int(cents - (b*10)-(a*25))  //5
    d= int(cents - (c*5)-(b*10)-(a*25))
    print(a,"pieces de 25 cents")
    print(b,"pieces de 10 cents")
    print(c,"pieces de 5 cents")
    print(d,"pieces de 1 cents")
    return a+b+c+d

