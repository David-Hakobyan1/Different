# Milionater )))
import random

gamer = raw_input("name gamer: ")
def open_file():
    with open("norik.txt") as f:
        return f.read()

def filter_file(mlist):
    st=""
    l=[]
    for el in mlist:
        if el != "\n":
            st+=el
        else:
            lis=st.split("-")
            l.append(lis)
            st=""
    return l

def filter_patasxan(lis):
    st=""
    l=[]
    chisht=[]
    ls=[]
    for i in range(len(lis)):
        lis[i][1]=str(lis[i][1])
        ds=lis[i][1].split(",")
        l.append(ds)
    for j in l:
        for h in j:
            if h[0]==" ":
                chisht.append(h)
    for g in chisht:
        ls.append(g.strip())
    return ls

                
def xax(lis,tlis):
    d={}
    c=0
    while True:
        if len(lis)!=0:
            s = random.randrange(len(lis))
            print(lis[s][0])
            print(lis[s][1])
            n = raw_input("mutq: ")
            if n in tlis and n in (lis[s][1]):
                print("chisht e")
                c+=1
                d[gamer]=c
            else:
                print("sxal e")
            del lis[s]
        else:
            print("avart")
            return d

def ret_d(my_dict):
    st=""
    for key,value in my_dict.items():
        st=key+" "+str(value)
    f=open("dfile.txt","a")
    fc=f.write(str(st))
    f.close()

def result():
    with open("dfile.txt") as f:
        st=""
        lis=[]
        l=[]
        fc=f.read()
        lis.append(fc.strip().split("\n"))
        for i in lis:
            for j in i:
                l.append(j[-1])
        ls=(sorted(l))
        return ls[-3:],lis

def lavaguyn_3(res):
    for i in res[0]:
        for j in range(len(res[1][0])):
            if i in res[1][0][j]:
                print(res[1][0][j])
    #print(len(res[1][0]))
def main():
    files=open_file()
    filtered_files=filter_file(files)
    tlis=filter_patasxan(filtered_files)
    tarb=xax(filtered_files,tlis)
    rets=ret_d(tarb)
    res=result()
    lavaguyn3=lavaguyn_3(res)
main()
