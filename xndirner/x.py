st = "hello good world"
dz=("a","u","i","e","y","o")
def baxadzayn():
    c=0
    fc=st.split(" ")
    for i in fc:
        for j in i:
            if j not in dz:
                c+=1
                if c==1:
                    continue
                else:
                    print(j)
                    c=0
baxadzayn()

def dzaynavor():
    c=0
    fc=st.split(" ")
    for i in fc:
        for j in i:
            if j in dz:
                c+=1
                if c == 1:
                    continue
                else:
                    print(j)
                    c=0
#dzaynavor()

def ar_dzaynavor():
    c=0
    fc=st.split(" ")
    for i in range(len(fc)):
        for j in fc[i]:
            if fc[i][0] in dz:
                print(fc[i])
#ar_dzaynavor()

def haj_bar():
    c=0
    s=""
    for i in range(len(st)):
        if (ord(st[i+1])-ord(st[i]))==1:
            c+=1
            s+=st[i]
            if c==3:
                print(s)
            else:
                c=0
                print("chka")

#haj_bar()
