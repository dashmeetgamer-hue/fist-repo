def calcute():
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        cal=input("enter the simbol")
        c=a+b
        d=a-b
        e=a*b
        if cal == "+":
                print (c)
        elif cal == "-":
            print (d)
        elif cal =="*":
            print (e)
calcute()