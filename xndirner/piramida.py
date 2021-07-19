a = int(input("mutq tiv : "))

def piramida(x):
    c = 1
    x = "*"
    st = " "
    b = 1
    bn = "*" + " "
    while c < a:
        if c == 1:
            g = (a*2/2-b) * st + c * x
        else:
            g = (a*2/2-b) * st + c * bn
        print(g)
        b+=1
        c+=1
piramida(a)

def adimarip(x):
    e = 1
    c = a
    x = "*"
    st = " "
    b = 0
    bn = "*" + " "
    while e <= a:
        if c != 1:
            g = (a/a-1+b) * st + c * bn
        else:
            g = (a*2/2-1) * st + c * x
        print(g)
        b+=1
        c-=1
        e+=1
adimarip(a)



    
        
